from datetime import timedelta
from decimal import Decimal

from django.test import TestCase
from django.utils import timezone

from apps.customers.models import Customer, CustomerAgreement, CustomerCommercialDocument
from apps.estimates.models import CostItem, Estimate, EstimateConfiguration
from apps.estimates.views import build_customer_commercial_memory, build_estimate_readiness
from apps.inventory.models import Material, Printer


class EstimateNumberTests(TestCase):
    def test_estimate_number_is_generated_when_empty(self):
        today = timezone.localdate()
        customer = Customer.objects.create(name="Cliente Numerazione")
        first = Estimate.objects.create(
            customer=customer,
            subject="Primo preventivo automatico",
            description="Richiesta tecnica.",
            date=today,
        )
        second = Estimate.objects.create(
            customer=customer,
            subject="Secondo preventivo automatico",
            description="Richiesta tecnica.",
            date=today,
        )

        self.assertEqual(first.number, f"B3D-{today.year}-001")
        self.assertEqual(second.number, f"B3D-{today.year}-002")

    def test_estimate_number_uses_next_existing_sequence_for_year(self):
        today = timezone.localdate()
        customer = Customer.objects.create(name="Cliente Progressivo")
        Estimate.objects.create(
            number=f"B3D-{today.year}-009",
            customer=customer,
            subject="Preventivo gia presente",
            description="Richiesta tecnica.",
            date=today,
        )

        estimate = Estimate.objects.create(
            customer=customer,
            subject="Preventivo successivo",
            description="Richiesta tecnica.",
            date=today,
        )

        self.assertEqual(estimate.number, f"B3D-{today.year}-010")


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


class AutomaticCostTests(TestCase):
    def test_generated_material_cost_uses_effective_material_cost(self):
        today = timezone.localdate()
        customer = Customer.objects.create(name="Cliente Materiale")
        estimate = Estimate.objects.create(
            customer=customer,
            subject="Costo materiale",
            description="Richiesta tecnica.",
            date=today,
        )
        material = Material.objects.create(
            name="PETG",
            cost_per_unit=Decimal("20.00"),
            waste_percentage=Decimal("10.00"),
        )
        configuration = EstimateConfiguration.objects.create(
            estimate=estimate,
            name="Opzione PETG",
            material=material,
            quantity=2,
            material_weight_per_unit="0.500",
        )

        response = self.client.post(f"/preventivi/configurazioni/{configuration.pk}/costi/auto/materiale/")

        self.assertEqual(response.status_code, 302)
        cost_item = configuration.cost_items.get(category=CostItem.Category.MATERIAL)
        self.assertEqual(cost_item.quantity, Decimal("1.00"))
        self.assertEqual(cost_item.unit_cost, material.effective_cost_per_unit)
        self.assertEqual(cost_item.total, material.effective_cost_per_unit)
        self.assertIn("scarto/extra 10.00%", cost_item.notes)

    def test_generated_machine_cost_uses_effective_printer_cost(self):
        today = timezone.localdate()
        customer = Customer.objects.create(name="Cliente Stampante")
        estimate = Estimate.objects.create(
            customer=customer,
            subject="Costo macchina",
            description="Richiesta tecnica.",
            date=today,
        )
        printer = Printer.objects.create(
            name="FDM Test",
            hourly_cost=Decimal("4.00"),
            maintenance_cost_per_hour=Decimal("1.00"),
            estimated_power_watts=500,
            electricity_cost_per_kwh=Decimal("0.40"),
            failure_rate_percentage=Decimal("10.00"),
        )
        configuration = EstimateConfiguration.objects.create(
            estimate=estimate,
            name="Opzione FDM",
            printer=printer,
            quantity=2,
            machine_time_hours_per_unit="1.50",
        )

        response = self.client.post(f"/preventivi/configurazioni/{configuration.pk}/costi/auto/macchina/")

        self.assertEqual(response.status_code, 302)
        cost_item = configuration.cost_items.get(category=CostItem.Category.MACHINE_TIME)
        self.assertEqual(cost_item.quantity, Decimal("3.00"))
        self.assertEqual(cost_item.unit_cost, printer.effective_hourly_cost)
        self.assertEqual(cost_item.total, printer.effective_hourly_cost * 3)
        self.assertIn("rischio fallimento 10.00%", cost_item.notes)
