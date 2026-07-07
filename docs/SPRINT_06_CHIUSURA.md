# Chiusura Sprint 06

## Obiettivo

Rendere la dashboard un punto di controllo quotidiano, non solo un riepilogo numerico.

## Risultato

La dashboard ora mostra un blocco **Da seguire** con:

- preventivi aperti in scadenza entro 14 giorni o gia scaduti;
- commesse attive con consegna prevista entro 14 giorni o gia superata;
- accordi cliente e documenti commerciali in scadenza entro 30 giorni o gia scaduti.

## Funzioni Consegnate

- Conteggio lavori pronti nella dashboard.
- Promemoria operativi con link diretti a preventivi, commesse, accordi e documenti commerciali.
- Evidenza delle date gia superate.
- Test automatico per verificare la presenza dei promemoria principali.
- Aggiornamento documentazione di progetto.

## Decisione Di Prodotto

La dashboard diventa la prima schermata da aprire a inizio lavoro per capire cosa seguire.

Per ora le soglie sono fisse e semplici:

- 14 giorni per preventivi e commesse;
- 30 giorni per accordi e documenti commerciali cliente.

## Verifiche

- Controllo Django con `manage.py check`: completato.
- Test automatico `apps.core`: completato.
- Apertura dashboard da browser locale con risposta HTTP 200: completata.

## Da Riprendere In Futuro

- Notifiche automatiche.
- Calendario operativo.
- Soglie configurabili.
- Eventuale aggiornamento automatico dello stato dei preventivi scaduti.
