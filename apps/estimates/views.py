from django.contrib import messages
from django.db import transaction
from django.db.models import Exists, OuterRef, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST
from datetime import timedelta
from decimal import Decimal, ROUND_CEILING

from apps.customers.models import CustomerAgreement, CustomerCommercialDocument
from apps.documents.models import GeneratedDocument
from apps.documents.services import (
    build_document_export_checks,
    generate_consulting_estimate_docx,
    generate_internal_estimate_docx,
    generate_supply_estimate_docx,
)
from apps.jobs.models import Job
from apps.jobs.services import create_job_from_estimate

from .forms import (
    CommercialTermsReviewForm,
    CostItemForm,
    EstimateConfigurationForm,
    EstimateForm,
    PricingRuleForm,
    TechnicalFileImportForm,
)
from .models import CostItem, Estimate, EstimateConfiguration
from .services import parse_technical_file


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


def money(value):
    return value.quantize(Decimal("0.01"))


def round_up_to_step(value, step):
    if step <= 0:
        return money(value)
    multiplier = (value / step).to_integral_value(rounding=ROUND_CEILING)
    return money(multiplier * step)


def build_configuration_pricing(configuration):
    cost_items = list(configuration.cost_items.all())
    base_cost = sum((item.total for item in cost_items if item.category != CostItem.Category.MARGIN), Decimal("0.00"))
    margin_total = sum((item.total for item in cost_items if item.category == CostItem.Category.MARGIN), Decimal("0.00"))
    total = base_cost + margin_total
    margin_percentage = Decimal("0.00")
    if base_cost:
        margin_percentage = (margin_total / base_cost * Decimal("100")).quantize(Decimal("0.01"))
    return {
        "base_cost": money(base_cost),
        "margin_total": money(margin_total),
        "total": money(total),
        "margin_percentage": margin_percentage,
    }


def estimate_list(request):
    query = request.GET.get("q", "").strip()
    view_filter = request.GET.get("view", "active")
    job_exists = Job.objects.filter(estimate=OuterRef("pk"))
    estimates = Estimate.objects.select_related("customer").annotate(has_job=Exists(job_exists))

    if query:
        estimates = estimates.filter(
            Q(number__icontains=query)
            | Q(customer__name__icontains=query)
            | Q(subject__icontains=query)
            | Q(description__icontains=query)
        )

    if view_filter == "converted":
        estimates = estimates.filter(has_job=True)
    elif view_filter != "all":
        view_filter = "active"
        estimates = estimates.filter(has_job=False)

    return render(
        request,
        "estimates/list.html",
        {
            "estimates": estimates,
            "query": query,
            "view_filter": view_filter,
        },
    )


def build_estimate_readiness(estimate, commercial_memory=None):
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
    if commercial_memory and commercial_memory["has_memory"] and not estimate.commercial_terms_reviewed_at:
        warnings.append("Confermare il controllo di accordi, listini e documenti commerciali del cliente.")

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

    document_checks = build_document_export_checks(estimate)

    return {
        "selected_configuration": selected_configuration,
        "missing_items": missing_items,
        "warnings": warnings,
        "document_missing_items": document_checks["missing_items"],
        "document_warnings": document_checks["warnings"],
        "latest_document": latest_document,
        "existing_job": existing_job,
        "can_generate": document_checks["can_generate"],
        "can_create_job": estimate.status == Estimate.Status.ACCEPTED and existing_job is None,
    }


def build_customer_commercial_memory(customer):
    today = timezone.localdate()
    alert_limit = today + timedelta(days=30)
    agreements = list(customer.agreements.all()[:5])
    commercial_documents = list(customer.commercial_documents.all()[:5])

    agreement_alerts = []
    for agreement in agreements:
        if agreement.status == CustomerAgreement.Status.ACTIVE:
            if agreement.ends_on and agreement.ends_on < today:
                agreement_alerts.append(f"Accordo scaduto: {agreement.name}.")
            elif agreement.ends_on and agreement.ends_on <= alert_limit:
                agreement_alerts.append(f"Accordo in scadenza: {agreement.name}.")

    document_alerts = []
    for document in commercial_documents:
        active_statuses = [
            CustomerCommercialDocument.Status.SIGNED,
            CustomerCommercialDocument.Status.ACTIVE,
        ]
        if document.status in active_statuses:
            if document.expires_on and document.expires_on < today:
                document_alerts.append(f"Documento scaduto: {document.name}.")
            elif document.expires_on and document.expires_on <= alert_limit:
                document_alerts.append(f"Documento in scadenza: {document.name}.")

    return {
        "agreements": agreements,
        "commercial_documents": commercial_documents,
        "alerts": agreement_alerts + document_alerts,
        "has_memory": bool(agreements or commercial_documents),
    }


