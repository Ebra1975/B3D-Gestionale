from django import forms

from .models import Material, Printer


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = [
            "name",
            "material_type",
            "brand",
            "color",
            "cost_per_unit",
            "supplier",
            "technical_notes",
            "uv_resistance",
            "temperature_notes",
            "available",
        ]


class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = [
            "name",
            "model",
            "ownership",
            "build_volume",
            "enclosed_chamber",
            "supported_materials",
            "hourly_cost",
            "estimated_power_watts",
            "notes",
            "active",
        ]
