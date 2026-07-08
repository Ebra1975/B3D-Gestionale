# Chiusura Sprint 18 - Backup automatico e prova ripristino BMAX

## Risultato

Sprint chiuso con una prima procedura automatizzabile per i backup del BMAX e una prova di ripristino sicura.

Il backup automatico crea un archivio completo e datato con database PostgreSQL, file media, configurazione `.env`, manifesto e checksum. La prova di ripristino usa contenitori Docker temporanei, cosi non modifica i dati reali del gestionale.

## Scelta di prodotto

Il backup BMAX viene gestito come operazione di sistema, non come pulsante dentro il gestionale. In questa fase e la scelta piu semplice e robusta: il backup deve funzionare anche se l'interfaccia web non e raggiungibile.

## Controlli eseguiti

- Sintassi degli script shell verificata.
- Controllo generale Django completato.
- Documentazione operativa aggiornata.

## Note operative

Prima di affidare dati reali al gestionale, sul BMAX va eseguita almeno una prova:

```bash
scripts/bmax_backup.sh
scripts/bmax_restore_test.sh backups/bmax/NOME_BACKUP.tar.gz
```

Poi va controllato che il gestionale reale continui ad aprirsi normalmente.

## Documentazione controllata

- `docs/BACKUP_E_RIPRISTINO.md`
- `docs/PROCEDURA_MANUTENZIONE.md`
- `docs/DECISIONI.md`
- `docs/APPROVAZIONI.md`
- `docs/BOARD_SPRINT_18.md`
