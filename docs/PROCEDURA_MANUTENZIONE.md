# Procedura Manutenzione

## Scopo

Questa procedura spiega cosa controllare per mantenere il gestionale B3D Lab funzionante sul mini PC BMAX.

E pensata per una persona non tecnica: l'obiettivo e sapere cosa fare, quando farlo e quando fermarsi prima di rischiare i dati.

## Regola Principale

Prima di ogni aggiornamento importante fare sempre un backup e controllare che il gestionale funzioni.

Non aggiornare il server se:

- il backup non e stato creato;
- lo spazio disco e quasi pieno;
- il gestionale contiene dati importanti e non e mai stato provato un ripristino;
- non si ha tempo per verificare il risultato.

## Controllo Giornaliero

Quando il gestionale viene usato, controllare:

- apertura dashboard;
- presenza dei clienti e preventivi recenti;
- possibilita di aprire documenti generati;
- assenza di errori evidenti nel browser.

Se qualcosa non torna, non fare aggiornamenti: prima creare un backup e segnare cosa e successo.

Il backup automatico giornaliero e pianificato alle 02:30 sul BMAX.

## Controllo Settimanale

Una volta a settimana:

```bash
docker compose ps
```

Controllare che i servizi principali siano attivi:

- `web`;
- `db`;
- `redis`;
- `worker`;
- `beat`.

Controllare lo spazio disco:

```bash
df -h
```

Controllare che il backup automatico stia creando archivi recenti:

```bash
ls -lh backups/bmax
tail -n 30 backups/bmax/backup.log
```

Se non ci sono backup recenti, creare subito un backup manuale:

```bash
scripts/bmax_backup.sh
```

## Controllo Mensile

Una volta al mese:

- copiare almeno un backup fuori dal disco principale del BMAX;
- aprire un backup recente e controllare che contenga database, media e configurazione;
- eseguire una prova di ripristino su un backup recente, se non e stata fatta di recente;
- verificare che GitHub sia aggiornato con l'ultima versione del codice;
- leggere eventuali note aperte in `docs/APPROVAZIONI.md`.

Copia ultimo backup fuori dal BMAX:

```bash
EXTERNAL_BACKUP_DIR=/mnt/backup/b3d_backups scripts/bmax_copy_latest_backup.sh
```

Sul BMAX B3D Lab la prima destinazione reale e `/mnt/backup/b3d_backups`, sul secondo disco interno etichettato `b3d-backup`.

Nota: il secondo disco interno protegge dal guasto del disco principale. Per dati reali importanti resta consigliata anche una copia periodica fuori dal mini PC fisico.

Prova ripristino:

```bash
scripts/bmax_restore_test.sh backups/bmax/NOME_BACKUP.tar.gz
```

## Aggiornare Il Gestionale Sul BMAX

Prima dell'aggiornamento:

1. fare backup;
2. segnare data e motivo dell'aggiornamento;
3. verificare che nessuno stia usando il gestionale.

Poi:

```bash
git pull
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py collectstatic --noinput
docker compose exec web python manage.py check
```

Dopo l'aggiornamento aprire dal browser:

```text
http://b3d-gestionale.local:8000
```

Se il nome locale non risponde, provare anche l'indirizzo IP del BMAX:

```text
http://192.168.1.143:8000
```

Controllare:

- dashboard;
- lista clienti;
- dettaglio di un cliente;
- lista preventivi;
- dettaglio di un preventivo;
- generazione documento, se lo sprint aggiornato riguarda i documenti.

Per una prova completa DOCX/PDF sul BMAX usare:

```bash
docker compose exec web python manage.py verify_pdf_export
```

Il comando PDF crea dati test. Dopo la verifica, e prima dell'uso con clienti reali, usare la procedura documentata in `docs/PULIZIA_DATI_TEST_USO_REALE.md`.

Anteprima dati test:

```bash
docker compose exec web python manage.py prepare_real_use
```

Pulizia reale, solo dopo backup:

```bash
docker compose exec web python manage.py prepare_real_use --apply --confirm "PULISCI DATI TEST"
```

## Riavvio

Il gestionale e configurato per riaccendersi automaticamente dopo il riavvio del BMAX, tramite la regola Docker `restart: unless-stopped`.

Per riavviare il gestionale:

```bash
docker compose restart
```

Per fermarlo:

```bash
docker compose stop
```

Per riaccenderlo:

```bash
docker compose up -d
```

La prova completa di riavvio del mini PC e descritta in `docs/AVVIO_AUTOMATICO_BMAX.md`.

La configurazione del nome locale e descritta in `docs/INDIRIZZO_LOCALE_BMAX.md`.

## Quando Chiedere Aiuto

Chiedere supporto prima di procedere se:

- il database non parte;
- il backup fallisce;
- il ripristino fallisce;
- Git segnala conflitti;
- dopo un aggiornamento mancano dati;
- il PDF non viene generato sul BMAX.

In questi casi non cancellare file e non svuotare volumi Docker senza una copia di sicurezza.

## Registro Manutenzione

Tenere traccia degli interventi importanti con una nota semplice:

```text
Data:
Operazione:
Backup creato:
Esito:
Problemi:
```

Il registro puo stare in un file locale non caricato su GitHub se contiene informazioni operative o sensibili.
