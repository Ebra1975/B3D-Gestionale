from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from apps.customers.models import Customer, CustomerAgreement, CustomerCommercialDocument
from apps.estimates.models import Estimate
from apps.estimates.views import build_customer_commercial_memory, build_estimate_readiness


class EstimateDetailTests(TestCase):
    def test_customer_commercial_memory_includes_alerts(self):
        today = timezone.localdate()
        customer = Customer.objects.create(name="Cliente Sprint 07")
        agreement = CustomerAgreement.objects.create(
            customer=customer,
            name="Accordo consulenza annuale",
            price_list_name="Listino PMI",
            status=CustomerAgreement.Status.ACTIVE,
            starts_on=today,
            ends_on=today + timedelta(days=10),
        )
        document = CustomerCommercialDocument.objects.create(
            customer=customer,
            name="NDA firmato",
            document_type=CustomerCommercialDocument.DocumentType.NDA,
            status=CustomerCommercialDocument.Status.ACTIVE,
            signed_on=today,
            expires_on=today + timedelta(days=20),
        )

        memory = build_customer_commercial_memory(customer)

        self.assertTrue(memory["has_memory"])
        self.assertEqual(memory["agreements"][0], agreement)
        self.assertEqual(memory["commercial_documents"][0], document)
        self.assertIn("Accordo in scadenza: Accordo consulenza annuale.", memory["alerts"])
        self.assertIn("Documento in scadenza: NDA firmato.", memory["alerts"])

    def test_readiness_warns_until_commercial_terms_are_reviewed(self):
        today = timezone.localdate()
        customer = Customer.objects.create(name="Cliente Sprint 08")
        CustomerAgreement.objects.create(
            customer=customer,
            name="Accordo da controllare",
            status=CustomerAgreement.Status.ACTIVE,
            starts_on=today,
        )
        estimate = Estimate.objects.create(
            number="B3D-TEST-08",
            customer=customer,
            subject="Preventivo con condizioni cliente",
            description="Richiesta tecnica da prezzare.",
            date=today,
        )

        memory = build_customer_commercial_memory(customer)
        readiness = build_estimate_readiness(estimate, memory)

        self.assertIn(
            "Confermare il controllo di accordi, listini e documenti commerciali del cliente.",
            readiness["warnings"],
        )

        estimate.commercial_terms_reviewed_at = timezone.now()
        estimate.commercial_terms_review_notes = "Condizioni controllate manualmente."
        readiness = build_estimate_readiness(estimate, memory)

        self.assertNotIn(
            "Confermare il controllo di accordi, listini e documenti commerciali del cliente.",
            readiness["warnings"],
        )

    def test_confirm_commercial_terms_review_saves_timestamp_and_notes(self):
        today = timezone.localdate()
        customer = Customer.objects.create(name="Cliente Conferma")
        estimate = Estimate.objects.create(
            number="B3D-TEST-08B",
            customer=customer,
            subject="Conferma condizioni",
            description="Preventivo da controllare.",
            date=today,
        )

        response = self.client.post(
            f"/preventivi/{estimate.pk}/condizioni-cliente/conferma/",
            {"notes": "Accordo e documento controllati prima del prezzo."},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], f"/preventivi/{estimate.pk}/")
        estimate.refresh_from_db()
        self.assertIsNotNone(estimate.commercial_terms_reviewed_at)
        self.assertEqual(
            estimate.commercial_terms_review_notes,
            "Accordo e documento controllati prima del prezzo.",
        )
