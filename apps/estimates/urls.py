from django.urls import path

from . import views


app_name = "estimates"

urlpatterns = [
    path("", views.estimate_list, name="list"),
    path("nuovo/", views.estimate_create, name="create"),
    path("<int:pk>/", views.estimate_detail, name="detail"),
    path("<int:pk>/modifica/", views.estimate_update, name="update"),
    path("<int:pk>/documenti/consulenza/genera/", views.generate_consulting_document, name="generate_consulting_document"),
    path("<int:pk>/documenti/interno/genera/", views.generate_internal_document, name="generate_internal_document"),
    path("<int:pk>/documenti/fornitura/genera/", views.generate_supply_document, name="generate_supply_document"),
    path("<int:pk>/stato/<str:status>/", views.update_estimate_status, name="update_status"),
    path("<int:pk>/condizioni-cliente/conferma/", views.confirm_commercial_terms_review, name="confirm_commercial_terms_review"),
    path("<int:pk>/commessa/crea/", views.create_job, name="create_job"),
    path("<int:pk>/configurazioni/nuova/", views.configuration_create, name="configuration_create"),
    path("configurazioni/<int:pk>/modifica/", views.configuration_update, name="configuration_update"),
    path("configurazioni/<int:pk>/costi/auto/materiale/", views.add_material_cost, name="add_material_cost"),
    path("configurazioni/<int:pk>/costi/auto/macchina/", views.add_machine_time_cost, name="add_machine_time_cost"),
    path("configurazioni/<int:pk>/costi/auto/setup/", views.add_setup_cost, name="add_setup_cost"),
    path("configurazioni/<int:pk>/prezzo/applica/", views.apply_pricing_rule, name="apply_pricing_rule"),
    path("configurazioni/<int:pk>/costi/nuovo/", views.cost_item_create, name="cost_item_create"),
    path("costi/<int:pk>/modifica/", views.cost_item_update, name="cost_item_update"),
]
