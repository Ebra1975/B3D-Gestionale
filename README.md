# Gestionale B3D Lab

Gestionale per attivita di consulenza tecnica e manifattura additiva.

La prima versione nasce per uso locale su mini PC Linux Server, ma la struttura e pensata per poter crescere verso un prodotto vendibile o SaaS.

## Stack Approvato

- Django
- PostgreSQL
- Redis + Celery
- Template Django modulari
- HTMX mirato
- CSS separato come piccolo design system
- Template documenti `.docx`
- Conversione PDF con LibreOffice headless
- Docker Compose

## Struttura

- `config/`: configurazione Django.
- `apps/`: moduli applicativi.
- `templates/`: pagine HTML.
- `static/`: CSS e asset statici.
- `media/`: file caricati e generati, esclusi dal controllo versione.
- `docs/`: documentazione decisionale e funzionale.

## Avvio Locale Con Docker

1. Copiare `.env.example` in `.env`.
2. Avviare i servizi:

```bash
docker compose up --build
```

3. Applicare le migrazioni:

```bash
docker compose exec web python manage.py migrate
```

4. Creare l'utente amministratore:

```bash
docker compose exec web python manage.py createsuperuser
```

5. Aprire:

```text
http://localhost:8000
```

## Verifiche

Quando le dipendenze sono installate, eseguire:

```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
```

Nell'ambiente Windows iniziale Django potrebbe non essere installato. La verifica completa e prevista dentro Docker o dentro un ambiente Python con le dipendenze di `requirements.txt`.

## Nota

Questa e una base tecnica iniziale. Le funzioni operative verranno aggiunte progressivamente partendo da clienti, preventivi, configurazioni, costi interni e documenti.

## Sviluppo Windows Senza Docker

In sviluppo su Windows il progetto usa SQLite se `DJANGO_ENV=dev`.

Flusso previsto:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

La produzione sul BMAX usera invece `DJANGO_ENV=prod` con PostgreSQL tramite Docker Compose.

## Backup E Installazione BMAX

Le prime procedure operative sono in:

- `docs/BACKUP_E_RIPRISTINO.md`
- `docs/INSTALLAZIONE_BMAX_LINUX.md`
- `docs/GITHUB_E_VERSIONAMENTO.md`
- `docs/PROCEDURA_MANUTENZIONE.md`
- `docs/AVVIO_AUTOMATICO_BMAX.md`
- `docs/INDIRIZZO_LOCALE_BMAX.md`
- `docs/VERIFICA_PDF_BMAX.md`
- `docs/COPIA_BACKUP_FUORI_BMAX.md`

In sviluppo locale e disponibile il comando:

```bash
python manage.py backup_local
```

Il comando crea uno zip in `backups/` con database SQLite, file media e documentazione.

Sul BMAX reale lo Sprint 19 ha verificato:

- accesso da `http://b3d-gestionale.local:8000`;
- riavvio automatico dei servizi Docker;
- generazione DOCX/PDF tramite LibreOffice;
- backup copiato e verificato sul secondo disco interno.
