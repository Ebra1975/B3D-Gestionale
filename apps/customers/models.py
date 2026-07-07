from django.db import models


def commercial_document_upload_path(instance, filename):
    return f"customers/{instance.customer_id}/commercial_documents/{filename}"


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


class CustomerAgreement(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Bozza"
        ACTIVE = "active", "Attivo"
        EXPIRED = "expired", "Scaduto"
        PAUSED = "paused", "Sospeso"
        RENEWED = "renewed", "Rinnovato"
        CLOSED = "closed", "Chiuso"

    customer = models.ForeignKey(Customer, verbose_name="cliente", on_delete=models.CASCADE, related_name="agreements")
    name = models.CharField("nome accordo", max_length=255)
    price_list_name = models.CharField("listino collegato", max_length=255, blank=True)
    starts_on = models.DateField("data inizio", null=True, blank=True)
    ends_on = models.DateField("data fine", null=True, blank=True)
    status = models.CharField("stato", max_length=32, choices=Status.choices, default=Status.DRAFT)
    general_terms = models.TextField("condizioni generali", blank=True)
    commercial_notes = models.TextField("note commerciali", blank=True)
    created_at = models.DateTimeField("creato il", auto_now_add=True)
    updated_at = models.DateTimeField("aggiornato il", auto_now=True)

    class Meta:
        ordering = ["customer", "-starts_on", "name"]
        verbose_name = "accordo cliente"
        verbose_name_plural = "accordi cliente"

    def __str__(self):
        return f"{self.customer} - {self.name}"


class CustomerCommercialDocument(models.Model):
    class DocumentType(models.TextChoices):
        NDA = "nda", "NDA"
        COMMERCIAL_AGREEMENT = "commercial_agreement", "Accordo commerciale"
        FRAME_AGREEMENT = "frame_agreement", "Accordo quadro"
        SPECIAL_TERMS = "special_terms", "Condizioni particolari"
        SIGNED_PRICE_LIST = "signed_price_list", "Listino firmato"
        ENGAGEMENT_LETTER = "engagement_letter", "Lettera di incarico"
        OTHER = "other", "Altro"

    class Status(models.TextChoices):
        DRAFT = "draft", "Bozza"
        SENT = "sent", "Inviato"
        SIGNED = "signed", "Firmato"
        ACTIVE = "active", "Attivo"
        EXPIRED = "expired", "Scaduto"
        REPLACED = "replaced", "Sostituito"
        ARCHIVED = "archived", "Archiviato"

    customer = models.ForeignKey(Customer, verbose_name="cliente", on_delete=models.CASCADE, related_name="commercial_documents")
    name = models.CharField("nome documento", max_length=255)
    document_type = models.CharField("tipo documento", max_length=64, choices=DocumentType.choices)
    issued_on = models.DateField("data emissione", null=True, blank=True)
    signed_on = models.DateField("data firma", null=True, blank=True)
    expires_on = models.DateField("data scadenza", null=True, blank=True)
    status = models.CharField("stato", max_length=32, choices=Status.choices, default=Status.DRAFT)
    file = models.FileField("file allegato", upload_to=commercial_document_upload_path, blank=True)
    notes = models.TextField("note", blank=True)
    created_at = models.DateTimeField("creato il", auto_now_add=True)
    updated_at = models.DateTimeField("aggiornato il", auto_now=True)

    class Meta:
        ordering = ["customer", "-issued_on", "name"]
        verbose_name = "documento commerciale cliente"
        verbose_name_plural = "documenti commerciali cliente"

    def __str__(self):
        return f"{self.customer} - {self.name}"
