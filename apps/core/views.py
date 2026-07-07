from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

from apps.customers.models import Customer, CustomerAgreement, CustomerCommercialDocument
from apps.documents.models import GeneratedDocument
from apps.estimates.models import Estimate, Prototype
from apps.jobs.models import Job


def build_dashboard_context():
    today = timezone.localdate()
    soon = today + timedelta(days=14)
    commercial_soon = today + timedelta(days=30)
    open_estimate_statuses = [
        Estimate.Status.DRAFT,
        Estimate.Status.SENT,
        Estimate.Status.REVISION,
    ]
    active_job_statuses = [
        Job.Status.TODO,
        Job.Status.DESIGN,
        Job.Status.PRINTING,
        Job.Status.POST_PROCESSING,
        Job.Status.READY,
        Job.Status.PAUSED,
    ]

    return {
        "open_estimates_count": Estimate.objects.exclude(
            status__in=[Estimate.Status.ACCEPTED, Estimate.Status.REJECTED, Estimate.Status.CANCELLED]
        ).count(),
        "active_jobs_count": Job.objects.exclude(status__in=[Job.Status.DELIVERED, Job.Status.CANCELLED]).count(),
        "ready_jobs_count": Job.objects.filter(status=Job.Status.READY).count(),
        "generated_documents_count": GeneratedDocument.objects.count(),
        "pending_prototypes_count": Prototype.objects.exclude(
            status__in=[Prototype.Status.NOT_PLANNED, Prototype.Status.VALIDATED]
        ).count(),
        "customers_count": Customer.objects.count(),
        "latest_estimates": Estimate.objects.select_related("customer").all()[:5],
        "estimates_to_follow": Estimate.objects.select_related("customer")
        .filter(status__in=open_estimate_statuses, valid_until__isnull=False, valid_until__lte=soon)
        .order_by("valid_until", "number")[:6],
        "jobs_to_follow": Job.objects.select_related("customer", "estimate")
        .filter(status__in=active_job_statuses, expected_delivery__isnull=False, expected_delivery__lte=soon)
        .order_by("expected_delivery", "number")[:6],
        "agreements_to_follow": CustomerAgreement.objects.select_related("customer")
        .filter(
            status__in=[CustomerAgreement.Status.ACTIVE, CustomerAgreement.Status.DRAFT],
            ends_on__isnull=False,
            ends_on__lte=commercial_soon,
        )
        .order_by("ends_on", "customer__name", "name")[:6],
        "commercial_documents_to_follow": CustomerCommercialDocument.objects.select_related("customer")
        .filter(
            status__in=[
                CustomerCommercialDocument.Status.SENT,
                CustomerCommercialDocument.Status.SIGNED,
                CustomerCommercialDocument.Status.ACTIVE,
            ],
            expires_on__isnull=False,
            expires_on__lte=commercial_soon,
        )
        .order_by("expires_on", "customer__name", "name")[:6],
        "today": today,
    }


def dashboard(request):
    context = build_dashboard_context()
    return render(request, "core/dashboard.html", context)


def manual(request):
    return render(request, "core/manual.html")
