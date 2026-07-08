from decimal import Decimal
from datetime import timedelta

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone

from apps.customers.models import Customer
from apps.documents.services import (
    find_libreoffice_command,
    generate_consulting_estimate_docx,
    generate_internal_estimate_docx,
    generate_supply_estimate_docx,
)
from apps.estimates.models import CostItem, Estimate, EstimateConfiguration


class Command(BaseCommand):
    help = "Crea un preventivo di test e verifica che DOCX e PDF vengano generati."

    def handle(self, *args, **options):
        libreoffice_command = find_libreoffice_command()
        if not libreoffice_command:
            raise CommandError("LibreOffice non trovato: impossibile convertire DOCX in PDF.")

        self.stdout.write(f"LibreOffice trovato: {libreoffice_command}")

        with transaction.atomic():
            customer = Customer.objects.create(
                name="TEST PDF BMAX - eliminabile",
                customer_type=Customer.CustomerType.COMPANY,
                contact_person="Verifica automatica",
                email="test-pdf-bmax@example.local",
                address="Cliente di prova per verifica PDF BMAX",
                notes="Creato dal comando verify_pdf_export. Puo essere eliminato dopo la verifica.",
            )
            estimate = Estimate.objects.create(
                customer=customer,
                subject="TEST PDF BMAX - verifica conversione LibreOffice",
                description=(
                    "Preventivo di prova creato automaticamente per verificare che "
                    "sul BMAX vengano generati sia DOCX sia PDF."
                ),
                date=timezone.localdate(),
                valid_until=timezone.localdate() + timedelta(days=15),
                quantity=2,
                general_terms="Condizioni di prova per verifica tecnica interna.",
                internal_notes="Preventivo creato automaticamente: non usare verso clienti.",
            )
            configuration = EstimateConfiguration.objects.create(
                estimate=estimate,
                name="Configurazione test PDF BMAX",
                description="Configurazione fittizia per prova documento reale.",
                process="FDM / verifica sistema",
                treatment="Nessuno",
                expected_duration="2 giorni lavorativi",
                operating_mode="Prova interna di generazione documento.",
                quantity=2,
                public_notes="Prova tecnica interna.",
                internal_notes="Creato dal comando verify_pdf_export.",
                is_selected=True,
            )
            CostItem.objects.create(
                configuration=configuration,
                category=CostItem.Category.DESIGN,
                description="Consulenza tecnica e preparazione file",
                quantity=Decimal("1.00"),
                unit="voce",
                unit_cost=Decimal("80.00"),
                visible_internal=True,
                visible_consulting=False,
                visible_supply=True,
                notes="Voce di test.",
            )
            CostItem.objects.create(
                configuration=configuration,
                category=CostItem.Category.MACHINE_TIME,
                description="Tempo macchina di prova",
                quantity=Decimal("2.00"),
                unit="h",
                unit_cost=Decimal("12.50"),
                visible_internal=True,
                visible_consulting=False,
                visible_supply=True,
                notes="Voce di test.",
            )
            CostItem.objects.create(
                configuration=configuration,
                category=CostItem.Category.MARGIN,
                description="Margine commerciale di prova",
                quantity=Decimal("1.00"),
                unit="voce",
                unit_cost=Decimal("25.00"),
                visible_internal=True,
                visible_consulting=False,
                visible_supply=True,
                notes="Voce di test.",
            )

        self.stdout.write(f"Preventivo test creato: {estimate.number}")

        documents = [
            ("cliente consulenza", generate_consulting_estimate_docx(estimate)),
            ("interno dettagliato", generate_internal_estimate_docx(estimate)),
            ("fornitura/artigiano", generate_supply_estimate_docx(estimate)),
        ]

        missing_pdf = []
        for label, document in documents:
            self.stdout.write(f"Documento {label}:")
            self.stdout.write(f"  DOCX: {document.docx_file.name or 'MANCANTE'}")
            self.stdout.write(f"  PDF:  {document.pdf_file.name or 'MANCANTE'}")
            if not document.docx_file or not document.pdf_file:
                missing_pdf.append(label)

        if missing_pdf:
            raise CommandError(
                "PDF non generato per: "
                + ", ".join(missing_pdf)
                + ". Controllare LibreOffice nel container web."
            )

        self.stdout.write(self.style.SUCCESS("Verifica PDF completata: DOCX e PDF generati correttamente."))
