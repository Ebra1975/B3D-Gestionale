from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.customers.models import Customer
from apps.documents.services import generate_consulting_estimate_docx
from apps.estimates.models import CostItem, Estimate, EstimateConfiguration
from apps.inventory.models import Material, Printer


class Command(BaseCommand):
    help = "Crea un preventivo demo realistico per provare il flusso consulenza B3D Lab."

    def add_arguments(self, parser):
        parser.add_argument(
            "--with-documents",
            action="store_true",
            help="Genera anche DOCX/PDF consulenza per il preventivo demo.",
        )

    def handle(self, *args, **options):
        customer, _ = Customer.objects.update_or_create(
            name="Studio Tecnico Demo",
            defaults={
                "customer_type": Customer.CustomerType.COMPANY,
                "contact_person": "Referente demo",
                "email": "demo@example.com",
                "phone": "+39 000 0000000",
                "address": "Indirizzo demo",
                "tax_code": "P.IVA demo",
                "notes": "Cliente dimostrativo per testare il flusso preventivo consulenza.",
            },
        )

        material, _ = Material.objects.update_or_create(
            name="PETG UV demo",
            brand="B3D Lab",
            color="Nero",
            defaults={
                "material_type": "FDM",
                "cost_per_unit": Decimal("24.00"),
                "supplier": "Fornitore demo",
                "technical_notes": "Materiale dimostrativo per componenti funzionali da interno/esterno leggero.",
                "uv_resistance": "Media",
                "temperature_notes": "Uso ordinario, verificare condizioni reali di esercizio.",
                "available": True,
            },
        )

        printer, _ = Printer.objects.update_or_create(
            name="B3D FDM grande formato demo",
            defaults={
                "model": "FDM 400x400x450",
                "ownership": Printer.Ownership.OWNED,
                "build_volume": "400x400x450 mm",
                "enclosed_chamber": False,
                "supported_materials": "PLA, PETG, ASA da validare sul caso specifico.",
                "hourly_cost": Decimal("0.85"),
                "estimated_power_watts": 350,
                "notes": "Macchina dimostrativa per calcolo preventivi.",
                "active": True,
            },
        )

        estimate, _ = Estimate.objects.update_or_create(
            number="B3D-2026-001",
            defaults={
                "customer": customer,
                "subject": "Supporti tecnici personalizzati per attrezzatura",
                "description": (
                    "Studio preliminare, progettazione e realizzazione tramite manifattura "
                    "additiva di supporti tecnici personalizzati per il fissaggio di una "
                    "piccola attrezzatura in ambiente operativo."
                ),
                "date": timezone.localdate(),
                "valid_until": timezone.localdate() + timezone.timedelta(days=30),
                "status": Estimate.Status.DRAFT,
                "quantity": 12,
                "preferred_document_profile": Estimate.DocumentProfile.CONSULTING,
                "general_terms": (
                    "Validita 30 giorni. Tempi e modalita definitive da confermare dopo "
                    "validazione tecnica del prototipo o dei file esecutivi."
                ),
                "internal_notes": "Preventivo dimostrativo creato dal comando seed_demo_data.",
            },
        )

        configuration, _ = EstimateConfiguration.objects.update_or_create(
            estimate=estimate,
            name="Configurazione consulenza PETG",
            defaults={
                "description": (
                    "Soluzione in PETG con progettazione adattata al caso d'uso, "
                    "validazione dimensionale e realizzazione di 12 unita."
                ),
                "material": material,
                "printer": printer,
                "process": "FDM",
                "treatment": "Rimozione supporti e controllo dimensionale base",
                "expected_duration": "7-10 giorni lavorativi dopo conferma",
                "operating_mode": (
                    "Analisi richiesta, preparazione modello, stampa additiva, controllo "
                    "funzionale e consegna dei componenti validati."
                ),
                "quantity": 12,
                "material_weight_per_unit": Decimal("0.180"),
                "machine_time_hours_per_unit": Decimal("2.50"),
                "public_notes": "La proposta include validazione tecnica base prima della consegna.",
                "internal_notes": "Configurazione dimostrativa per testare costi, totale e documento consulenza.",
                "is_selected": True,
            },
        )

        self.upsert_cost(
            configuration,
            CostItem.Category.MATERIAL,
            "Materiale PETG UV demo",
            Decimal("2.16"),
            "kg",
            Decimal("24.00"),
        )
        self.upsert_cost(
            configuration,
            CostItem.Category.MACHINE_TIME,
            "Tempo macchina FDM",
            Decimal("30.00"),
            "h",
            Decimal("0.85"),
        )
        self.upsert_cost(
            configuration,
            CostItem.Category.DESIGN,
            "Consulenza tecnica e progettazione",
            Decimal("6.00"),
            "h",
            Decimal("38.00"),
        )
        self.upsert_cost(
            configuration,
            CostItem.Category.SETUP,
            "Setup, slicing e validazione processo",
            Decimal("1.00"),
            "voce",
            Decimal("75.00"),
        )
        self.upsert_cost(
            configuration,
            CostItem.Category.POST_PROCESSING,
            "Post-processing e controllo base",
            Decimal("12.00"),
            "pz",
            Decimal("4.50"),
        )
        self.upsert_cost(
            configuration,
            CostItem.Category.MARGIN,
            "Margine operativo",
            Decimal("1.00"),
            "voce",
            Decimal("120.00"),
        )

        document_message = ""
        if options["with_documents"]:
            document = generate_consulting_estimate_docx(estimate)
            document_message = f" Documento consulenza v{document.version} generato."

        self.stdout.write(
            self.style.SUCCESS(
                f"Creato/aggiornato preventivo demo {estimate.number} "
                f"con totale {configuration.total:.2f} EUR.{document_message}"
            )
        )

    def upsert_cost(self, configuration, category, description, quantity, unit, unit_cost):
        cost_item, _ = CostItem.objects.update_or_create(
            configuration=configuration,
            category=category,
            description=description,
            defaults={
                "quantity": quantity,
                "unit": unit,
                "unit_cost": unit_cost,
                "visible_internal": True,
                "visible_consulting": False,
                "visible_supply": True,
            },
        )
        cost_item.save()
        return cost_item
