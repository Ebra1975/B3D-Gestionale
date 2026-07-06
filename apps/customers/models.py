from django.db import models


class Customer(models.Model):
    class CustomerType(models.TextChoices):
        PERSON = "person", "Persona"
        COMPANY = "company", "Azienda"
        NON_PROFIT = "non_profit", "Ente / cooperativa"

    name = models.CharField("nome", max_length=255)
    customer_type = models.CharField("tipo cliente", max_length=32, choices=CustomerType.choices, default=CustomerType.COMPANY)
    contact_person = models.CharField("referente", max_length=255, blank=True)
    email = models.EmailField("email", blank=True)
    phone = models.CharField("telefono", max_length=64, blank=True)
    address = models.TextField("indirizzo", blank=True)
    tax_code = models.CharField("codice fiscale / partita IVA", max_length=64, blank=True)
    notes = models.TextField("note", blank=True)
    created_at = models.DateTimeField("creato il", auto_now_add=True)
    updated_at = models.DateTimeField("aggiornato il", auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "cliente"
        verbose_name_plural = "clienti"

    def __str__(self):
        return self.name
