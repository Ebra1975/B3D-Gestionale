from django.urls import path

from . import views


app_name = "customers"

urlpatterns = [
    path("", views.customer_list, name="list"),
    path("nuovo/", views.customer_create, name="create"),
    path("<int:pk>/modifica/", views.customer_update, name="update"),
]
