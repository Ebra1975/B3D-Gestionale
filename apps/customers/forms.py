from django import forms

from .models import Customer, CustomerAgreement, CustomerCommercialDocument


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


class CustomerAgreementForm(forms.ModelForm):
    class Meta:
        model = CustomerAgreement
        fields = [
            "name",
            "price_list_name",
            "starts_on",
            "ends_on",
            "status",
            "general_terms",
            "commercial_notes",
        ]
        widgets = {
            "starts_on": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "ends_on": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }


class CustomerCommercialDocumentForm(forms.ModelForm):
    class Meta:
        model = CustomerCommercialDocument
        fields = [
            "name",
            "document_type",
            "issued_on",
            "signed_on",
            "expires_on",
            "status",
            "file",
            "notes",
        ]
        widgets = {
            "issued_on": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "signed_on": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "expires_on": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }
