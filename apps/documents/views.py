from django.db.models import Q
from django.shortcuts import render

from .models import DocumentProfile, DocumentTemplate, GeneratedDocument


def document_list(request):
    query = request.GET.get("q", "").strip()
    templates = DocumentTemplate.objects.all()
    document_profiles = DocumentProfile.objects.all()
    generated_documents = GeneratedDocument.objects.select_related("estimate", "estimate__customer", "template").all()
    if query:
        templates = templates.filter(
            Q(name__icontains=query)
            | Q(profile__icontains=query)
            | Q(template_version__icontains=query)
            | Q(notes__icontains=query)
        )
        generated_documents = generated_documents.filter(
            Q(estimate__number__icontains=query)
            | Q(estimate__subject__icontains=query)
            | Q(estimate__customer__name__icontains=query)
            | Q(notes__icontains=query)
        )
    generated_documents = generated_documents[:50]
    return render(
        request,
        "documents/list.html",
        {
            "document_profiles": document_profiles,
            "templates": templates,
            "generated_documents": generated_documents,
            "query": query,
        },
    )
