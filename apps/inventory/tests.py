from decimal import Decimal

from django.test import TestCase

from .models import Material, Printer


class EconomicParameterTests(TestCase):
    def test_material_effective_cost_includes_waste_percentage(self):
        material = Material.objects.create(
            name="PETG",
            cost_per_unit=Decimal("20.00"),
            waste_percentage=Decimal("10.00"),
        )

        self.assertEqual(material.effective_cost_per_unit, Decimal("22.00"))
        self.assertIn("costo usato 22.00 EUR/kg-l", material.pricing_summary)

    def test_printer_effective_hourly_cost_includes_accessory_costs(self):
        printer = Printer.objects.create(
            name="FDM Test",
            hourly_cost=Decimal("4.00"),
            maintenance_cost_per_hour=Decimal("1.00"),
            estimated_power_watts=500,
            electricity_cost_per_kwh=Decimal("0.40"),
            failure_rate_percentage=Decimal("10.00"),
        )

        self.assertEqual(printer.energy_cost_per_hour, Decimal("0.20"))
        self.assertEqual(printer.effective_hourly_cost, Decimal("5.72"))
        self.assertIn("costo usato 5.72 EUR/h", printer.pricing_summary)
