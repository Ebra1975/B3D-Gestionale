from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomerForm
from .models import Customer


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customers/list.html", {"customers": customers})


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