def estimate_detail(request, pk):
    estimate = get_object_or_404(
        Estimate.objects.select_related("customer").prefetch_related(
            "configurations__cost_items",
            "generated_documents",
            "jobs",
            "customer__agreements",
            "customer__commercial_documents",
        ),
        pk=pk,
    )
    commercial_memory = build_customer_commercial_memory(estimate.customer)
    return render(
        request,
        "estimates/detail.html",
        {
            "estimate": estimate,
            "readiness": build_estimate_readiness(estimate, commercial_memory),
            "commercial_memory": commercial_memory,
            "commercial_review_form": CommercialTermsReviewForm(
                initial={"notes": estimate.commercial_terms_review_notes}
            ),
            "pricing_form": PricingRuleForm(),
        },
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
    checks = build_document_export_checks(estimate)
    if not checks["can_generate"]:
        messages.error(request, "Completa i dati obbligatori prima di generare il documento cliente.")
        for item in checks["missing_items"]:
            messages.error(request, item)
        return redirect("estimates:detail", pk=estimate.pk)

    document = generate_consulting_estimate_docx(estimate)
    messages.success(request, f"Documento cliente generato: versione {document.version}.")
    if not document.pdf_file:
        messages.warning(request, "DOCX creato, ma il PDF non e stato convertito: verificare LibreOffice.")
    return redirect("estimates:detail", pk=estimate.pk)


@require_POST
def generate_internal_document(request, pk):
    estimate = get_object_or_404(
        Estimate.objects.select_related("customer").prefetch_related("configurations__cost_items"),
        pk=pk,
    )
    checks = build_document_export_checks(estimate)
    if not checks["can_generate"]:
        messages.error(request, "Completa i dati obbligatori prima di generare il documento interno.")
        for item in checks["missing_items"]:
            messages.error(request, item)
        return redirect("estimates:detail", pk=estimate.pk)

    document = generate_internal_estimate_docx(estimate)
    messages.success(request, f"Documento interno generato: versione {document.version}.")
    if not document.pdf_file:
        messages.warning(request, "DOCX creato, ma il PDF non e stato convertito: verificare LibreOffice.")
    return redirect("estimates:detail", pk=estimate.pk)


@require_POST
def generate_supply_document(request, pk):
    estimate = get_object_or_404(
        Estimate.objects.select_related("customer").prefetch_related("configurations__cost_items"),
        pk=pk,
    )
    checks = build_document_export_checks(estimate)
    if not checks["can_generate"]:
        messages.error(request, "Completa i dati obbligatori prima di generare il documento fornitura/artigiano.")
        for item in checks["missing_items"]:
            messages.error(request, item)
        return redirect("estimates:detail", pk=estimate.pk)

    document = generate_supply_estimate_docx(estimate)
    messages.success(request, f"Documento fornitura/artigiano preparatorio generato: versione {document.version}.")
    if not document.pdf_file:
        messages.warning(request, "DOCX creato, ma il PDF non e stato convertito: verificare LibreOffice.")
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
def confirm_commercial_terms_review(request, pk):
    estimate = get_object_or_404(Estimate, pk=pk)
    form = CommercialTermsReviewForm(request.POST)
    if not form.is_valid():
        messages.error(request, "Controlla le note della revisione condizioni cliente.")
        return redirect("estimates:detail", pk=estimate.pk)

    estimate.commercial_terms_reviewed_at = timezone.now()
    estimate.commercial_terms_review_notes = form.cleaned_data["notes"]
    estimate.save(
        update_fields=[
            "commercial_terms_reviewed_at",
            "commercial_terms_review_notes",
            "updated_at",
        ]
    )
    messages.success(request, "Controllo condizioni cliente registrato.")
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
    return redirect("jobs:detail", pk=job.pk)


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
            "unit_cost": configuration.material.effective_cost_per_unit,
            "visible_internal": True,
            "visible_consulting": False,
            "visible_supply": True,
            "notes": configuration.material.pricing_summary,
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
            "unit_cost": configuration.printer.effective_hourly_cost,
            "visible_internal": True,
            "visible_consulting": False,
            "visible_supply": True,
            "notes": configuration.printer.pricing_summary,
        },
    )
    messages.success(request, "Costo tempo macchina generato." if created else "Costo tempo macchina aggiornato.")
    return redirect("estimates:detail", pk=configuration.estimate.pk)


