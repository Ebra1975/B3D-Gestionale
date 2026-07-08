from django.urls import path

from . import views


app_name = "documents"

urlpatterns = [
    path("", views.document_list, name="list"),
    path("dati-documento/modifica/", views.document_profile_update, name="profile_update"),
    path("template/nuovo/", views.document_template_create, name="template_create"),
    path("template/<int:pk>/modifica/", views.document_template_update, name="template_update"),
    path("template/<int:pk>/attiva/", views.document_template_activate, name="template_activate"),
    path("template/<int:pk>/disattiva/", views.document_template_deactivate, name="template_deactivate"),
]
