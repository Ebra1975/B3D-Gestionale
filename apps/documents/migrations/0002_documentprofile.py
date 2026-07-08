# Generated for Sprint 09 on 2026-07-08

import apps.documents.models
from django.db import migrations, models


def create_default_document_profile(apps, schema_editor):
    DocumentProfile = apps.get_model("documents", "DocumentProfile")
    DocumentProfile.objects.get_or_create(
        name="B3D Lab",
        defaults={
            "company_name": "B3D Lab",
            "subtitle": "Consulenza tecnica e manifattura additiva",
            "standard_consulting_terms": (
                "Validita, tempi e modalita operative da confermare in base "
                "all'accettazione del cliente."
            ),
            "fiscal_note": "Dicitura commerciale e fiscale da validare con commercialista.",
            "internal_footer_note": "Documento interno: non inviare al cliente.",
            "active": True,
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DocumentProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(default="B3D Lab", max_length=255, verbose_name="nome profilo")),
                ("company_name", models.CharField(default="B3D Lab", max_length=255, verbose_name="nome azienda")),
                (
                    "subtitle",
                    models.CharField(
                        default="Consulenza tecnica e manifattura additiva",
                        max_length=255,
                        verbose_name="sottotitolo",
                    ),
                ),
                ("address", models.TextField(blank=True, verbose_name="indirizzo")),
                ("email", models.EmailField(blank=True, max_length=254, verbose_name="email")),
                ("phone", models.CharField(blank=True, max_length=64, verbose_name="telefono")),
                ("website", models.CharField(blank=True, max_length=255, verbose_name="sito web")),
                ("tax_code", models.CharField(blank=True, max_length=64, verbose_name="codice fiscale / partita IVA")),
                ("logo", models.FileField(blank=True, upload_to=apps.documents.models.logo_upload_path, verbose_name="logo")),
                (
                    "standard_consulting_terms",
                    models.TextField(
                        blank=True,
                        default="Validita, tempi e modalita operative da confermare in base all'accettazione del cliente.",
                        verbose_name="condizioni standard consulenza",
                    ),
                ),
                (
                    "fiscal_note",
                    models.TextField(
                        default="Dicitura commerciale e fiscale da validare con commercialista.",
                        verbose_name="nota fiscale",
                    ),
                ),
                (
                    "internal_footer_note",
                    models.TextField(
                        blank=True,
                        default="Documento interno: non inviare al cliente.",
                        verbose_name="nota interna",
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="attivo")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="aggiornato il")),
            ],
            options={
                "verbose_name": "dati documento",
                "verbose_name_plural": "dati documento",
                "ordering": ["-active", "name"],
            },
        ),
        migrations.RunPython(create_default_document_profile, migrations.RunPython.noop),
    ]
