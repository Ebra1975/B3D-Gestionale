# Board Sprint 18 - Backup automatico e prova ripristino BMAX

## Problema pratico

Quando il gestionale sara usato sul BMAX con dati reali, non basta ricordarsi di fare un backup manuale. Serve un salvataggio ripetibile, controllabile e provabile, per ridurre il rischio di perdere clienti, preventivi, commesse, documenti e allegati.

## Fatto

- Aggiunto script `scripts/bmax_backup.sh` per creare backup BMAX completi.
- Il backup include database PostgreSQL, media, `.env`, manifesto e checksum.
- Aggiunta rotazione automatica dei backup vecchi, con valore predefinito di 30 giorni.
- Aggiunto controllo minimo dello spazio libero prima di creare il backup.
- Aggiunto script `scripts/bmax_restore_test.sh` per provare un ripristino su ambiente Docker temporaneo.
- Aggiornata la procedura `docs/BACKUP_E_RIPRISTINO.md` con uso manuale, cron e prova ripristino.
- Installazione reale avviata sul BMAX e raggiungibile da browser.
- Backup manuale creato sul BMAX.
- Prova di ripristino completata sul BMAX.
- Cron giornaliero alle 02:30 configurato.

## Verifiche

- Build e avvio Docker Compose sul BMAX.
- Migrazioni PostgreSQL completate.
- Dashboard e admin Django raggiungibili su `http://192.168.1.143:8000`.
- Backup creato in `backups/bmax/`.
- Prova ripristino completata: 25 tabelle database ripristinate.
- File media ripristinati: 0, atteso per installazione iniziale senza file caricati.

## Rimandato

- Notifica automatica dell'esito backup.
- Copia automatica fuori dal BMAX su NAS o disco esterno.
- Indicatore backup recente nella dashboard del gestionale.
