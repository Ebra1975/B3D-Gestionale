from django.db import models

from apps.customers.models import Customer
from apps.estimates.models import Estimate
from apps.jobs.models import Job


def original_upload_path(instance, filename):
    return f"attachments/originals/{instance.file_type}/{filename}"


def preview_upload_path(instance, filename):
    return f"attachments/previews/{instance.file_type}/{filename}"


class AttachedFile(models.Model):
    class FileType(models.TextChoices):
        THREE_MF = "3mf", "3MF"
        GCODE = "gcode", "G-code"
        STL = "stl", "STL"
        PDF = "pdf", "PDF"
        DOCX = "docx", "DOCX"
        IMAGE = "image", "Immagine"
        OTHER = "other", "Altro"

    class ProcessingStatus(models.TextChoices):
        PENDING = "pending", "Da elaborare"
        PROCESSING = "processing", "In elaborazione"
        READY = "ready", "Pronto"
        FAILED = "failed", "Errore"
        SKIPPED = "skipped", "Saltato"

    name = models.CharField("nome", max_length=255)
    file_type = models.CharField("tipo file", max_length=32, choices=FileType.choices, default=FileType.OTHER)
    customer = models.ForeignKey(Customer, verbose_name="cliente", on_delete=models.SET_NULL, null=True, blank=True, related_name="attached_files")
    estimate = models.ForeignKey(Estimate, verbose_name="preventivo", on_delete=models.SET_NULL, null=True, blank=True, related_name="attached_files")
    job = models.ForeignKey(Job, verbose_name="commessa", on_delete=models.SET_NULL, null=True, blank=True, related_name="attached_files")
    original_file = models.FileField("file originale", upload_to=original_upload_path)
    preview_file = models.FileField("preview", upload_to=preview_upload_path, blank=True)
    extracted_metadata = models.JSONField("metadati estratti", default=dict, blank=True)
    processing_status = models.CharField("stato elaborazione", max_length=32, choices=ProcessingStatus.choices, default=ProcessingStatus.PENDING)
    processing_error = models.TextField("errore elaborazione", blank=True)
    notes = models.TextField("note", blank=True)
    uploaded_at = models.DateTimeField("caricato il", auto_now_add=True)
    updated_at = models.DateTimeField("aggiornato il", auto_now=True)

    class Meta:
        ordering = ["-uploaded_at"]
        verbose_name = "file allegato"
        verbose_name_plural = "file allegati"

    def __str__(self):
        return self.name
