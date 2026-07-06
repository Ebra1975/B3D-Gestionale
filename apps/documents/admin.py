from django.contrib import admin

from .models import DocumentTemplate, GeneratedDocument


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
