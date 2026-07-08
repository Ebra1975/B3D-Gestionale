from django import forms

from .models import CostItem, Estimate, EstimateConfiguration, Prototype


class EstimateForm(forms.ModelForm):
    number = forms.CharField(
        label="Numero",
        required=False,
        help_text="Lascia vuoto per assegnare automaticamente il prossimo numero disponibile.",
    )

    class Meta:
        model = Estimate
        fields = [
            "number",
            "customer",
            "subject",
            "description",
            "date",
            "valid_until",
            "status",
            "quantity",
            "preferred_document_profile",
            "general_terms",
            "internal_notes",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "valid_until": forms.DateInput(attrs={"type": "date"}),
        }


class EstimateConfigurationForm(forms.ModelForm):
    class Meta:
        model = EstimateConfiguration
        fields = [
            "name",
            "description",
            "material",
            "printer",
            "process",
            "treatment",
            "expected_duration",
            "operating_mode",
            "quantity",
            "material_weight_per_unit",
            "machine_time_hours_per_unit",
            "public_notes",
            "internal_notes",
            "is_selected",
        ]


class CostItemForm(forms.ModelForm):
    class Meta:
        model = CostItem
        fields = [
            "category",
            "description",
            "quantity",
            "unit",
            "unit_cost",
            "visible_internal",
            "visible_consulting",
            "visible_supply",
            "notes",
        ]


class PricingRuleForm(forms.Form):
    margin_percentage = forms.DecimalField(
        label="Margine percentuale",
        min_value=0,
        max_digits=5,
        decimal_places=2,
        initial=30,
    )
    rounding_step = forms.DecimalField(
        label="Arrotonda al multiplo di",
        min_value=0,
        max_digits=8,
        decimal_places=2,
        initial=5,
        help_text="Usare 0 per non arrotondare.",
    )


class CommercialTermsReviewForm(forms.Form):
    notes = forms.CharField(
        label="Note interne sul controllo",
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "placeholder": "Esempio: controllato accordo annuale e NDA; prezzo confermato manualmente.",
            }
        ),
    )


class TechnicalFileImportForm(forms.Form):
    technical_file = forms.FileField(
        label="File G-code o 3MF",
        help_text="Usa il file esportato dallo slicer per importare peso materiale, tempo macchina e piatti rilevati.",
    )

    def clean_technical_file(self):
        technical_file = self.cleaned_data["technical_file"]
        allowed_extensions = (".gcode", ".gco", ".3mf")
        if not technical_file.name.lower().endswith(allowed_extensions):
            raise forms.ValidationError("Carica un file G-code, GCO o 3MF.")
        return technical_file


class PrototypeForm(forms.ModelForm):
    class Meta:
        model = Prototype
        fields = [
            "description",
            "material",
            "internal_cost",
            "price",
            "status",
            "notes",
            "validated_at",
        ]
        widgets = {
            "validated_at": forms.DateInput(attrs={"type": "date"}),
        }
