from django.shortcuts import render
from django.db.models import Q

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
