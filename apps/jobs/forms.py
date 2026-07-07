from django import forms

from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "status",
            "start_date",
            "expected_delivery",
            "delivered_at",
            "operational_notes",
            "final_notes",
        ]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "expected_delivery": forms.DateInput(attrs={"type": "date"}),
            "delivered_at": forms.DateInput(attrs={"type": "date"}),
        }
