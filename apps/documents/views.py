from django.shortcuts import render

from .models import DocumentTemplate, GeneratedDocument


def document_list(request):
    templates = DocumentTemplate.objects.all()
    generated_documents = GeneratedDocument.objects.select_related("estimate", "template").all()[:50]
    return render(
        request,
        "documents/list.html",
        {"templates": templates, "generated_documents": generated_documents},
    )
