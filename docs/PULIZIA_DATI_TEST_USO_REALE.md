# Pulizia Dati Test E Preparazione Uso Reale

## Scopo

Questa procedura serve prima di iniziare a inserire dati reali nel gestionale.

Il problema pratico e semplice: durante le verifiche sono stati creati clienti, preventivi e documenti fittizi. Non devono confondersi con clienti veri, ma non vanno cancellati a mano in modo casuale.

## Regola Di Sicurezza

Prima della pulizia reale deve esistere un backup recente e verificabile.

Sul BMAX, prima di cancellare dati test:

```bash
cd ~/gestionale-b3d
scripts/bmax_backup.sh
EXTERNAL_BACKUP_DIR=/mnt/backup/b3d_backups scripts/bmax_copy_latest_backup.sh
```

## Anteprima

Eseguire prima sempre l'anteprima:

```bash
docker compose exec web python manage.py prepare_real_use
```

Il comando mostra:

- clienti test riconosciuti;
- preventivi test riconosciuti;
- commesse collegate a test;
- documenti generati da test;
- materiali demo non usati da preventivi reali;
- stampanti demo non usate da preventivi reali.

In anteprima non viene cancellato nulla.

## Pulizia Reale

Se l'elenco e corretto e il backup e stato creato, eseguire:

```bash
docker compose exec web python manage.py prepare_real_use --apply --confirm "PULISCI DATI TEST"
```

La frase di conferma e obbligatoria per evitare cancellazioni involontarie.

## Dopo La Pulizia

Aprire dal browser:

```text
http://b3d-gestionale.local:8000
```

Controllare:

- dashboard;
- clienti;
- preventivi;
- commesse;
- documenti.

Il risultato atteso e un ambiente leggibile: niente dati prova nelle liste operative, dati documento ancora presenti, template ancora disponibili, backup recente conservato.

## Cosa Non Fa

La procedura non svuota tutto il gestionale e non inizializza da zero il database.

Non elimina template documento, dati aziendali documento, configurazione server, utenti admin o backup.

## Dati Riconosciuti Come Test

La pulizia riconosce solo dati con marcatori espliciti, per esempio:

- nomi o testi con `demo`;
- cliente `TEST PDF BMAX - eliminabile`;
- email di prova come `example.com` o `example.local`;
- preventivo demo `B3D-2026-001`;
- record creati dai comandi `seed_demo_data` e `verify_pdf_export`.

Se un cliente con nome demo ha anche un preventivo reale collegato, il comando non lo elimina.
