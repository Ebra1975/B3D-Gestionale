from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "name",
            "customer_type",
            "contact_person",
            "email",
            "phone",
            "address",
            "tax_code",
            "notes",
        ]
