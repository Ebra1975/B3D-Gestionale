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
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
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
        "b3d": {
            "nome": "B3D Lab",
            "sottotitolo": "Consulenza tecnica e manifattura additiva",
        },
    }


def set_cell_background(cell, color):
    cell_properties = cell._tc.get_or_add_tcPr()
    shading = OxmlElement("w:shd")
    shading.set(qn("w:fill"), color)
    cell_properties.append(shading)


def set_cell_text(cell, text, bold=False, color=None):
    cell.text = ""
    paragraph = cell.paragraphs[0]
    run = paragraph.add_run(text)
    run.bold = bold
    if color:
        run.font.color.rgb = RGBColor.from_string(color)


def add_section_title(document, text):
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.space_before = Pt(12)
    paragraph.paragraph_format.space_after = Pt(6)
    run = paragraph.add_run(text)
    run.bold = True
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(35, 87, 166)


def create_default_consulting_template(template_path):
    template_path.parent.mkdir(parents=True, exist_ok=True)

    document = Document()
    section = document.sections[0]
    section.top_margin = Cm(1.6)
    section.bottom_margin = Cm(1.6)
    section.left_margin = Cm(1.8)
    section.right_margin = Cm(1.8)

    styles = document.styles
    styles["Normal"].font.name = "Aptos"
    styles["Normal"].font.size = Pt(10.5)

    header = document.add_table(rows=1, cols=2)
    header.autofit = True
    left, right = header.rows[0].cells
    set_cell_background(left, "F3F6FA")
    set_cell_background(right, "2457A6")
    left.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    right.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

    brand = left.paragraphs[0]
    brand.paragraph_format.space_after = Pt(2)
    run = brand.add_run("{{ b3d.nome }}")
    run.bold = True
    run.font.size = Pt(18)
    run.font.color.rgb = RGBColor(23, 32, 42)
    subtitle = left.add_paragraph()
    run = subtitle.add_run("{{ b3d.sottotitolo }}")
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(97, 112, 128)

    doc_type = right.paragraphs[0]
    doc_type.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = doc_type.add_run("PROPOSTA DI CONSULENZA")
    run.bold = True
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(255, 255, 255)
    meta = right.add_paragraph()
    meta.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = meta.add_run("N. {{ preventivo.numero }} | {{ preventivo.data }}")
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(255, 255, 255)

    document.add_paragraph()

    summary = document.add_table(rows=4, cols=2)
    summary.style = "Table Grid"
    rows = [
        ("Cliente", "{{ cliente.nome }}"),
        ("Referente", "{{ cliente.referente }}"),
        ("Oggetto", "{{ preventivo.oggetto }}"),
        ("Validita proposta", "{{ preventivo.validita }}"),
    ]
    for row, (label, value) in zip(summary.rows, rows):
        label_cell, value_cell = row.cells
        set_cell_background(label_cell, "EEF2F7")
        set_cell_text(label_cell, label, bold=True)
        set_cell_text(value_cell, value)

    add_section_title(document, "Contesto e richiesta")
    paragraph = document.add_paragraph("{{ preventivo.descrizione }}")
    paragraph.paragraph_format.space_after = Pt(8)

    add_section_title(document, "Soluzione proposta")
    document.add_paragraph("{{ configurazione.nome }}").runs[0].bold = True
    document.add_paragraph("{{ configurazione.descrizione }}")

    technical = document.add_table(rows=5, cols=2)
    technical.style = "Table Grid"
    rows = [
        ("Materiale / tecnologia", "{{ configurazione.materiale }}"),
        ("Processo", "{{ configurazione.processo }}"),
        ("Trattamento", "{{ configurazione.trattamento }}"),
        ("Durata attesa", "{{ configurazione.durata }}"),
        ("Modalita operativa", "{{ configurazione.modalita }}"),
    ]
    for row, (label, value) in zip(technical.rows, rows):
        label_cell, value_cell = row.cells
        set_cell_background(label_cell, "F8FAFC")
        set_cell_text(label_cell, label, bold=True)
        set_cell_text(value_cell, value)

    add_section_title(document, "Sintesi economica")
    table = document.add_table(rows=1, cols=4)
    table.style = "Table Grid"
    header = table.rows[0].cells
    labels = ["Voce", "Quantita", "Unitario", "Totale"]
    for cell, label in zip(header, labels):
        set_cell_background(cell, "2457A6")
        set_cell_text(cell, label, bold=True, color="FFFFFF")
    row = table.add_row().cells
    row[0].text = "{{ proposta.voce }}"
    row[1].text = "{{ preventivo.quantita }}"
    row[2].text = "{{ proposta.unitario }}"
    row[3].text = "{{ proposta.totale }}"

    total_row = table.add_row().cells
    total_row[0].merge(total_row[2])
    set_cell_background(total_row[0], "EEF2F7")
    set_cell_background(total_row[3], "EEF2F7")
    set_cell_text(total_row[0], "Totale proposta", bold=True)
    set_cell_text(total_row[3], "{{ proposta.totale }}", bold=True)

    fiscal_note = document.add_paragraph()
    fiscal_note.paragraph_format.space_before = Pt(6)
    run = fiscal_note.add_run("Nota: ")
    run.bold = True
    fiscal_note.add_run("{{ proposta.nota_fiscale }}")

    add_section_title(document, "Condizioni e note")
    document.add_paragraph("{{ preventivo.condizioni }}")
    document.add_paragraph("{{ configurazione.note }}")

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = footer.add_run("B3D Lab - Documento generato dal gestionale interno")
    run.font.size = Pt(8)
    run.font.color.rgb = RGBColor(97, 112, 128)

    document.save(template_path)
    return template_path


def get_or_create_default_consulting_template():
    generated_template = (
        DocumentTemplate.objects.filter(
            document_type=DocumentTemplate.DocumentType.CONSULTING_ESTIMATE,
            active=True,
            name__startswith="Preventivo consulenza base",
        )
        .order_by("-uploaded_at", "-id")
        .first()
    )
    if generated_template:
        relative_path = Path("templates") / "consulting_estimate" / "preventivo_consulenza_base_v2.docx"
        absolute_path = Path(settings.MEDIA_ROOT) / relative_path
        create_default_consulting_template(absolute_path)
        generated_template.template_file = str(relative_path).replace("\\", "/")
        generated_template.template_version = "v2"
        generated_template.notes = (
            "Template base generato dal gestionale e rifinito nello Sprint 03. "
            "Resta sostituibile con un template DOCX personalizzato."
        )
        generated_template.save(update_fields=["template_file", "template_version", "notes"])
        return generated_template

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

    relative_path = Path("templates") / "consulting_estimate" / "preventivo_consulenza_base_v2.docx"
    absolute_path = Path(settings.MEDIA_ROOT) / relative_path
    create_default_consulting_template(absolute_path)

    return DocumentTemplate.objects.create(
        name="Preventivo consulenza base",
        document_type=DocumentTemplate.DocumentType.CONSULTING_ESTIMATE,
        profile="consulting",
        template_file=str(relative_path).replace("\\", "/"),
        template_version="v2",
        active=True,
        notes=(
            "Template base generato dal gestionale e rifinito nello Sprint 03. "
            "Resta sostituibile con un template DOCX personalizzato."
        ),
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
