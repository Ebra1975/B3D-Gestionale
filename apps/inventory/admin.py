from django.contrib import admin

from .models import Material, Printer


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "material_type", "brand", "color", "cost_per_unit", "waste_percentage", "effective_cost_per_unit", "available")
    search_fields = ("name", "brand", "color", "supplier")
    list_filter = ("material_type", "available")


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "ownership", "enclosed_chamber", "hourly_cost", "effective_hourly_cost", "active")
    search_fields = ("name", "model")
    list_filter = ("ownership", "enclosed_chamber", "active")
