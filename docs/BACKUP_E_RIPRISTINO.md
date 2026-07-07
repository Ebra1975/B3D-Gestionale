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

Creare la cartella backup se non esiste:

```bash
mkdir -p backups
```

Backup database:

```bash
docker compose exec db pg_dump -U b3dlab b3dlab > backups/b3dlab_db_YYYYMMDD.sql
```

Backup file media e documenti generati.

Nel `docker-compose.yml` attuale la cartella `media` del gestionale e montata come volume Docker `media_data`.

Con `COMPOSE_PROJECT_NAME=gestionale-b3d` nel file `.env`, il volume si chiama `gestionale-b3d_media_data`. Per salvarlo in modo affidabile usare:

```bash
docker run --rm -v gestionale-b3d_media_data:/media_data -v "$(pwd)/backups:/backup" alpine tar -czf /backup/b3dlab_media_YYYYMMDD.tar.gz -C /media_data .
```

Se `COMPOSE_PROJECT_NAME` viene cambiato o non viene impostato, il nome del volume Docker puo cambiare. Verificarlo con:

```bash
docker volume ls
```

Backup configurazione:

```bash
cp .env backups/env_YYYYMMDD.txt
```

Il file `.env` contiene segreti e password: non va caricato su GitHub.

## Backup Prima Di Aggiornare

Prima di eseguire `git pull` o aggiornare Docker sul BMAX:

1. creare backup database;
2. creare backup media;
3. salvare `.env`;
4. copiare almeno una volta il backup fuori dal BMAX se contiene dati reali importanti.

## Ripristino BMAX

Prima di ripristinare, fermare i servizi che usano il database:

```bash
docker compose stop web worker beat
```

Ripristino database PostgreSQL:

```bash
docker compose exec -T db psql -U b3dlab b3dlab < backups/b3dlab_db_YYYYMMDD.sql
```

Ripristino media:

```bash
docker run --rm -v gestionale-b3d_media_data:/media_data -v "$(pwd)/backups:/backup" alpine sh -c "rm -rf /media_data/* && tar -xzf /backup/b3dlab_media_YYYYMMDD.tar.gz -C /media_data"
```

Dopo il ripristino:

```bash
docker compose up -d
docker compose exec web python manage.py check
```

Aprire poi il gestionale e controllare clienti, preventivi, commesse, documenti e file allegati.

## Prova Di Ripristino Obbligatoria

Prima di affidare dati reali al gestionale, fare almeno una prova di ripristino su una copia di test.

La prova deve confermare che:

- il database ripristinato si apre;
- i documenti generati sono presenti;
- i file caricati sono presenti;
- il gestionale parte senza errori;
- l'utente amministratore riesce ad accedere.

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
