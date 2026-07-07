# Chiusura Sprint 07

## Obiettivo

Portare la memoria commerciale cliente nel punto in cui serve di piu: il dettaglio preventivo.

## Risultato

Il dettaglio preventivo ora mostra un riquadro **Memoria commerciale cliente** con:

- ultimi accordi cliente;
- listino collegato, se presente;
- documenti commerciali cliente;
- avvisi per accordi o documenti scaduti o in scadenza entro 30 giorni;
- link diretto alla scheda cliente.

## Funzioni Consegnate

- Riepilogo accordi cliente nel dettaglio preventivo.
- Riepilogo documenti commerciali cliente nel dettaglio preventivo.
- Avvisi commerciali prima della proposta.
- Test automatico sulla memoria commerciale.
- Aggiornamento documentazione di progetto.

## Decisione Di Prodotto

Gli accordi cliente vengono mostrati nel preventivo come promemoria operativo, ma non modificano ancora automaticamente prezzi, margini o condizioni.

Questa scelta mantiene obbligatoria la revisione del titolare fino alla futura progettazione dei listini strutturati.

## Verifiche

- Controllo Django con `manage.py check`: completato.
- Test automatico `apps.estimates`: completato.

## Da Riprendere In Futuro

- Listini base e listini cliente strutturati.
- Regole prezzo collegate ad accordi commerciali.
- Applicazione assistita, non automatica, delle condizioni cliente al preventivo.
- Notifiche automatiche su accordi e documenti in scadenza.
