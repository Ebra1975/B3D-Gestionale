from django.core.validators import RegexValidator
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("estimates", "0002_estimate_commercial_terms_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="estimate",
            name="number",
            field=models.CharField(
                blank=True,
                max_length=64,
                unique=True,
                validators=[
                    RegexValidator(
                        regex="^B3D-\\d{4}-\\d{3,}$",
                        message="Usa il formato B3D-ANNO-NNN, per esempio B3D-2026-001.",
                    )
                ],
                verbose_name="numero",
            ),
        ),
    ]
