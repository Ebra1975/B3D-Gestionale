# Backup E Ripristino

## Scopo

Questa procedura spiega cosa salvare per non perdere il lavoro del gestionale B3D Lab.

La prima versione usa due scenari:

- sviluppo locale Windows con SQLite;
- produzione futura su BMAX Linux Server con PostgreSQL e Docker Compose.

## Cosa Va Salvato

Salvare sempre:

- database;
- cartella `media/`, con documenti generati e file caricati;
- file `.env` del server, conservato in luogo sicuro;
- documentazione di progetto in `docs/`;
- codice sorgente tramite Git/GitHub.

Non basta salvare solo il codice: i dati reali stanno nel database e nei file media.

## Backup Locale Windows

In sviluppo locale il database e il file:

```text
db.sqlite3
```

Per creare un backup locale usare:

```bash
python manage.py backup_local
```

Il comando crea un file `.zip` nella cartella:

```text
backups/
```

Il backup locale include:

- `db.sqlite3`;
- `media/`;
- `docs/`.

La cartella `backups/` non viene salvata in Git.

## Ripristino Locale Windows

Per ripristinare un backup locale:

1. chiudere il server Django;
2. conservare una copia della situazione attuale, se esiste;
3. estrarre lo zip di backup nella cartella del progetto;
4. verificare che siano presenti `db.sqlite3` e `media/`;
5. riavviare il gestionale;
6. aprire clienti, preventivi, commesse e documenti per controllare il risultato.

## Backup BMAX Con Docker Compose

Sul BMAX il database previsto e PostgreSQL dentro Docker.

Backup database:

```bash
docker compose exec db pg_dump -U b3dlab b3dlab > backups/b3dlab_db_YYYYMMDD.sql
```

Backup file media:

```bash
tar -czf backups/b3dlab_media_YYYYMMDD.tar.gz media
```

Backup configurazione:

```bash
cp .env backups/env_YYYYMMDD.txt
```

Il file `.env` contiene segreti e password: non va caricato su GitHub.

## Ripristino BMAX

Ripristino database PostgreSQL:

```bash
docker compose exec -T db psql -U b3dlab b3dlab < backups/b3dlab_db_YYYYMMDD.sql
```

Ripristino media:

```bash
tar -xzf backups/b3dlab_media_YYYYMMDD.tar.gz
```

Dopo il ripristino:

```bash
docker compose restart
docker compose exec web python manage.py check
```

## Frequenza Consigliata

Per uso reale:

- backup giornaliero quando il gestionale viene usato;
- backup manuale prima di aggiornamenti importanti;
- copia periodica su disco esterno o NAS;
- almeno una prova di ripristino prima di affidare dati reali al sistema.

## Da Automatizzare

In una fase successiva il backup dovra diventare automatico, con:

- cartella dedicata sul BMAX;
- rotazione dei backup vecchi;
- controllo spazio disco;
- notifica o riepilogo dell'esito.
