from django.db import models


class AutomationLog(models.Model):
    class Status(models.TextChoices):
        STARTED = "started", "Avviata"
        SUCCESS = "success", "Completata"
        FAILED = "failed", "Errore"

    name = models.CharField("nome", max_length=255)
    status = models.CharField("stato", max_length=32, choices=Status.choices)
    message = models.TextField("messaggio", blank=True)
    payload = models.JSONField("dati", default=dict, blank=True)
    started_at = models.DateTimeField("avviata il", auto_now_add=True)
    finished_at = models.DateTimeField("terminata il", null=True, blank=True)

    class Meta:
        ordering = ["-started_at"]
        verbose_name = "log automazione"
        verbose_name_plural = "log automazioni"

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"
