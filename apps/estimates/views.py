from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from apps.documents.models import GeneratedDocument
from apps.documents.services import generate_consulting_estimate_docx
from apps.jobs.services import create_job_from_estimate

from .forms import CostItemForm, EstimateConfigurationForm, EstimateForm
from .models import CostItem, Estimate, EstimateConfiguration


def upsert_cost_item(configuration, category, defaults):
    cost_item = (
        CostItem.objects.filter(
            configuration=configuration,
            category=category,
            description=defaults["description"],
        )
        .order_by("id")
        .first()
    )
    created = cost_item is None
    if created:
        cost_item = CostItem(configuration=configuration, category=category)

    for field, value in defaults.items():
        setattr(cost_item, field, value)
    cost_item.save()
    return cost_item, created


def estimate_list(request):
    estimates = Estimate.objects.select_related("customer").all()
    return render(request, "estimates/list.html", {"estimates": estimates})


def build_estimate_readiness(estimate):
    configurations = list(estimate.configurations.all())
    selected_configuration = next((configuration for configuration in configurations if configuration.is_selected), None)
    if not selected_configuration and configurations:
        selected_configuration = configurations[0]

    missing_items = []
    warnings = []

    if not configurations:
        missing_items.append("Aggiungere almeno una configurazione tecnica.")
    if configurations and not any(configuration.is_selected for configuration in configurations):
        warnings.append("Nessuna configurazione marcata come scelta: per ora viene usata la prima.")
    if not estimate.description:
        missing_items.append("Inserire una descrizione della richiesta cliente.")
    if not estimate.valid_until:
        warnings.append("Inserire una data di validita della proposta.")

    if selected_configuration:
        if not selected_configuration.cost_items.exists():
            missing_items.append("Inserire o generare almeno una voce di costo.")
        if not selected_configuration.total:
            missing_items.append("Completare gli importi: il totale della configurazione e ancora zero.")
        if not selected_configuration.description:
            warnings.append("Aggiungere una descrizione alla configurazione scelta.")
        if not selected_configuration.material:
            warnings.append("Indicare il materiale o la tecnologia prevista.")
    else:
        missing_items.append("Scegliere i dati tecnici prima di generare il documento.")

    latest_document = next(
        (
            document
            for document in estimate.generated_documents.all()
            if document.document_type == GeneratedDocument.DocumentType.CONSULTING
        ),
        None,
    )
    existing_job = estimate.jobs.first()

    return {
        "selected_configuration": selected_configuration,
        "missing_items": missing_items,
        "warnings": warnings,
        "latest_document": latest_document,
        "existing_job": existing_job,
        "can_generate": bool(configurations) and not missing_items,
        "can_create_job": estimate.status == Estimate.Status.ACCEPTED and existing_job is None,
    }


def estimate_detail(request, pk):
    estimate = get_object_or_404(
        Estimate.objects.select_related("customer").prefetch_related(
            "configurations__cost_items",
            "generated_documents",
            "jobs",
        ),
        pk=pk,
    )
    return render(
        request,
        "estimates/detail.html",
        {"estimate": estimate, "readiness": build_estimate_readiness(estimate)},
    )


def estimate_create(request):
    form = EstimateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        estimate = form.save()
        messages.success(request, "Preventivo creato.")
        return redirect("estimates:detail", pk=estimate.pk)
    return render(request, "estimates/form.html", {"form": form, "title": "Nuovo preventivo"})


def estimate_update(request, pk):
    estimate = get_object_or_404(Estimate, pk=pk)
    form = EstimateForm(request.POST or None, instance=estimate)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Preventivo aggiornato.")
        return redirect("estimates:detail", pk=estimate.pk)
    return render(request, "estimates/form.html", {"form": form, "estimate": estimate, "title": "Modifica preventivo"})


@require_POST
def generate_consulting_document(request, pk):
    estimate = get_object_or_404(
        Estimate.objects.select_related("customer").prefetch_related("configurations__cost_items"),
        pk=pk,
    )
    if not estimate.configurations.exists():
        messages.error(request, "Aggiungi almeno una configurazione prima di generare il DOCX consulenza.")
        return redirect("estimates:detail", pk=estimate.pk)

    document = generate_consulting_estimate_docx(estimate)
    messages.success(request, f"DOCX consulenza generato: versione {document.version}.")
    return redirect("estimates:detail", pk=estimate.pk)


@require_POST
def update_estimate_status(request, pk, status):
    estimate = get_object_or_404(Estimate, pk=pk)
    valid_statuses = dict(Estimate.Status.choices)
    if status not in valid_statuses:
        messages.error(request, "Stato preventivo non valido.")
        return redirect("estimates:detail", pk=estimate.pk)

    estimate.status = status
    estimate.save(update_fields=["status", "updated_at"])
    messages.success(request, f"Preventivo aggiornato: {valid_statuses[status]}.")
    return redirect("estimates:detail", pk=estimate.pk)


@require_POST
def create_job(request, pk):
    estimate = get_object_or_404(
        Estimate.objects.select_related("customer").prefetch_related("configurations", "jobs"),
        pk=pk,
    )
    try:
        job, created = create_job_from_estimate(estimate)
    except ValueError as error:
        messages.error(request, str(error))
        return redirect("estimates:detail", pk=estimate.pk)

    if created:
        messages.success(request, f"Commessa {job.number} creata dal preventivo.")
    else:
        messages.info(request, f"Commessa {job.number} gia presente per questo preventivo.")
    return redirect("jobs:list")


