from django.urls import path

from . import views


app_name = "inventory"

urlpatterns = [
    path("materiali/", views.material_list, name="materials"),
    path("materiali/nuovo/", views.material_create, name="material_create"),
    path("materiali/<int:pk>/modifica/", views.material_update, name="material_update"),
    path("stampanti/", views.printer_list, name="printers"),
    path("stampanti/nuova/", views.printer_create, name="printer_create"),
    path("stampanti/<int:pk>/modifica/", views.printer_update, name="printer_update"),
]
