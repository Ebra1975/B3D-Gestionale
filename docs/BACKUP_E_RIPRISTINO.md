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

### Backup Automatico Consigliato

Lo Sprint 18 introduce uno script dedicato:

```bash
scripts/bmax_backup.sh
```

Il problema pratico che risolve e questo: quando il gestionale contiene dati reali, il backup non deve dipendere dalla memoria dell'operatore. Deve creare sempre un archivio completo e datato, controllando anche lo spazio disponibile.

Lo script salva in un unico archivio `.tar.gz`:

- database PostgreSQL;
- file caricati e documenti generati nel volume `media`;
- copia del file `.env`, da conservare con attenzione;
- manifesto del backup;
- checksum per controllare che i file non siano corrotti.

Prima del primo uso sul BMAX rendere eseguibili gli script:

```bash
chmod +x scripts/bmax_backup.sh scripts/bmax_restore_test.sh
```

Esecuzione manuale:

```bash
scripts/bmax_backup.sh
```

Il backup viene creato in:

```text
backups/bmax/
```

Per impostazione predefinita lo script mantiene i backup degli ultimi 30 giorni e richiede almeno 1 GB libero nella destinazione.

Valori modificabili al bisogno:

```bash
BACKUP_DIR=/percorso/backup RETENTION_DAYS=60 MIN_FREE_MB=2048 scripts/bmax_backup.sh
```

### Pianificazione Automatica

Sul BMAX si puo programmare il backup giornaliero con `cron`.

Aprire la pianificazione:

```bash
crontab -e
```

Esempio: backup ogni giorno alle 02:30, con log dell'esito:

```cron
30 2 * * * cd /percorso/gestionale-b3d && scripts/bmax_backup.sh >> backups/bmax/backup.log 2>&1
```

Sostituire `/percorso/gestionale-b3d` con la cartella reale del progetto sul BMAX.

Il log non sostituisce il controllo umano: una volta a settimana va verificato che nella cartella `backups/bmax/` ci siano archivi recenti.

### Backup Manuale Di Emergenza

I comandi manuali restano utili se lo script non e disponibile o se si vuole capire cosa succede passo passo.

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

Lo Sprint 18 introduce uno script per provarlo senza toccare il gestionale reale:

```bash
scripts/bmax_restore_test.sh backups/bmax/b3dlab_bmax_YYYYMMDD_HHMMSS.tar.gz
```

La prova crea contenitori e volumi Docker temporanei, ripristina database e media, controlla i checksum se presenti e alla fine pulisce l'ambiente di test.

Se serve ispezionare manualmente l'ambiente prima della pulizia:

```bash
KEEP_RESTORE_TEST=1 scripts/bmax_restore_test.sh backups/bmax/b3dlab_bmax_YYYYMMDD_HHMMSS.tar.gz
```

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

Completato nello Sprint 18:

- cartella dedicata sul BMAX;
- rotazione dei backup vecchi;
- controllo spazio disco;
- riepilogo dell'esito su terminale e log cron.

Resta da valutare in futuro:

- notifica automatica via email o altro canale;
- copia automatica fuori dal BMAX, ad esempio su NAS o disco esterno;
- controllo periodico visibile nella dashboard del gestionale.
