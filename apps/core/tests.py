from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from apps.core.views import build_dashboard_context
from apps.customers.models import Customer, CustomerAgreement, CustomerCommercialDocument
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
