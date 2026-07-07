from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomerAgreementForm, CustomerCommercialDocumentForm, CustomerForm
from .models import Customer, CustomerAgreement, CustomerCommercialDocument


def customer_list(request):
    query = request.GET.get("q", "").strip()
    customers = Customer.objects.all()
    if query:
        customers = customers.filter(
            Q(name__icontains=query)
            | Q(contact_person__icontains=query)
            | Q(email__icontains=query)
            | Q(phone__icontains=query)
            | Q(tax_code__icontains=query)
            | Q(notes__icontains=query)
        )
    return render(request, "customers/list.html", {"customers": customers, "query": query})


def customer_create(request):
    form = CustomerForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        customer = form.save()
        messages.success(request, "Cliente creato.")
        return redirect("customers:detail", pk=customer.pk)
    return render(request, "customers/form.html", {"form": form, "title": "Nuovo cliente"})


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    agreements = customer.agreements.all()
    commercial_documents = customer.commercial_documents.all()
    estimates = customer.estimates.all()[:10]
    jobs = customer.jobs.select_related("estimate").all()[:10]
    return render(
        request,
        "customers/detail.html",
        {
            "customer": customer,
            "agreements": agreements,
            "commercial_documents": commercial_documents,
            "estimates": estimates,
            "jobs": jobs,
        },
    )


def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Cliente aggiornato.")
        return redirect("customers:detail", pk=customer.pk)
    return render(request, "customers/form.html", {"form": form, "customer": customer, "title": "Modifica cliente"})


def agreement_create(request, customer_pk):
    customer = get_object_or_404(Customer, pk=customer_pk)
    form = CustomerAgreementForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        agreement = form.save(commit=False)
        agreement.customer = customer
        agreement.save()
        messages.success(request, "Accordo cliente creato.")
        return redirect("customers:detail", pk=customer.pk)
    return render(
        request,
        "customers/agreement_form.html",
        {"form": form, "customer": customer, "title": "Nuovo accordo cliente"},
    )


def agreement_update(request, pk):
    agreement = get_object_or_404(CustomerAgreement.objects.select_related("customer"), pk=pk)
    form = CustomerAgreementForm(request.POST or None, instance=agreement)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Accordo cliente aggiornato.")
        return redirect("customers:detail", pk=agreement.customer.pk)
    return render(
        request,
        "customers/agreement_form.html",
        {"form": form, "customer": agreement.customer, "agreement": agreement, "title": "Modifica accordo cliente"},
    )


def commercial_document_create(request, customer_pk):
    customer = get_object_or_404(Customer, pk=customer_pk)
    form = CustomerCommercialDocumentForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        document = form.save(commit=False)
        document.customer = customer
        document.save()
        messages.success(request, "Documento commerciale creato.")
        return redirect("customers:detail", pk=customer.pk)
    return render(
        request,
        "customers/commercial_document_form.html",
        {"form": form, "customer": customer, "title": "Nuovo documento commerciale"},
    )


def commercial_document_update(request, pk):
    document = get_object_or_404(CustomerCommercialDocument.objects.select_related("customer"), pk=pk)
    form = CustomerCommercialDocumentForm(request.POST or None, request.FILES or None, instance=document)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Documento commerciale aggiornato.")
        return redirect("customers:detail", pk=document.customer.pk)
    return render(
        request,
        "customers/commercial_document_form.html",
        {"form": form, "customer": document.customer, "document": document, "title": "Modifica documento commerciale"},
    )
