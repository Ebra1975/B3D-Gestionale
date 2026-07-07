from django.urls import path

from . import views


app_name = "customers"

urlpatterns = [
    path("", views.customer_list, name="list"),
    path("nuovo/", views.customer_create, name="create"),
    path("<int:pk>/", views.customer_detail, name="detail"),
    path("<int:pk>/modifica/", views.customer_update, name="update"),
    path("<int:customer_pk>/accordi/nuovo/", views.agreement_create, name="agreement_create"),
    path("accordi/<int:pk>/modifica/", views.agreement_update, name="agreement_update"),
    path("<int:customer_pk>/documenti-commerciali/nuovo/", views.commercial_document_create, name="commercial_document_create"),
    path("documenti-commerciali/<int:pk>/modifica/", views.commercial_document_update, name="commercial_document_update"),
]
