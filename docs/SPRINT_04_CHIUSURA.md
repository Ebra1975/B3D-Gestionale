# Chiusura Sprint 04

## Obiettivo

Avviare la memoria commerciale cliente senza introdurre automatismi sui prezzi.

## Risultato

Lo Sprint 04 aggiunge una scheda cliente piu completa e due nuovi archivi collegati:

- accordi cliente;
- documenti commerciali cliente.

La scheda cliente ora permette di vedere dati anagrafici, note, accordi, documenti commerciali, preventivi recenti e commesse recenti.

## Funzioni Consegnate

- Dettaglio cliente raggiungibile dalla lista clienti.
- Creazione e modifica accordi cliente.
- Creazione e modifica documenti commerciali cliente con file allegato opzionale.
- Visualizzazione di accordi e documenti commerciali nella scheda cliente.
- Gestione dei nuovi archivi anche dal pannello admin.
- Documentazione aggiornata in board, decisioni, approvazioni, manuale operativo, modello dati, schermate/flussi e documento listini/accordi.

## Decisione Di Prodotto

Gli accordi cliente sono memoria commerciale, non regole automatiche di prezzo.

Per ora il titolare deve controllare accordi e documenti nella scheda cliente prima di preparare un preventivo. L'applicazione automatica di listini, sconti o maggiorazioni resta una fase successiva.

## Verifiche

- `python manage.py check`: positivo.
- Migrazione clienti Sprint 04 applicata: positivo.
- Controllo migrazioni residue: nessuna modifica rilevata.
- Compilazione Python `config` e `apps`: positiva.
- Lista clienti, scheda cliente, form accordo e form documento commerciale: risposte HTTP 200.
- Creazione/cancellazione dati prova per accordo e documento commerciale: positiva.

## Da Riprendere In Futuro

- Upload e apertura file allegato reale da browser.
- Avvisi su documenti o accordi in scadenza.
- Listino strutturato con voci prezzo.
- Applicazione assistita, non automatica, delle condizioni cliente al preventivo.
- Backup automatico BMAX.
