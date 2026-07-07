from django.contrib import admin

from .models import CostItem, Estimate, EstimateConfiguration, Prototype


class CostItemInline(admin.TabularInline):
    model = CostItem
    extra = 0


class EstimateConfigurationInline(admin.StackedInline):
    model = EstimateConfiguration
    extra = 0


@admin.register(Estimate)
class EstimateAdmin(admin.ModelAdmin):
    list_display = ("number", "customer", "subject", "date", "status", "preferred_document_profile", "commercial_terms_reviewed_at")
    search_fields = ("number", "subject", "customer__name")
    list_filter = ("status", "preferred_document_profile", "date", "commercial_terms_reviewed_at")
    inlines = [EstimateConfigurationInline]


@admin.register(EstimateConfiguration)
class EstimateConfigurationAdmin(admin.ModelAdmin):
    list_display = ("estimate", "name", "quantity", "is_selected")
    search_fields = ("estimate__number", "name")
    inlines = [CostItemInline]


@admin.register(CostItem)
class CostItemAdmin(admin.ModelAdmin):
    list_display = ("configuration", "category", "description", "quantity", "unit_cost", "total")
    list_filter = ("category", "visible_internal", "visible_consulting", "visible_supply")


admin.site.register(Prototype)
