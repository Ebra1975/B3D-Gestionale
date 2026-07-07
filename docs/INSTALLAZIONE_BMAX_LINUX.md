# Installazione BMAX Linux Server

## Scopo

Questa e la prima procedura per installare il gestionale B3D Lab sul mini PC BMAX con Linux Server.

La procedura e pensata per uso in rete locale da browser.

## Risultato Atteso

A fine installazione il gestionale deve essere raggiungibile da un altro PC della stessa rete con un indirizzo simile a:

```text
http://IP_DEL_BMAX:8000
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
DJANGO_ENV=prod
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,IP_DEL_BMAX

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
docker compose up --build
```

In un secondo terminale applicare le migrazioni:

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

## Avvio In Background

Quando la configurazione e corretta:

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

## Note Importanti

- La prima installazione resta pensata per rete locale.
- Accesso remoto solo con soluzione sicura, preferibilmente VPN.
- Il file `.env` non va caricato su GitHub.
- Prima dell'uso reale va provato almeno un backup e ripristino.

## Da Rifinire Prima Della Produzione Stabile

- Collegamento GitHub definitivo.
- Dominio o nome locale del BMAX.
- Procedura backup automatico.
- Eventuale servizio systemd per riavvio automatico.
- Verifica LibreOffice PDF direttamente sul BMAX.
