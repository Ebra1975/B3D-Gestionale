from django.db import models


class Material(models.Model):
    name = models.CharField("nome", max_length=255)
    material_type = models.CharField("tipo", max_length=128, blank=True)
    brand = models.CharField("marca", max_length=128, blank=True)
    color = models.CharField("colore", max_length=128, blank=True)
    cost_per_unit = models.DecimalField("costo per kg/litro", max_digits=10, decimal_places=2, default=0)
    supplier = models.CharField("fornitore", max_length=255, blank=True)
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
    hourly_cost = models.DecimalField("costo orario stimato", max_digits=10, decimal_places=2, default=0)
    estimated_power_watts = models.PositiveIntegerField("consumo stimato watt", null=True, blank=True)
    notes = models.TextField("note", blank=True)
    active = models.BooleanField("attiva", default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "stampante / strumentazione"
        verbose_name_plural = "stampanti / strumentazioni"

    def __str__(self):
        return self.name
