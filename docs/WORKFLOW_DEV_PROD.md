# Workflow Dev / Prod

## Scopo

Questo documento definisce come lavorare sul gestionale durante lo sviluppo e come portarlo poi in produzione sul mini PC BMAX.

## Decisione

Il progetto usera due ambienti:

- Windows come ambiente di sviluppo;
- BMAX con Linux Server come ambiente di produzione.

Il passaggio tra i due ambienti avverra tramite GitHub.

## Ambiente Dev - Windows

Sul PC Windows si lavora su:

- codice;
- documentazione;
- interfaccia;
- modelli dati;
- template `.docx`;
- test base;
- prime funzioni operative.

In sviluppo il gestionale usa SQLite.

Motivi:

- non richiede PostgreSQL locale;
- semplifica l'avvio;
- basta per sviluppare le funzioni iniziali;
- riduce la complessita sul PC Windows.

## Ambiente Prod - BMAX Linux Server

Sul BMAX girera la versione stabile del gestionale.

In produzione saranno usati:

- Linux Server;
- Docker Compose;
- Django;
- PostgreSQL;
- Redis;
- Celery;
- LibreOffice headless;
- backup automatici.

## Database

### Dev

SQLite.

### Prod

PostgreSQL.

### Regola

Durante lo sviluppo evitare funzioni specifiche di SQLite o PostgreSQL non gestite da Django.

Usare modelli Django standard e migrazioni Django, cosi il passaggio a PostgreSQL resta pulito.

## GitHub

GitHub sara usato come ponte tra sviluppo e produzione.

Flusso previsto:

1. Si lavora su Windows.
2. Si salvano le modifiche nel repository Git.
3. Si pubblicano le modifiche su GitHub.
4. Il BMAX scarica la versione aggiornata.
5. Sul BMAX si applicano migrazioni, statici e riavvio servizi.

## Configurazione Ambiente

La variabile principale e:

```text
DJANGO_ENV
```

Valori:

- `dev`: usa SQLite;
- `prod`: usa PostgreSQL.

In Windows sviluppo:

```text
DJANGO_ENV=dev
```

Sul BMAX:

```text
DJANGO_ENV=prod
```

## Rischi Da Evitare

- Scrivere codice che funziona solo su SQLite.
- Modificare manualmente il database senza migrazioni.
- Caricare file `.env`, database locali o allegati su GitHub.
- Fare modifiche direttamente in produzione senza riportarle nel repository.

## Regola Pratica

Lo sviluppo resta semplice su Windows.

La produzione resta ordinata sul BMAX.

GitHub diventa il punto di passaggio ufficiale.
