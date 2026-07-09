from datetime import timedelta

from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone

from apps.core.views import build_dashboard_context
from apps.customers.models import Customer, CustomerAgreement, CustomerCommercialDocument
from apps.documents.models import GeneratedDocument
from apps.estimates.models import Estimate, EstimateConfiguration
from apps.jobs.models import Job


class DashboardTests(TestCase):
    def test_dashboard_context_includes_operational_followups(self):
        today = timezone.localdate()
        customer = Customer.objects.create(name="Cliente Sprint 06")
        estimate = Estimate.objects.create(
            number="B3D-2026-900",
            customer=customer,
            subject="Preventivo da seguire",
            date=today,
            valid_until=today + timedelta(days=3),
            status=Estimate.Status.SENT,
        )
        configuration = EstimateConfiguration.objects.create(
            estimate=estimate,
            name="Configurazione confermata",
            is_selected=True,
        )
        Job.objects.create(
            number="COMM-2026-900",
            estimate=estimate,
            customer=customer,
            selected_configuration=configuration,
            status=Job.Status.PRINTING,
            expected_delivery=today + timedelta(days=2),
        )
        CustomerAgreement.objects.create(
            customer=customer,
            name="Accordo annuale",
            status=CustomerAgreement.Status.ACTIVE,
            ends_on=today + timedelta(days=20),
        )
        CustomerCommercialDocument.objects.create(
            customer=customer,
            name="NDA firmato",
            document_type=CustomerCommercialDocument.DocumentType.NDA,
            status=CustomerCommercialDocument.Status.ACTIVE,
            expires_on=today + timedelta(days=25),
        )

        context = build_dashboard_context()

        self.assertEqual(context["estimates_to_follow"][0].number, "B3D-2026-900")
        self.assertEqual(context["jobs_to_follow"][0].number, "COMM-2026-900")
        self.assertEqual(context["agreements_to_follow"][0].name, "Accordo annuale")
        self.assertEqual(context["commercial_documents_to_follow"][0].name, "NDA firmato")


class PrepareRealUseCommandTests(TestCase):
    def test_preview_does_not_delete_test_data(self):
        customer = Customer.objects.create(
            name="TEST PDF BMAX - eliminabile",
            email="test-pdf-bmax@example.local",
            notes="Creato dal comando verify_pdf_export.",
        )
        estimate = Estimate.objects.create(
            customer=customer,
            subject="TEST PDF BMAX - verifica conversione LibreOffice",
            date=timezone.localdate(),
            internal_notes="Preventivo creato da verify_pdf_export.",
        )

        call_command("prepare_real_use")

        self.assertTrue(Customer.objects.filter(id=customer.id).exists())
        self.assertTrue(Estimate.objects.filter(id=estimate.id).exists())

    def test_apply_removes_only_customers_without_real_links(self):
        test_customer = Customer.objects.create(
            name="Studio Tecnico Demo",
            email="demo@example.com",
            notes="Cliente dimostrativo.",
        )
        protected_customer = Customer.objects.create(
            name="Cliente Demo con lavoro reale",
            email="demo-reale@example.com",
            notes="Nome demo ma con preventivo reale da conservare.",
        )
        Estimate.objects.create(
            number="B3D-2026-001",
            customer=test_customer,
            subject="Supporti demo",
            date=timezone.localdate(),
            internal_notes="Preventivo dimostrativo creato dal comando seed_demo_data.",
        )
        real_estimate = Estimate.objects.create(
            number="B3D-2026-777",
            customer=protected_customer,
            subject="Lavoro reale da conservare",
            date=timezone.localdate(),
        )
        real_document = GeneratedDocument.objects.create(
            estimate=real_estimate,
            document_type=GeneratedDocument.DocumentType.CONSULTING,
            version=1,
        )

        call_command("prepare_real_use", "--apply", "--confirm", "PULISCI DATI TEST")

        self.assertFalse(Customer.objects.filter(id=test_customer.id).exists())
        self.assertTrue(Customer.objects.filter(id=protected_customer.id).exists())
        self.assertTrue(Estimate.objects.filter(number="B3D-2026-777").exists())
        self.assertTrue(GeneratedDocument.objects.filter(id=real_document.id).exists())
