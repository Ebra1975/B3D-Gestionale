from decimal import Decimal

from django.db import models
from django.db.models import Sum

from apps.customers.models import Customer
from apps.inventory.models import Material, Printer


class Estimate(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Bozza"
        SENT = "sent", "Inviato"
        REVISION = "revision", "Da rivedere"
        ACCEPTED = "accepted", "Accettato"
        REJECTED = "rejected", "Rifiutato"
        EXPIRED = "expired", "Scaduto"
        CANCELLED = "cancelled", "Annullato"

    class DocumentProfile(models.TextChoices):
        INTERNAL = "internal", "Interno dettagliato"
        CONSULTING = "consulting", "Consulenza"
        SUPPLY = "supply", "Fornitura / artigiano"

    number = models.CharField("numero", max_length=64, unique=True)
    customer = models.ForeignKey(Customer, verbose_name="cliente", on_delete=models.PROTECT, related_name="estimates")
    subject = models.CharField("oggetto", max_length=255)
    description = models.TextField("descrizione", blank=True)
    date = models.DateField("data")
    valid_until = models.DateField("valido fino al", null=True, blank=True)
    status = models.CharField("stato", max_length=32, choices=Status.choices, default=Status.DRAFT)
    quantity = models.PositiveIntegerField("quantita", default=1)
    preferred_document_profile = models.CharField(
        "profilo documento preferito",
        max_length=32,
        choices=DocumentProfile.choices,
        default=DocumentProfile.CONSULTING,
    )
    commercial_terms_reviewed_at = models.DateTimeField("condizioni cliente controllate il", null=True, blank=True)
    commercial_terms_review_notes = models.TextField("note revisione condizioni cliente", blank=True)
    general_terms = models.TextField("condizioni generali", blank=True)
    internal_notes = models.TextField("note interne", blank=True)
    created_at = models.DateTimeField("creato il", auto_now_add=True)
    updated_at = models.DateTimeField("aggiornato il", auto_now=True)

    class Meta:
        ordering = ["-date", "-id"]
        verbose_name = "preventivo"
        verbose_name_plural = "preventivi"

    def __str__(self):
        return f"{self.number} - {self.subject}"


class EstimateConfiguration(models.Model):
    estimate = models.ForeignKey(Estimate, verbose_name="preventivo", on_delete=models.CASCADE, related_name="configurations")
    name = models.CharField("nome", max_length=255)
    description = models.TextField("descrizione", blank=True)
    material = models.ForeignKey(Material, verbose_name="materiale", on_delete=models.SET_NULL, null=True, blank=True)
    printer = models.ForeignKey(Printer, verbose_name="stampante / strumentazione", on_delete=models.SET_NULL, null=True, blank=True)
    process = models.CharField("processo", max_length=255, blank=True)
    treatment = models.CharField("trattamento", max_length=255, blank=True)
    expected_duration = models.CharField("durata attesa", max_length=255, blank=True)
    operating_mode = models.TextField("modalita operativa", blank=True)
    quantity = models.PositiveIntegerField("quantita", default=1)
    material_weight_per_unit = models.DecimalField("peso materiale per unita", max_digits=10, decimal_places=3, null=True, blank=True)
    machine_time_hours_per_unit = models.DecimalField("ore macchina per unita", max_digits=10, decimal_places=2, null=True, blank=True)
    public_notes = models.TextField("note pubbliche", blank=True)
    internal_notes = models.TextField("note interne", blank=True)
    is_selected = models.BooleanField("configurazione scelta", default=False)

    class Meta:
        ordering = ["estimate", "id"]
        verbose_name = "configurazione"
        verbose_name_plural = "configurazioni"

    def __str__(self):
        return f"{self.estimate.number} - {self.name}"

    @property
    def total(self):
        value = self.cost_items.aggregate(total=Sum("total"))["total"]
        return value or Decimal("0.00")

    @property
    def base_cost(self):
        value = self.cost_items.exclude(category=CostItem.Category.MARGIN).aggregate(total=Sum("total"))["total"]
        return value or Decimal("0.00")

    @property
    def margin_total(self):
        value = self.cost_items.filter(category=CostItem.Category.MARGIN).aggregate(total=Sum("total"))["total"]
        return value or Decimal("0.00")

    @property
    def margin_percentage(self):
        if not self.base_cost:
            return Decimal("0.00")
        return self.margin_total / self.base_cost * Decimal("100")

    @property
    def unit_price(self):
        if not self.quantity:
            return Decimal("0.00")
        return self.total / self.quantity


class CostItem(models.Model):
    class Category(models.TextChoices):
        MATERIAL = "material", "Materiale"
        MACHINE_TIME = "machine_time", "Tempo macchina"
        ELECTRICITY = "electricity", "Elettricita"
        DESIGN = "design", "Progettazione"
        SETUP = "setup", "Setup"
        LABOR = "labor", "Manodopera"
        TRAVEL = "travel", "Trasferta"
        POST_PROCESSING = "post_processing", "Post-processing"
        TREATMENT = "treatment", "Trattamento"
        MARGIN = "margin", "Margine"
        OTHER = "other", "Altro"

    configuration = models.ForeignKey(EstimateConfiguration, verbose_name="configurazione", on_delete=models.CASCADE, related_name="cost_items")
    category = models.CharField("categoria", max_length=32, choices=Category.choices)
    description = models.CharField("descrizione", max_length=255)
    quantity = models.DecimalField("quantita", max_digits=10, decimal_places=2, default=1)
    unit = models.CharField("unita", max_length=32, blank=True)
    unit_cost = models.DecimalField("costo unitario", max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField("totale", max_digits=10, decimal_places=2, default=0)
    visible_internal = models.BooleanField("visibile interno", default=True)
    visible_consulting = models.BooleanField("visibile consulenza", default=False)
    visible_supply = models.BooleanField("visibile fornitura/artigiano", default=True)
    notes = models.TextField("note", blank=True)

    class Meta:
        ordering = ["configuration", "id"]
        verbose_name = "voce di costo"
        verbose_name_plural = "voci di costo"

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.unit_cost
        super().save(*args, **kwargs)


class Prototype(models.Model):
    class Status(models.TextChoices):
        NOT_PLANNED = "not_planned", "Non previsto"
        PROPOSED = "proposed", "Proposto"
        APPROVED = "approved", "Approvato"
        PRODUCED = "produced", "Realizzato"
        VALIDATED = "validated", "Validato"
        NEEDS_CHANGES = "needs_changes", "Da modificare"

    estimate = models.OneToOneField(Estimate, verbose_name="preventivo", on_delete=models.CASCADE, related_name="prototype")
    description = models.TextField("descrizione", blank=True)
    material = models.ForeignKey(Material, verbose_name="materiale", on_delete=models.SET_NULL, null=True, blank=True)
    internal_cost = models.DecimalField("costo interno", max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField("compenso/prezzo", max_digits=10, decimal_places=2, default=0)
    status = models.CharField("stato", max_length=32, choices=Status.choices, default=Status.NOT_PLANNED)
    notes = models.TextField("note", blank=True)
    validated_at = models.DateField("data validazione", null=True, blank=True)

    class Meta:
        verbose_name = "prototipo"
        verbose_name_plural = "prototipi"

    def __str__(self):
        return f"Prototipo {self.estimate.number}"
