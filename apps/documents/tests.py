import shutil
import tempfile
from decimal import Decimal

from django.test import TestCase, override_settings
from django.utils import timezone

from apps.customers.models import Customer
from apps.documents.models import DocumentProfile, GeneratedDocument
from apps.documents.services import build_document_export_checks, generate_internal_estimate_docx
from apps.estimates.models import CostItem, Estimate, EstimateConfiguration
from apps.inventory.models import Material


class DocumentExportTests(TestCase):
    def setUp(self):
        self.media_root = tempfile.mkdtemp(prefix="b3dlab_test_media_")
        self.override = override_settings(MEDIA_ROOT=self.media_root)
        self.override.enable()

    def tearDown(self):
        self.override.disable()
        shutil.rmtree(self.media_root, ignore_errors=True)

    def test_export_checks_block_empty_estimate(self):
        estimate = Estimate.objects.create(
            number="B3D-DOC-EMPTY",
            customer=Customer.objects.create(name="Cliente Documenti"),
            subject="",
            date=timezone.localdate(),
        )

        checks = build_document_export_checks(estimate)

        self.assertFalse(checks["can_generate"])
        self.assertIn("Completare l'oggetto del preventivo.", checks["missing_items"])
        self.assertIn("Inserire una descrizione della richiesta cliente.", checks["missing_items"])
        self.assertIn("Scegliere o aggiungere una configurazione tecnica.", checks["missing_items"])

    def test_internal_document_is_generated_from_same_cost_items(self):
        DocumentProfile.objects.create(
            name="Profilo test",
            company_name="B3D Lab Test",
            fiscal_note="Nota fiscale da validare con commercialista.",
            active=True,
        )
        material = Material.objects.create(name="PETG", cost_per_unit=Decimal("20.00"))
        estimate = Estimate.objects.create(
            number="B3D-DOC-001",
            customer=Customer.objects.create(name="Cliente PDF", email="cliente@example.com"),
            subject="Supporto tecnico",
            description="Realizzazione e validazione di un componente tecnico.",
            date=timezone.localdate(),
            valid_until=timezone.localdate(),
            quantity=2,
        )
        configuration = EstimateConfiguration.objects.create(
            estimate=estimate,
            name="Configurazione scelta",
            description="Soluzione FDM in PETG.",
            material=material,
            quantity=2,
            is_selected=True,
        )
        CostItem.objects.create(
            configuration=configuration,
            category=CostItem.Category.MATERIAL,
            description="Materiale PETG",
            quantity=Decimal("1.00"),
            unit="kg",
            unit_cost=Decimal("20.00"),
        )
        CostItem.objects.create(
            configuration=configuration,
            category=CostItem.Category.MARGIN,
            description="Margine commerciale",
            quantity=Decimal("1.00"),
            unit="voce",
            unit_cost=Decimal("10.00"),
        )

        document = generate_internal_estimate_docx(estimate)

        self.assertEqual(document.document_type, GeneratedDocument.DocumentType.INTERNAL)
        self.assertEqual(document.version, 1)
        self.assertTrue(document.docx_file.name.endswith("_interno_v1.docx"))
        self.assertEqual(configuration.total, Decimal("30.00"))
