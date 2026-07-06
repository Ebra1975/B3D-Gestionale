import re
import shutil
import subprocess
import tempfile
from decimal import Decimal
from pathlib import Path

from django.conf import settings
from django.db.models import Max
from docxtpl import DocxTemplate
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt, RGBColor

from .models import DocumentTemplate, GeneratedDocument


def money(value):
    amount = value or Decimal("0.00")
    return f"{amount:.2f} EUR"


def safe_filename(value):
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "_", value).strip("_")
    return cleaned or "documento"


def render_docx_template(template_path, output_path, context):
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    document = DocxTemplate(template_path)
    document.render(context)
    document.save(output)
    return output


def find_libreoffice_command():
    configured_path = getattr(settings, "LIBREOFFICE_PATH", "")
    if configured_path and Path(configured_path).exists():
        return configured_path

    windows_path = Path("C:/Program Files/LibreOffice/program/soffice.com")
    if windows_path.exists():
        return str(windows_path)

    return shutil.which("soffice") or shutil.which("libreoffice")


def convert_docx_to_pdf(docx_path, output_dir):
    command = find_libreoffice_command()
    if not command:
        return None

    docx_path = Path(docx_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="b3dlab_lo_profile_") as profile_dir:
        user_installation = Path(profile_dir).resolve().as_uri()
        result = subprocess.run(
            [
                command,
                f"-env:UserInstallation={user_installation}",
                "--headless",
                "--norestore",
                "--convert-to",
                "pdf",
                "--outdir",
                str(output_dir),
                str(docx_path),
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    pdf_path = output_dir / f"{docx_path.stem}.pdf"
    if result.returncode != 0 or not pdf_path.exists():
        return None
    return pdf_path


def selected_configuration(estimate):
    selected = [configuration for configuration in estimate.configurations.all() if configuration.is_selected]
    if selected:
        return selected[0]
    configurations = list(estimate.configurations.all())
    return configurations[0] if configurations else None


def build_consulting_context(estimate):
    configuration = selected_configuration(estimate)
    total = configuration.total if configuration else Decimal("0.00")
    unit_price = configuration.unit_price if configuration else Decimal("0.00")

    return {
        "cliente": {
            "nome": estimate.customer.name,
            "referente": estimate.customer.contact_person or "",
            "email": estimate.customer.email or "",
            "indirizzo": estimate.customer.address or "",
            "codice_fiscale": estimate.customer.tax_code or "",
        },
        "preventivo": {
            "numero": estimate.number,
            "oggetto": estimate.subject,
            "descrizione": estimate.description or "",
            "data": estimate.date.strftime("%d/%m/%Y"),
            "validita": estimate.valid_until.strftime("%d/%m/%Y") if estimate.valid_until else "",
            "quantita": configuration.quantity if configuration else estimate.quantity,
            "condizioni": estimate.general_terms or "Condizioni da definire in base alla conferma del cliente.",
        },
        "configurazione": {
            "nome": configuration.name if configuration else "Configurazione da completare",
            "descrizione": configuration.description if configuration else "",
            "materiale": str(configuration.material) if configuration and configuration.material else "",
            "processo": configuration.process if configuration else "",
            "trattamento": configuration.treatment if configuration else "",
            "durata": configuration.expected_duration if configuration else "",
            "modalita": configuration.operating_mode if configuration else "",
            "note": configuration.public_notes if configuration else "",
            "totale": money(total),
            "unitario": money(unit_price),
        },
        "proposta": {
            "voce": (
                "Compenso per consulenza tecnica, progettazione, validazione "
                "e realizzazione"
            ),
            "totale": money(total),
            "unitario": money(unit_price),
            "nota_fiscale": (
                "Dicitura commerciale e fiscale da validare con commercialista."
            ),
        },
    }


def create_default_consulting_template(template_path):
    template_path.parent.mkdir(parents=True, exist_ok=True)

    document = Document()
    section = document.sections[0]
    section.top_margin = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(2.0)
    section.right_margin = Cm(2.0)

    styles = document.styles
    styles["Normal"].font.name = "Arial"
    styles["Normal"].font.size = Pt(10.5)

    title = document.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = title.add_run("B3D Lab")
    run.bold = True
    run.font.size = Pt(18)
    run.font.color.rgb = RGBColor(35, 58, 89)

    subtitle = document.add_paragraph()
    run = subtitle.add_run("Proposta di consulenza tecnica")
    run.bold = True
    run.font.size = Pt(14)

    document.add_paragraph("Preventivo n. {{ preventivo.numero }} del {{ preventivo.data }}")
    document.add_paragraph("Cliente: {{ cliente.nome }}")
    document.add_paragraph("Oggetto: {{ preventivo.oggetto }}")

    document.add_heading("Contesto e richiesta", level=1)
    document.add_paragraph("{{ preventivo.descrizione }}")

    document.add_heading("Configurazione proposta", level=1)
    document.add_paragraph("{{ configurazione.nome }}")
    document.add_paragraph("{{ configurazione.descrizione }}")
    document.add_paragraph("Materiale / processo: {{ configurazione.materiale }} {{ configurazione.processo }}")
    document.add_paragraph("Modalita operativa: {{ configurazione.modalita }}")
    document.add_paragraph("Durata attesa: {{ configurazione.durata }}")
    document.add_paragraph("Note: {{ configurazione.note }}")

    document.add_heading("Compenso", level=1)
    table = document.add_table(rows=1, cols=3)
    table.style = "Table Grid"
    header = table.rows[0].cells
    header[0].text = "Voce"
    header[1].text = "Quantita"
    header[2].text = "Totale"
    row = table.add_row().cells
    row[0].text = "{{ proposta.voce }}"
    row[1].text = "{{ preventivo.quantita }}"
    row[2].text = "{{ proposta.totale }}"

    document.add_paragraph("Prezzo unitario indicativo: {{ proposta.unitario }}")
    document.add_paragraph("{{ proposta.nota_fiscale }}")

    document.add_heading("Condizioni", level=1)
    document.add_paragraph("Validita proposta: {{ preventivo.validita }}")
    document.add_paragraph("{{ preventivo.condizioni }}")

    document.save(template_path)
    return template_path


def get_or_create_default_consulting_template():
    template = (
        DocumentTemplate.objects.filter(
            document_type=DocumentTemplate.DocumentType.CONSULTING_ESTIMATE,
            active=True,
        )
        .order_by("-uploaded_at", "-id")
        .first()
    )
    if template:
        return template

    relative_path = Path("templates") / "consulting_estimate" / "preventivo_consulenza_base_v1.docx"
    absolute_path = Path(settings.MEDIA_ROOT) / relative_path
    create_default_consulting_template(absolute_path)

    return DocumentTemplate.objects.create(
        name="Preventivo consulenza base",
        document_type=DocumentTemplate.DocumentType.CONSULTING_ESTIMATE,
        profile="consulting",
        template_file=str(relative_path).replace("\\", "/"),
        template_version="v1",
        active=True,
        notes="Template base generato dal gestionale per il primo flusso reale Sprint 02.",
    )


def generate_consulting_estimate_docx(estimate):
    template = get_or_create_default_consulting_template()
    latest_version = (
        GeneratedDocument.objects.filter(
            estimate=estimate,
            document_type=GeneratedDocument.DocumentType.CONSULTING,
        ).aggregate(value=Max("version"))["value"]
        or 0
    )
    version = latest_version + 1
    filename = f"preventivo_{safe_filename(estimate.number)}_consulenza_v{version}.docx"
    relative_path = Path("generated") / safe_filename(estimate.number) / "consulting" / filename
    output_path = Path(settings.MEDIA_ROOT) / relative_path

    render_docx_template(
        template.template_file.path,
        output_path,
        build_consulting_context(estimate),
    )
    pdf_path = convert_docx_to_pdf(output_path, output_path.parent)
    pdf_file = ""
    if pdf_path:
        pdf_file = str(relative_path.with_suffix(".pdf")).replace("\\", "/")

    return GeneratedDocument.objects.create(
        estimate=estimate,
        template=template,
        document_type=GeneratedDocument.DocumentType.CONSULTING,
        version=version,
        docx_file=str(relative_path).replace("\\", "/"),
        pdf_file=pdf_file,
        notes="Documento consulenza generato dal dettaglio preventivo.",
    )
