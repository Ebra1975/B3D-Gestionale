# Chiusura Sprint 20 - Pulizia dati test e preparazione uso reale

## Risultato

Sprint chiuso con una procedura controllata per preparare il gestionale all'uso reale dopo le prove BMAX.

Il nuovo comando:

```bash
python manage.py prepare_real_use
```

mostra in anteprima clienti, preventivi, commesse, documenti generati, materiali e stampanti riconosciuti come dati test.

La pulizia reale richiede una conferma esplicita:

```bash
python manage.py prepare_real_use --apply --confirm "PULISCI DATI TEST"
```

## Scelta Di Prodotto

La pulizia non e un reset totale del gestionale.

Il gestionale deve restare pronto per l'uso reale: template documento, dati aziendali documento, utenti, backup e configurazioni restano al loro posto. Si rimuovono solo dati test riconoscibili, con anteprima e conferma.

## Perche Risolve Un Problema Reale

Dopo le prove PDF e BMAX restano record fittizi utili per verificare il sistema, ma per l'uso quotidiano rischiano di sporcare liste, dashboard e documenti.

La nuova procedura permette di:

- vedere prima cosa verra rimosso;
- fare backup prima dell'operazione;
- cancellare solo dati marcati come test;
- consegnare a un collaboratore un ambiente piu leggibile.

## Controlli Eseguiti

- Backup locale creato prima della pulizia: `backups/b3dlab_backup_locale_20260709_111739.zip`.
- Pulizia reale eseguita sull'ambiente locale di sviluppo con conferma esplicita.
- Anteprima finale: 0 clienti test, 0 preventivi test, 0 commesse test, 0 documenti test, 0 materiali demo, 0 stampanti demo.
- Test automatici comando `prepare_real_use`.
- Controllo Django.
- Compilazione moduli Python.
- Documentazione allineata.

## Documentazione Aggiornata

- `docs/PULIZIA_DATI_TEST_USO_REALE.md`
- `docs/BOARD_SPRINT_20.md`
- `docs/MANUALE_OPERATIVO.md`
- `docs/PROCEDURA_MANUTENZIONE.md`
- `docs/DECISIONI.md`
- `docs/APPROVAZIONI.md`
- `README.md`