def configuration_create(request, pk):
    estimate = get_object_or_404(Estimate, pk=pk)
    form = EstimateConfigurationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        configuration = form.save(commit=False)
        configuration.estimate = estimate
        configuration.save()
        messages.success(request, "Configurazione aggiunta.")
        return redirect("estimates:detail", pk=estimate.pk)
    return render(
        request,
        "estimates/configuration_form.html",
        {"form": form, "estimate": estimate, "title": "Nuova configurazione"},
    )


def configuration_update(request, pk):
    configuration = get_object_or_404(EstimateConfiguration.objects.select_related("estimate"), pk=pk)
    form = EstimateConfigurationForm(request.POST or None, instance=configuration)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Configurazione aggiornata.")
        return redirect("estimates:detail", pk=configuration.estimate.pk)
    return render(
        request,
        "estimates/configuration_form.html",
        {"form": form, "estimate": configuration.estimate, "configuration": configuration, "title": "Modifica configurazione"},
    )


def cost_item_create(request, pk):
    configuration = get_object_or_404(EstimateConfiguration.objects.select_related("estimate"), pk=pk)
    form = CostItemForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        cost_item = form.save(commit=False)
        cost_item.configuration = configuration
        cost_item.save()
        messages.success(request, "Voce di costo aggiunta.")
        return redirect("estimates:detail", pk=configuration.estimate.pk)
    return render(
        request,
        "estimates/cost_item_form.html",
        {"form": form, "configuration": configuration, "estimate": configuration.estimate, "title": "Nuova voce di costo"},
    )


@transaction.atomic
@require_POST
def add_material_cost(request, pk):
    configuration = get_object_or_404(EstimateConfiguration.objects.select_related("estimate", "material"), pk=pk)
    if not configuration.material:
        messages.error(request, "Seleziona un materiale nella configurazione prima di generare il costo materiale.")
        return redirect("estimates:detail", pk=configuration.estimate.pk)
    if not configuration.material_weight_per_unit:
        messages.error(request, "Inserisci il peso materiale per unita prima di generare il costo materiale.")
        return redirect("estimates:detail", pk=configuration.estimate.pk)

    quantity = configuration.material_weight_per_unit * configuration.quantity
    _, created = upsert_cost_item(
        configuration,
        CostItem.Category.MATERIAL,
        {
            "description": f"Materiale {configuration.material}",
            "quantity": quantity,
            "unit": "kg/l",
            "unit_cost": configuration.material.cost_per_unit,
            "visible_internal": True,
            "visible_consulting": False,
            "visible_supply": True,
        },
    )
    messages.success(request, "Costo materiale generato." if created else "Costo materiale aggiornato.")
    return redirect("estimates:detail", pk=configuration.estimate.pk)


@transaction.atomic
@require_POST
def add_machine_time_cost(request, pk):
    configuration = get_object_or_404(EstimateConfiguration.objects.select_related("estimate", "printer"), pk=pk)
    if not configuration.printer:
        messages.error(request, "Seleziona una stampante nella configurazione prima di generare il costo macchina.")
        return redirect("estimates:detail", pk=configuration.estimate.pk)
    if not configuration.machine_time_hours_per_unit:
        messages.error(request, "Inserisci le ore macchina per unita prima di generare il costo macchina.")
        return redirect("estimates:detail", pk=configuration.estimate.pk)

    quantity = configuration.machine_time_hours_per_unit * configuration.quantity
    _, created = upsert_cost_item(
        configuration,
        CostItem.Category.MACHINE_TIME,
        {
            "description": f"Tempo macchina {configuration.printer}",
            "quantity": quantity,
            "unit": "h",
            "unit_cost": configuration.printer.hourly_cost,
            "visible_internal": True,
            "visible_consulting": False,
            "visible_supply": True,
        },
    )
    messages.success(request, "Costo tempo macchina generato." if created else "Costo tempo macchina aggiornato.")
    return redirect("estimates:detail", pk=configuration.estimate.pk)


@transaction.atomic
@require_POST
def add_setup_cost(request, pk):
    configuration = get_object_or_404(EstimateConfiguration.objects.select_related("estimate"), pk=pk)
    _, created = upsert_cost_item(
        configuration,
        CostItem.Category.SETUP,
        {
            "description": "Progettazione e setup",
            "quantity": 1,
            "unit": "voce",
            "unit_cost": 0,
            "visible_internal": True,
            "visible_consulting": False,
            "visible_supply": True,
            "notes": "Inserire il valore corretto modificando questa voce.",
        },
    )
    messages.success(
        request,
        "Voce progettazione/setup generata con importo da completare."
        if created
        else "Voce progettazione/setup gia presente e aggiornata.",
    )
    return redirect("estimates:detail", pk=configuration.estimate.pk)


def cost_item_update(request, pk):
    cost_item = get_object_or_404(CostItem.objects.select_related("configuration__estimate"), pk=pk)
    form = CostItemForm(request.POST or None, instance=cost_item)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Voce di costo aggiornata.")
        return redirect("estimates:detail", pk=cost_item.configuration.estimate.pk)
    return render(
        request,
        "estimates/cost_item_form.html",
        {
            "form": form,
            "cost_item": cost_item,
            "configuration": cost_item.configuration,
            "estimate": cost_item.configuration.estimate,
            "title": "Modifica voce di costo",
        },
    )
