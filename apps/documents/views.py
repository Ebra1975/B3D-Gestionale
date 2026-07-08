from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import DocumentProfileForm, DocumentTemplateForm
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
            "active_profile": DocumentProfile.get_active(),
            "templates": templates,
            "generated_documents": generated_documents,
            "query": query,
        },
    )


def document_profile_update(request):
    profile = DocumentProfile.get_active()
    form = DocumentProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Dati documento aggiornati. I prossimi DOCX/PDF useranno questi dati.")
        return redirect("documents:list")
    return render(
        request,
        "documents/profile_form.html",
        {
            "form": form,
            "profile": profile,
            "title": "Modifica dati documento",
        },
    )


def document_template_create(request):
    form = DocumentTemplateForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        template = form.save(commit=False)
        if template.active:
            DocumentTemplate.objects.filter(
                document_type=template.document_type,
                active=True,
            ).update(active=False)
        template.save()
        messages.success(request, "Template DOCX caricato. Sara usato nelle prossime generazioni se attivo.")
        return redirect("documents:list")
    return render(
        request,
        "documents/template_form.html",
        {
            "form": form,
            "title": "Nuovo template DOCX",
            "submit_label": "Carica template",
        },
    )


def document_template_update(request, pk):
    template = get_object_or_404(DocumentTemplate, pk=pk)
    form = DocumentTemplateForm(request.POST or None, request.FILES or None, instance=template)
    if request.method == "POST" and form.is_valid():
        updated_template = form.save(commit=False)
        if updated_template.active:
            DocumentTemplate.objects.filter(
                document_type=updated_template.document_type,
                active=True,
            ).exclude(pk=updated_template.pk).update(active=False)
        updated_template.save()
        messages.success(request, "Template DOCX aggiornato.")
        return redirect("documents:list")
    return render(
        request,
        "documents/template_form.html",
        {
            "form": form,
            "template": template,
            "title": "Modifica template DOCX",
            "submit_label": "Salva template",
        },
    )


@require_POST
def document_template_activate(request, pk):
    template = get_object_or_404(DocumentTemplate, pk=pk)
    DocumentTemplate.objects.filter(
        document_type=template.document_type,
        active=True,
    ).exclude(pk=template.pk).update(active=False)
    template.active = True
    template.save(update_fields=["active"])
    messages.success(request, "Template attivato per le prossime generazioni di questo tipo documento.")
    return redirect("documents:list")


@require_POST
def document_template_deactivate(request, pk):
    template = get_object_or_404(DocumentTemplate, pk=pk)
    template.active = False
    template.save(update_fields=["active"])
    messages.success(request, "Template disattivato.")
    return redirect("documents:list")
