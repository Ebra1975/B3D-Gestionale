from datetime import datetime
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Crea un backup locale di sviluppo con database SQLite, media e documentazione."

    def add_arguments(self, parser):
        parser.add_argument(
            "--output-dir",
            default="backups",
            help="Cartella in cui salvare il file zip di backup.",
        )

    def handle(self, *args, **options):
        if settings.DJANGO_ENV != "dev":
            raise CommandError(
                "backup_local e pensato solo per sviluppo locale con SQLite. "
                "In produzione usare la procedura PostgreSQL documentata."
            )

        base_dir = Path(settings.BASE_DIR)
        output_dir = base_dir / options["output_dir"]
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_path = output_dir / f"b3dlab_backup_locale_{timestamp}.zip"

        included_paths = [
            base_dir / "db.sqlite3",
            base_dir / "media",
            base_dir / "docs",
        ]

        with ZipFile(archive_path, "w", ZIP_DEFLATED) as archive:
            files_added = 0
            for path in included_paths:
                if not path.exists():
                    self.stdout.write(self.style.WARNING(f"Saltato, non trovato: {path.name}"))
                    continue
                if path.is_file():
                    archive.write(path, path.relative_to(base_dir))
                    files_added += 1
                    continue
                for file_path in path.rglob("*"):
                    if file_path.is_file():
                        archive.write(file_path, file_path.relative_to(base_dir))
                        files_added += 1

        if files_added == 0:
            archive_path.unlink(missing_ok=True)
            raise CommandError("Nessun file trovato da salvare.")

        self.stdout.write(self.style.SUCCESS(f"Backup creato: {archive_path}"))
        self.stdout.write(f"File inclusi: {files_added}")
