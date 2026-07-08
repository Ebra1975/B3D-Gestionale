from django.db import models

from apps.estimates.models import Estimate


def template_upload_path(instance, filename):
    return f"templates/{instance.document_type}/{filename}"


def generated_document_path(instance, filename):
    return f"generated/{instance.estimate.number}/{instance.document_type}/{filename}"


def logo_upload_path(instance, filename):
    return f"document_data/{filename}"


class DocumentProfile(models.Model):
    name = models.CharField("nome profilo", max_length=255, default="B3D Lab")
    company_name = models.CharField("nome azienda", max_length=255, default="B3D Lab")
    subtitle = models.CharField(
        "sottotitolo",
        max_length=255,
        default="Consulenza tecnica e manifattura additiva",
    )
    address = models.TextField("indirizzo", blank=True)
    email = models.EmailField("email", blank=True)
    phone = models.CharField("telefono", max_length=64, blank=True)
    website = models.CharField("sito web", max_length=255, blank=True)
    tax_code = models.CharField("codice fiscale / partita IVA", max_length=64, blank=True)
    logo = models.FileField("logo", upload_to=logo_upload_path, blank=True)
    standard_consulting_terms = models.TextField(
        "condizioni standard consulenza",
        blank=True,
        default="Validita, tempi e modalita operative da confermare in base all'accettazione del cliente.",
    )
    fiscal_note = models.TextField(
        "nota fiscale",
        default="Dicitura commerciale e fiscale da validare con commercialista.",
    )
    internal_footer_note = models.TextField(
        "nota interna",
        blank=True,
        default="Documento interno: non inviare al cliente.",
    )
    active = models.BooleanField("attivo", default=True)
    updated_at = models.DateTimeField("aggiornato il", auto_now=True)

    class Meta:
        ordering = ["-active", "name"]
        verbose_name = "dati documento"
        verbose_name_plural = "dati documento"

    def __str__(self):
        return self.name

    @classmethod
    def get_active(cls):
        profile = cls.objects.filter(active=True).order_by("id").first()
        if profile:
            return profile
        return cls.objects.create()


class DocumentTemplate(models.Model):
    class DocumentType(models.TextChoices):
        INTERNAL_ESTIMATE = "internal_estimate", "Preventivo interno"
        CONSULTING_ESTIMATE = "consulting_estimate", "Preventivo consulenza"
        SUPPLY_ESTIMATE = "supply_estimate", "Preventivo fornitura/artigiano"
        DELIVERY = "delivery", "Documento di consegna"
        TECHNICAL_REPORT = "technical_report", "Relazione tecnica"
        FISCAL_FUTURE = "fiscal_future", "Documento fiscale futuro"

    name = models.CharField("nome", max_length=255)
    document_type = models.CharField("tipo documento", max_length=64, choices=DocumentType.choices)
    profile = models.CharField("profilo", max_length=64, blank=True)
    template_file = models.FileField("file template DOCX", upload_to=template_upload_path)
    template_version = models.CharField("versione template", max_length=32, default="v1")
    active = models.BooleanField("attivo", default=True)
    uploaded_at = models.DateTimeField("caricato il", auto_now_add=True)
    notes = models.TextField("note", blank=True)

    class Meta:
        ordering = ["document_type", "name"]
        verbose_name = "template documento"
        verbose_name_plural = "template documenti"

    def __str__(self):
        return f"{self.name} ({self.template_version})"


class GeneratedDocument(models.Model):
    class DocumentType(models.TextChoices):
        INTERNAL = "internal", "Interno dettagliato"
        CONSULTING = "consulting", "Consulenza"
        SUPPLY = "supply", "Fornitura / artigiano"
        DELIVERY = "delivery", "Consegna"
        TECHNICAL_REPORT = "technical_report", "Relazione tecnica"

    estimate = models.ForeignKey(Estimate, verbose_name="preventivo", on_delete=models.CASCADE, related_name="generated_documents")
    template = models.ForeignKey(DocumentTemplate, verbose_name="template", on_delete=models.PROTECT, null=True, blank=True)
    document_type = models.CharField("tipo documento", max_length=64, choices=DocumentType.choices)
    version = models.PositiveIntegerField("versione", default=1)
    docx_file = models.FileField("file DOCX", upload_to=generated_document_path, blank=True)
    pdf_file = models.FileField("file PDF", upload_to=generated_document_path, blank=True)
    generated_at = models.DateTimeField("generato il", auto_now_add=True)
    notes = models.TextField("note", blank=True)

    class Meta:
        ordering = ["-generated_at"]
        verbose_name = "documento generato"
        verbose_name_plural = "documenti generati"
        unique_together = ("estimate", "document_type", "version")

    def __str__(self):
        return f"{self.estimate.number} - {self.get_document_type_display()} v{self.version}"
