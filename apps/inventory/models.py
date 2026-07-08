from decimal import Decimal

from django.db import models


def money(value):
    return value.quantize(Decimal("0.01"))


class Material(models.Model):
    name = models.CharField("nome", max_length=255)
    material_type = models.CharField("tipo", max_length=128, blank=True)
    brand = models.CharField("marca", max_length=128, blank=True)
    color = models.CharField("colore", max_length=128, blank=True)
    cost_per_unit = models.DecimalField(
        "costo base per kg/litro",
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text="Costo di acquisto o riferimento interno prima di scarti e maggiorazioni.",
    )
    waste_percentage = models.DecimalField(
        "scarto / extra materiale %",
        max_digits=5,
        decimal_places=2,
        default=0,
        help_text="Percentuale prudenziale per supporti, prove, sfridi o materiale non recuperabile.",
    )
    supplier = models.CharField("fornitore", max_length=255, blank=True)
    pricing_notes = models.TextField("note costo materiale", blank=True)
    technical_notes = models.TextField("note tecniche", blank=True)
    uv_resistance = models.CharField("resistenza UV", max_length=255, blank=True)
    temperature_notes = models.CharField("temperatura", max_length=255, blank=True)
    available = models.BooleanField("disponibile", default=True)

    class Meta:
        ordering = ["name", "brand", "color"]
        verbose_name = "materiale"
        verbose_name_plural = "materiali"

    def __str__(self):
        parts = [self.name, self.brand, self.color]
        return " - ".join(part for part in parts if part)

    @property
    def effective_cost_per_unit(self):
        multiplier = Decimal("1.00") + (self.waste_percentage or Decimal("0.00")) / Decimal("100")
        return money(self.cost_per_unit * multiplier)

    @property
    def pricing_summary(self):
        return (
            f"Costo base {self.cost_per_unit:.2f} EUR/kg-l"
            f", scarto/extra {self.waste_percentage:.2f}%"
            f", costo usato {self.effective_cost_per_unit:.2f} EUR/kg-l."
        )


class Printer(models.Model):
    class Ownership(models.TextChoices):
        OWNED = "owned", "Propria"
        CUSTOMER = "customer", "Cliente"
        LOAN = "loan", "Comodato"
        OTHER = "other", "Altro"

    name = models.CharField("nome", max_length=255)
    model = models.CharField("modello", max_length=255, blank=True)
    ownership = models.CharField("proprieta", max_length=32, choices=Ownership.choices, default=Ownership.OWNED)
    build_volume = models.CharField("volume di stampa", max_length=128, blank=True)
    enclosed_chamber = models.BooleanField("camera chiusa", default=False)
    supported_materials = models.TextField("materiali supportati", blank=True)
    hourly_cost = models.DecimalField(
        "costo orario base",
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text="Quota oraria principale: ammortamento, noleggio o stima interna gia nota.",
    )
    maintenance_cost_per_hour = models.DecimalField(
        "manutenzione per ora",
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text="Quota prudenziale per ricambi, ugelli, usura e manutenzione ordinaria.",
    )
    estimated_power_watts = models.PositiveIntegerField("consumo stimato watt", null=True, blank=True)
    electricity_cost_per_kwh = models.DecimalField(
        "costo energia kWh",
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text="Costo energia usato per stimare la quota elettrica oraria.",
    )
    failure_rate_percentage = models.DecimalField(
        "rischio fallimento %",
        max_digits=5,
        decimal_places=2,
        default=0,
        help_text="Percentuale prudenziale per prove fallite, riavvii o rilavorazioni.",
    )
    economic_notes = models.TextField("note economiche", blank=True)
    notes = models.TextField("note", blank=True)
    active = models.BooleanField("attiva", default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "stampante / strumentazione"
        verbose_name_plural = "stampanti / strumentazioni"

    def __str__(self):
        return self.name

    @property
    def energy_cost_per_hour(self):
        if not self.estimated_power_watts or not self.electricity_cost_per_kwh:
            return Decimal("0.00")
        return money(Decimal(self.estimated_power_watts) / Decimal("1000") * self.electricity_cost_per_kwh)

    @property
    def effective_hourly_cost(self):
        subtotal = self.hourly_cost + self.maintenance_cost_per_hour + self.energy_cost_per_hour
        multiplier = Decimal("1.00") + (self.failure_rate_percentage or Decimal("0.00")) / Decimal("100")
        return money(subtotal * multiplier)

    @property
    def pricing_summary(self):
        return (
            f"Costo base {self.hourly_cost:.2f} EUR/h"
            f", manutenzione {self.maintenance_cost_per_hour:.2f} EUR/h"
            f", energia {self.energy_cost_per_hour:.2f} EUR/h"
            f", rischio fallimento {self.failure_rate_percentage:.2f}%"
            f", costo usato {self.effective_hourly_cost:.2f} EUR/h."
        )
