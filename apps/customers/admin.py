from django.contrib import admin

from .models import Customer, CustomerAgreement, CustomerCommercialDocument


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "customer_type", "contact_person", "email", "phone")
    search_fields = ("name", "contact_person", "email", "tax_code")
    list_filter = ("customer_type",)


@admin.register(CustomerAgreement)
class CustomerAgreementAdmin(admin.ModelAdmin):
    list_display = ("name", "customer", "status", "starts_on", "ends_on", "price_list_name")
    list_filter = ("status",)
    search_fields = ("name", "customer__name", "price_list_name", "general_terms", "commercial_notes")


@admin.register(CustomerCommercialDocument)
class CustomerCommercialDocumentAdmin(admin.ModelAdmin):
    list_display = ("name", "customer", "document_type", "status", "issued_on", "expires_on")
    list_filter = ("document_type", "status")
    search_fields = ("name", "customer__name", "notes")
