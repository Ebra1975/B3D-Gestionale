from django.db.models import Q
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JobForm
from .models import Job


def job_list(request):
    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "").strip()
    jobs = Job.objects.select_related("customer", "estimate", "selected_configuration").all()

    if query:
        jobs = jobs.filter(
            Q(number__icontains=query)
            | Q(customer__name__icontains=query)
            | Q(estimate__number__icontains=query)
            | Q(estimate__subject__icontains=query)
            | Q(selected_configuration__name__icontains=query)
        )

    valid_statuses = {value for value, _ in Job.Status.choices}
    if status in valid_statuses:
        jobs = jobs.filter(status=status)
    else:
        status = ""

    return render(
        request,
        "jobs/list.html",
        {
            "jobs": jobs,
            "query": query,
            "status_filter": status,
            "status_choices": Job.Status.choices,
        },
    )


def job_detail(request, pk):
    job = get_object_or_404(
        Job.objects.select_related(
            "customer",
            "estimate",
            "selected_configuration",
            "selected_configuration__material",
            "selected_configuration__printer",
        ).prefetch_related(
            "selected_configuration__cost_items",
            "estimate__generated_documents",
        ),
        pk=pk,
    )
    return render(request, "jobs/detail.html", {"job": job})


def job_update(request, pk):
    job = get_object_or_404(Job.objects.select_related("estimate"), pk=pk)
    form = JobForm(request.POST or None, instance=job)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Commessa aggiornata.")
        return redirect("jobs:detail", pk=job.pk)
    return render(request, "jobs/form.html", {"form": form, "job": job, "title": f"Modifica {job.number}"})
