from django.contrib import admin

from .models import AttachedFile


@admin.register(AttachedFile)
class AttachedFileAdmin(admin.ModelAdmin):
    list_display = ("name", "file_type", "customer", "estimate", "job", "processing_status", "uploaded_at")
    search_fields = ("name", "customer__name", "estimate__number", "job__number")
    list_filter = ("file_type", "processing_status")