@transaction.atomic
@require_POST
def import_technical_file(request, pk):
    configuration = get_object_or_404(EstimateConfiguration.objects.select_related("estimate"), pk=pk)
    form = TechnicalFileImportForm(request.POST, request.FILES)
    if not form.is_valid():
        messages.error(request, "Carica un file G-code, GCO o 3MF valido.")
        return redirect("estimates:detail", pk=configuration.estimate.pk)

    try:
        result = parse_technical_file(form.cleaned_data["technical_file"])
    except Exception:
        messages.error(request, "Il file tecnico non e leggibile. Esporta di nuovo il G-code/3MF dallo slicer e riprova.")
        return redirect("estimates:detail", pk=configuration.estimate.pk)

    if result.material_weight_kg:
        configuration.material_weight_per_unit = result.material_weight_kg
    if result.machine_time_hours:
        configuration.machine_time_hours_per_unit = result.machine_time_hours
    if result.machine_time_hours and not configuration.expected_duration:
        configuration.expected_duration = f"{result.machine_time_hours} h"

    import_note = result.raw_summary
    if configuration.internal_notes:
        configuration.internal_notes = f"{configuration.internal_notes}\n{import_note}"
    else:
        configuration.internal_notes = import_note
    configuration.save()

    if result.has_useful_data:
        messages.success(request, "Dati tecnici importati nella configurazione.")
    else:
        messages.warning(request, "File letto, ma non ho trovato peso, tempo o piatti riconoscibili.")
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


@transaction.atomic
@require_POST
def apply_pricing_rule(request, pk):
    configuration = get_object_or_404(EstimateConfiguration.objects.select_related("estimate"), pk=pk)
    form = PricingRuleForm(request.POST)
    if not form.is_valid():
        messages.error(request, "Controlla margine e arrotondamento: servono valori numerici validi.")
        return redirect("estimates:detail", pk=configuration.estimate.pk)

    pricing = build_configuration_pricing(configuration)
    base_cost = pricing["base_cost"]
    if base_cost <= 0:
        messages.error(request, "Inserisci prima almeno un costo interno diverso dal margine.")
        return redirect("estimates:detail", pk=configuration.estimate.pk)

    margin_percentage = form.cleaned_data["margin_percentage"]
    rounding_step = form.cleaned_data["rounding_step"]
    target_total = base_cost * (Decimal("1.00") + margin_percentage / Decimal("100"))
    target_total = round_up_to_step(target_total, rounding_step)
    margin_value = money(target_total - base_cost)

    margin_items = list(configuration.cost_items.filter(category=CostItem.Category.MARGIN).order_by("id"))
    created = not margin_items
    margin_item = margin_items[0] if margin_items else CostItem(configuration=configuration, category=CostItem.Category.MARGIN)
    margin_item.description = "Margine commerciale"
    margin_item.quantity = 1
    margin_item.unit = "voce"
    margin_item.unit_cost = margin_value
    margin_item.visible_internal = True
    margin_item.visible_consulting = False
    margin_item.visible_supply = True
    margin_item.notes = (
        f"Generato da regola: margine {margin_percentage}%"
        f", arrotondamento {rounding_step} EUR."
    )
    margin_item.save()

    for old_margin_item in margin_items[1:]:
        old_margin_item.unit_cost = Decimal("0.00")
        old_margin_item.quantity = 1
        old_margin_item.notes = "Voce margine disattivata dalla regola prezzo per evitare doppio conteggio."
        old_margin_item.save(update_fields=["quantity", "unit_cost", "total", "notes"])

    messages.success(
        request,
        "Margine commerciale generato." if created else "Margine commerciale aggiornato.",
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
