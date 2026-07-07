import re

from django.db import transaction
from django.utils import timezone

from apps.estimates.models import Estimate

from .models import Job


def selected_configuration_for_job(estimate):
    selected = estimate.configurations.filter(is_selected=True).first()
    return selected or estimate.configurations.first()


def next_job_number():
    year = timezone.localdate().year
    prefix = f"COM-{year}-"
    latest = Job.objects.filter(number__startswith=prefix).order_by("-number").first()
    if not latest:
        return f"{prefix}001"

    match = re.search(r"(\d+)$", latest.number)
    next_value = int(match.group(1)) + 1 if match else 1
    return f"{prefix}{next_value:03d}"


@transaction.atomic
def create_job_from_estimate(estimate):
    existing_job = estimate.jobs.select_related("selected_configuration").first()
    if existing_job:
        return existing_job, False

    if estimate.status != Estimate.Status.ACCEPTED:
        raise ValueError("Il preventivo deve essere accettato prima di creare la commessa.")

    selected_configuration = selected_configuration_for_job(estimate)
    if not selected_configuration:
        raise ValueError("Serve almeno una configurazione tecnica per creare la commessa.")

    job = Job.objects.create(
        number=next_job_number(),
        estimate=estimate,
        customer=estimate.customer,
        selected_configuration=selected_configuration,
        status=Job.Status.TODO,
        operational_notes=(
            f"Commessa creata dal preventivo {estimate.number}. "
            "Completare date operative, file e note di produzione."
        ),
    )
    return job, True
