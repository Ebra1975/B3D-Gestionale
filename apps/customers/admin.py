from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "customer_type", "contact_person", "email", "phone")
    search_fields = ("name", "contact_person", "email", "tax_code")
    list_filter = ("customer_type",)
