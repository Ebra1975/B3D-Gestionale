from django.contrib import admin

from .models import DocumentProfile, DocumentTemplate, GeneratedDocument


@admin.register(DocumentProfile)
class DocumentProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "company_name", "email", "active", "updated_at")
    search_fields = ("name", "company_name", "email", "tax_code")
    list_filter = ("active",)


@admin.register(DocumentTemplate)
class DocumentTemplateAdmin(admin.ModelAdmin):
    list_display = ("name", "document_type", "template_version", "active", "uploaded_at")
    search_fields = ("name", "profile")
    list_filter = ("document_type", "active")


@admin.register(GeneratedDocument)
class GeneratedDocumentAdmin(admin.ModelAdmin):
    list_display = ("estimate", "document_type", "version", "generated_at")
    search_fields = ("estimate__number",)
    list_filter = ("document_type",)
