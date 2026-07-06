from django.shortcuts import render

from apps.customers.models import Customer
from apps.documents.models import GeneratedDocument
from apps.estimates.models import Estimate, Prototype
from apps.jobs.models import Job


def dashboard(request):
    context = {
        "open_estimates_count": Estimate.objects.exclude(
            status__in=[Estimate.Status.ACCEPTED, Estimate.Status.REJECTED, Estimate.Status.CANCELLED]
        ).count(),
        "active_jobs_count": Job.objects.exclude(status__in=[Job.Status.DELIVERED, Job.Status.CANCELLED]).count(),
        "generated_documents_count": GeneratedDocument.objects.count(),
        "pending_prototypes_count": Prototype.objects.exclude(
            status__in=[Prototype.Status.NOT_PLANNED, Prototype.Status.VALIDATED]
        ).count(),
        "customers_count": Customer.objects.count(),
        "latest_estimates": Estimate.objects.select_related("customer").all()[:5],
    }
    return render(request, "core/dashboard.html", context)
