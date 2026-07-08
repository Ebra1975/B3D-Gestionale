from django import forms

from .models import DocumentProfile, DocumentTemplate
from .services import validate_docx_template_file


class DocumentProfileForm(forms.ModelForm):
    class Meta:
        model = DocumentProfile
        fields = [
            "name",
            "company_name",
            "subtitle",
            "address",
            "email",
            "phone",
            "website",
            "tax_code",
            "logo",
            "standard_consulting_terms",
            "fiscal_note",
            "internal_footer_note",
        ]


class DocumentTemplateForm(forms.ModelForm):
    class Meta:
        model = DocumentTemplate
        fields = [
            "name",
            "document_type",
            "profile",
            "template_file",
            "template_version",
            "active",
            "notes",
        ]
        help_texts = {
            "profile": "Campo libero utile per distinguere consulenza, interno o varianti future.",
            "template_file": "Caricare solo file Word in formato .docx con segnaposto compatibili.",
            "active": "Il template attivo sara usato per le prossime generazioni di questo tipo documento.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._template_file_changed = False
        if self.instance and self.instance.pk:
            self.fields["template_file"].required = False

    def clean_template_file(self):
        template_file = self.cleaned_data.get("template_file")
        if not template_file and self.instance and self.instance.pk:
            return self.instance.template_file
        if not template_file:
            raise forms.ValidationError("Caricare un file template DOCX.")
        if not template_file.name.lower().endswith(".docx"):
            raise forms.ValidationError("Il template deve essere un file .docx.")
        self._template_file_changed = True
        return template_file

    def clean(self):
        cleaned_data = super().clean()
        template_file = cleaned_data.get("template_file")
        document_type = cleaned_data.get("document_type")
        if self._template_file_changed and template_file and document_type:
            errors = validate_docx_template_file(template_file, document_type)
            if errors:
                self.add_error("template_file", forms.ValidationError(errors))
        return cleaned_data
