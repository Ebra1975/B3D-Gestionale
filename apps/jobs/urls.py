from django.urls import path

from . import views


app_name = "jobs"

urlpatterns = [
    path("", views.job_list, name="list"),
    path("<int:pk>/", views.job_detail, name="detail"),
    path("<int:pk>/modifica/", views.job_update, name="update"),
]
