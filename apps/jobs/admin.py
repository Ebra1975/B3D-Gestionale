from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("number", "customer", "status", "start_date", "expected_delivery", "delivered_at")
    search_fields = ("number", "customer__name", "estimate__number")
    list_filter = ("status",)
