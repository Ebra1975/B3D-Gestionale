from django import forms

from .models import CostItem, Estimate, EstimateConfiguration, Prototype


class EstimateForm(forms.ModelForm):
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
