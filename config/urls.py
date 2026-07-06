from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("clienti/", include("apps.customers.urls")),
    path("preventivi/", include("apps.estimates.urls")),
    path("commesse/", include("apps.jobs.urls")),
    path("magazzino/", include("apps.inventory.urls")),
    path("documenti/", include("apps.documents.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
