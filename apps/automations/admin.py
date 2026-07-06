from django.contrib import admin

from .models import AutomationLog


@admin.register(AutomationLog)
class AutomationLogAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "started_at", "finished_at")
    search_fields = ("name", "message")
    list_filter = ("status",)
