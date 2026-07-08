# Chiusura Sprint 18 - Backup automatico e prova ripristino BMAX

## Risultato

Sprint chiuso con installazione reale sul BMAX, backup automatico pronto e prova di ripristino completata.

Il gestionale e raggiungibile in rete locale all'indirizzo:

```text
http://192.168.1.143:8000
```

Il backup crea un archivio completo e datato con database PostgreSQL, file media, configurazione `.env`, manifesto e checksum. La prova di ripristino usa contenitori Docker temporanei, cosi non modifica i dati reali del gestionale.

## Scelta di prodotto

Il backup BMAX viene gestito come operazione di sistema, non come pulsante dentro il gestionale. In questa fase e la scelta piu semplice e robusta: il backup deve funzionare anche se l'interfaccia web non e raggiungibile.

## Controlli eseguiti

- Build Docker Compose completata sul BMAX.
- Servizi `web`, `db`, `redis`, `worker` e `beat` avviati.
- Migrazioni PostgreSQL completate.
- Utente amministratore creato.
- Dashboard e admin Django raggiungibili da browser.
- Backup manuale creato con `scripts/bmax_backup.sh`.
- Prova di ripristino completata con `scripts/bmax_restore_test.sh`.
- Ripristino confermato: 25 tabelle database ripristinate.
- File media ripristinati: 0, valore corretto per installazione iniziale senza allegati o documenti caricati.
- Cron giornaliero alle 02:30 configurato per il backup automatico.

## Note operative

La prova obbligatoria di ripristino e stata eseguita sul BMAX. Per i prossimi controlli periodici:

```bash
cd ~/gestionale-b3d
ls -lh backups/bmax
tail -n 30 backups/bmax/backup.log
```

Il cron configurato crea un backup ogni giorno alle 02:30. Il controllo settimanale deve verificare che esistano archivi recenti e che il log riporti `Backup creato`.

## Documentazione controllata

- `docs/BACKUP_E_RIPRISTINO.md`
- `docs/PROCEDURA_MANUTENZIONE.md`
- `docs/DECISIONI.md`
- `docs/APPROVAZIONI.md`
- `docs/BOARD_SPRINT_18.md`
- `docs/INSTALLAZIONE_BMAX_LINUX.md`
