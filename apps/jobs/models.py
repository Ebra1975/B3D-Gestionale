from django.db import models

from apps.customers.models import Customer
from apps.estimates.models import Estimate, EstimateConfiguration


class Job(models.Model):
    class Status(models.TextChoices):
        TODO = "todo", "Da fare"
        DESIGN = "design", "In progettazione"
        PRINTING = "printing", "In stampa"
        POST_PROCESSING = "post_processing", "In post-processing"
        READY = "ready", "Pronto"
        DELIVERED = "delivered", "Consegnato"
        PAUSED = "paused", "Sospeso"
        CANCELLED = "cancelled", "Annullato"

    number = models.CharField("numero commessa", max_length=64, unique=True)
    estimate = models.ForeignKey(Estimate, verbose_name="preventivo", on_delete=models.PROTECT, related_name="jobs")
    customer = models.ForeignKey(Customer, verbose_name="cliente", on_delete=models.PROTECT, related_name="jobs")
    selected_configuration = models.ForeignKey(
        EstimateConfiguration,
        verbose_name="configurazione scelta",
        on_delete=models.PROTECT,
        related_name="jobs",
    )
    status = models.CharField("stato", max_length=32, choices=Status.choices, default=Status.TODO)
    start_date = models.DateField("data avvio", null=True, blank=True)
    expected_delivery = models.DateField("consegna prevista", null=True, blank=True)
    delivered_at = models.DateField("data consegna", null=True, blank=True)
    operational_notes = models.TextField("note operative", blank=True)
    final_notes = models.TextField("note finali", blank=True)
    created_at = models.DateTimeField("creato il", auto_now_add=True)
    updated_at = models.DateTimeField("aggiornato il", auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "commessa"
        verbose_name_plural = "commesse"

    def __str__(self):
        return f"{self.number} - {self.customer}"
