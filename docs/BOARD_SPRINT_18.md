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

## Verifiche

- Controllo sintassi degli script shell.
- Controllo generale Django.
- Documentazione aggiornata per uso non tecnico.

## Rimandato

- Notifica automatica dell'esito backup.
- Copia automatica fuori dal BMAX su NAS o disco esterno.
- Indicatore backup recente nella dashboard del gestionale.
- Prova reale sul BMAX, da eseguire quando il server sara disponibile.
