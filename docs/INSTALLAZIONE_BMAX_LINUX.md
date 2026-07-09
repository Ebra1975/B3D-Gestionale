# Installazione BMAX Linux Server

## Scopo

Questa e la prima procedura per installare il gestionale B3D Lab sul mini PC BMAX con Linux Server.

La procedura e pensata per uso in rete locale da browser.

## Risultato Atteso

A fine installazione il gestionale deve essere raggiungibile da un altro PC della stessa rete con un indirizzo simile a:

```text
http://IP_DEL_BMAX:8000
```

Dopo la configurazione del nome locale, l'indirizzo consigliato diventa:

```text
http://b3d-gestionale.local:8000
```

Prima installazione reale Sprint 18:

```text
http://192.168.1.143:8000
```

## Prerequisiti

Sul BMAX servono:

- Linux Server installato e aggiornato;
- Docker;
- Docker Compose;
- Git;
- accesso alla rete locale;
- cartella dedicata al progetto.

## Preparazione Sistema

Aggiornare il sistema:

```bash
sudo apt update
sudo apt upgrade
```

Installare strumenti base:

```bash
sudo apt install git ca-certificates curl
```

Installare Docker seguendo la procedura ufficiale della distribuzione Linux scelta.

## Scaricare Il Progetto

Quando il collegamento GitHub sara pronto:

```bash
git clone https://github.com/Ebra1975/B3D-Gestionale.git gestionale-b3d
cd gestionale-b3d
```

La procedura di collegamento GitHub e descritta in `docs/GITHUB_E_VERSIONAMENTO.md`.

## Configurare `.env`

Creare il file `.env` partendo da `.env.example`.

Valori importanti:

```text
COMPOSE_PROJECT_NAME=gestionale-b3d

DJANGO_ENV=prod
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,IP_DEL_BMAX,b3d-gestionale.local

POSTGRES_DB=b3dlab
POSTGRES_USER=b3dlab
POSTGRES_PASSWORD=password_da_cambiare
POSTGRES_HOST=db
POSTGRES_PORT=5432

REDIS_URL=redis://redis:6379/0
TIME_ZONE=Europe/Rome
```

La password PostgreSQL e `DJANGO_SECRET_KEY` devono essere cambiate prima dell'uso reale.

## Primo Avvio

Costruire e avviare i servizi:

```bash
docker compose up -d --build
```

Applicare le migrazioni:

```bash
docker compose exec web python manage.py migrate
```

Creare l'utente amministratore:

```bash
docker compose exec web python manage.py createsuperuser
```

Raccogliere i file statici:

```bash
docker compose exec web python manage.py collectstatic --noinput
```

Controllare che i servizi siano accesi:

```bash
docker compose ps
```

## Verifica

Controllare lo stato applicazione:

```bash
docker compose exec web python manage.py check
```

Aprire dal browser:

```text
http://IP_DEL_BMAX:8000
```

Controllare:

- dashboard;
- clienti;
- preventivi;
- commesse;
- documenti;
- generazione PDF tramite LibreOffice.

La verifica PDF reale sul BMAX e descritta in:

```text
docs/VERIFICA_PDF_BMAX.md
```

Nella prima installazione reale sul BMAX sono stati verificati:

- dashboard raggiungibile;
- admin Django raggiungibile;
- migrazioni PostgreSQL completate;
- backup manuale creato;
- prova di ripristino completata;
- cron backup giornaliero alle 02:30 configurato.

## Avvio Ordinario

Per avviare normalmente:

```bash
docker compose up -d
```

Per fermare:

```bash
docker compose stop
```

Per riavviare:

```bash
docker compose restart
```

I servizi Docker sono configurati con riavvio automatico `unless-stopped`, quindi dopo un riavvio del BMAX Docker prova a riaccendere automaticamente gestionale, database, Redis e lavorazioni in background.

La procedura dettagliata e in:

```text
docs/AVVIO_AUTOMATICO_BMAX.md
```

## Aggiornamento Da GitHub

Quando una nuova versione e stata inviata su GitHub:

1. creare un backup seguendo `docs/BACKUP_E_RIPRISTINO.md`;
2. aggiornare il codice;
3. ricostruire i servizi;
4. applicare migrazioni;
5. verificare dal browser.

Comandi:

```bash
git pull
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py collectstatic --noinput
docker compose exec web python manage.py check
```

## Manutenzione

La procedura ordinaria di controllo e aggiornata in:

```text
docs/PROCEDURA_MANUTENZIONE.md
```

La configurazione del nome locale e descritta in:

```text
docs/INDIRIZZO_LOCALE_BMAX.md
```

## Note Importanti

- La prima installazione resta pensata per rete locale.
- Accesso remoto solo con soluzione sicura, preferibilmente VPN.
- Il file `.env` non va caricato su GitHub.
- Prima dell'uso reale va provato almeno un backup e ripristino.
- Le password predefinite di `.env.example` non vanno usate in produzione.

## Da Rifinire Prima Della Produzione Stabile

Completato nello Sprint 19:

- avvio automatico dopo riavvio BMAX;
- nome locale `b3d-gestionale.local:8000`;
- generazione DOCX/PDF reale tramite LibreOffice;
- copia backup verificata sul secondo disco interno in `/mnt/backup/b3d_backups`.

Resta da valutare dopo l'uso reale:

- copia periodica fuori dal mini PC fisico;
- pulizia ordinata dei dati test;
- eventuale rimozione di `:8000` con proxy locale.
