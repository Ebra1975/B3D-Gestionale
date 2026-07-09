from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q

from apps.customers.models import Customer
from apps.documents.models import GeneratedDocument
from apps.estimates.models import Estimate
from apps.inventory.models import Material, Printer
from apps.jobs.models import Job


CONFIRM_TEXT = "PULISCI DATI TEST"


def test_customer_filter():
    return (
        Q(name__icontains="demo")
        | Q(name__startswith="TEST PDF BMAX")
        | Q(email__icontains="example.")
        | Q(email__icontains="example.local")
        | Q(notes__icontains="dimostrativo")
        | Q(notes__icontains="verify_pdf_export")
    )


def test_estimate_filter():
    return (
        Q(number="B3D-2026-001")
        | Q(subject__icontains="demo")
        | Q(subject__startswith="TEST PDF BMAX")
        | Q(description__icontains="preventivo di prova")
        | Q(internal_notes__icontains="seed_demo_data")
        | Q(internal_notes__icontains="verify_pdf_export")
        | Q(configurations__internal_notes__icontains="verify_pdf_export")
    )


def test_material_filter():
    return (
        Q(name__icontains="demo")
        | Q(brand__icontains="demo")
        | Q(supplier__icontains="demo")
        | Q(technical_notes__icontains="dimostrativo")
    )


def test_printer_filter():
    return (
        Q(name__icontains="demo")
        | Q(model__icontains="demo")
        | Q(notes__icontains="dimostrativa")
    )


class Command(BaseCommand):
    help = "Prepara l'ambiente all'uso reale mostrando o rimuovendo i dati di test riconoscibili."

    def add_arguments(self, parser):
        parser.add_argument(
            "--apply",
            action="store_true",
            help="Esegue davvero la pulizia. Senza questa opzione mostra solo cosa verrebbe rimosso.",
        )
        parser.add_argument(
            "--confirm",
            default="",
            help=f"Testo di conferma richiesto per la pulizia reale: {CONFIRM_TEXT}",
        )

    def handle(self, *args, **options):
        plan = self.build_plan()
        self.print_plan(plan)

        if not options["apply"]:
            self.stdout.write("")
            self.stdout.write(
                self.style.WARNING(
                    "Anteprima completata: nessun dato e stato cancellato. "
                    "Prima della pulizia reale creare o verificare un backup recente."
                )
            )
            return

        if options["confirm"] != CONFIRM_TEXT:
            raise CommandError(
                f"Per pulire davvero i dati test usare: --apply --confirm \"{CONFIRM_TEXT}\""
            )

        self.delete_generated_files(plan["generated_documents"])
        deleted = self.delete_data(plan)

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS("Pulizia dati test completata."))
        for label, count in deleted:
            self.stdout.write(f"- {label}: {count}")
        self.stdout.write(
            "Controllo consigliato: aprire dashboard, clienti, preventivi, commesse e documenti dal browser."
        )

    def build_plan(self):
        estimates = Estimate.objects.filter(test_estimate_filter()).distinct()
        customers = Customer.objects.filter(test_customer_filter()).distinct()
        jobs = Job.objects.filter(estimate__in=estimates).distinct()
        generated_documents = GeneratedDocument.objects.filter(estimate__in=estimates).distinct()

        protected_material_ids = Estimate.objects.exclude(id__in=estimates).values_list(
            "configurations__material_id", flat=True
        )
        materials = Material.objects.filter(test_material_filter()).exclude(id__in=protected_material_ids).distinct()

        protected_printer_ids = Estimate.objects.exclude(id__in=estimates).values_list(
            "configurations__printer_id", flat=True
        )
        printers = Printer.objects.filter(test_printer_filter()).exclude(id__in=protected_printer_ids).distinct()

        real_estimates = Estimate.objects.exclude(id__in=estimates)
        real_jobs = Job.objects.exclude(id__in=jobs)
        removable_customers = (
            customers.exclude(estimates__in=real_estimates)
            .exclude(jobs__in=real_jobs)
            .distinct()
        )

        estimate_ids = list(estimates.values_list("id", flat=True))
        customer_ids = list(removable_customers.values_list("id", flat=True))
        job_ids = list(jobs.values_list("id", flat=True))
        generated_document_ids = list(generated_documents.values_list("id", flat=True))
        material_ids = list(materials.values_list("id", flat=True))
        printer_ids = list(printers.values_list("id", flat=True))

        return {
            "customers": Customer.objects.filter(id__in=customer_ids),
            "estimates": Estimate.objects.filter(id__in=estimate_ids),
            "jobs": Job.objects.filter(id__in=job_ids),
            "generated_documents": GeneratedDocument.objects.filter(id__in=generated_document_ids),
            "materials": Material.objects.filter(id__in=material_ids),
            "printers": Printer.objects.filter(id__in=printer_ids),
        }

    def print_plan(self, plan):
        self.stdout.write("Preparazione uso reale - dati test riconosciuti")
        self.stdout.write("")
        self.print_queryset("Clienti test", plan["customers"], "name")
        self.print_queryset("Preventivi test", plan["estimates"], "number")
        self.print_queryset("Commesse collegate a test", plan["jobs"], "number")
        self.print_queryset("Documenti generati test", plan["generated_documents"], "id")
        self.print_queryset("Materiali demo non usati da preventivi reali", plan["materials"], "name")
        self.print_queryset("Stampanti demo non usate da preventivi reali", plan["printers"], "name")

    def print_queryset(self, title, queryset, field_name):
        count = queryset.count()
        self.stdout.write(f"{title}: {count}")
        for item in queryset.order_by("id")[:10]:
            value = getattr(item, field_name)
            self.stdout.write(f"  - {value}: {item}")
        if count > 10:
            self.stdout.write(f"  - altri {count - 10} elementi non mostrati")

    def delete_generated_files(self, generated_documents):
        for document in generated_documents:
            for file_field in [document.docx_file, document.pdf_file]:
                if file_field and file_field.name and default_storage.exists(file_field.name):
                    default_storage.delete(file_field.name)

    def delete_data(self, plan):
        deleted = []
        deleted.append(("commesse test", plan["jobs"].delete()[0]))
        deleted.append(("preventivi test e dati collegati", plan["estimates"].delete()[0]))
        deleted.append(("clienti test", plan["customers"].delete()[0]))
        deleted.append(("materiali demo non usati", plan["materials"].delete()[0]))
        deleted.append(("stampanti demo non usate", plan["printers"].delete()[0]))
        return deleted
