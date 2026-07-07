from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomerForm
from .models import Customer


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
        return redirect("customers:update", pk=customer.pk)
    return render(request, "customers/form.html", {"form": form, "title": "Nuovo cliente"})


def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Cliente aggiornato.")
        return redirect("customers:update", pk=customer.pk)
    return render(request, "customers/form.html", {"form": form, "customer": customer, "title": "Modifica cliente"})
