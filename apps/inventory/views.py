from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MaterialForm, PrinterForm
from .models import Material, Printer


def material_list(request):
    materials = Material.objects.all()
    return render(request, "inventory/material_list.html", {"materials": materials})


def material_create(request):
    form = MaterialForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        material = form.save()
        messages.success(request, "Materiale creato.")
        return redirect("inventory:material_update", pk=material.pk)
    return render(request, "inventory/material_form.html", {"form": form, "title": "Nuovo materiale"})


def material_update(request, pk):
    material = get_object_or_404(Material, pk=pk)
    form = MaterialForm(request.POST or None, instance=material)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Materiale aggiornato.")
        return redirect("inventory:material_update", pk=material.pk)
    return render(request, "inventory/material_form.html", {"form": form, "material": material, "title": "Modifica materiale"})


def printer_list(request):
    printers = Printer.objects.all()
    return render(request, "inventory/printer_list.html", {"printers": printers})


def printer_create(request):
    form = PrinterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        printer = form.save()
        messages.success(request, "Stampante creata.")
        return redirect("inventory:printer_update", pk=printer.pk)
    return render(request, "inventory/printer_form.html", {"form": form, "title": "Nuova stampante"})


def printer_update(request, pk):
    printer = get_object_or_404(Printer, pk=pk)
    form = PrinterForm(request.POST or None, instance=printer)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Stampante aggiornata.")
        return redirect("inventory:printer_update", pk=printer.pk)
    return render(request, "inventory/printer_form.html", {"form": form, "printer": printer, "title": "Modifica stampante"})
