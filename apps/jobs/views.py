from django.shortcuts import render

from .models import Job


def job_list(request):
    jobs = Job.objects.select_related("customer", "estimate", "selected_configuration").all()
    return render(request, "jobs/list.html", {"jobs": jobs})
