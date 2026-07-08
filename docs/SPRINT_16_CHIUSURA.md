# Chiusura Sprint 16 - Parametri economici stampanti/materiali

## Risultato

Sprint chiuso con una prima versione dei parametri economici per materiali e stampanti.

Il gestionale ora permette di registrare negli archivi i valori che spiegano il costo usato nei preventivi:

- per i materiali, costo base e scarto/extra;
- per le stampanti, costo base, manutenzione, energia e rischio fallimento.

Quando si genera un costo automatico dal dettaglio preventivo, la voce interna usa questi parametri e conserva una nota con il riepilogo del calcolo.

## Controlli eseguiti

- Controllo generale Django completato senza errori.
- Test automatici su archivi e preventivi completati.
- Migrazione database locale applicata.

## Note operative

I preventivi gia esistenti non vengono ricalcolati automaticamente. Per aggiornare una configurazione aperta, rigenerare la voce materiale o macchina dal dettaglio preventivo.

Il calcolo resta volutamente semplice: l'ammortamento completo della stampante puo essere progettato in seguito senza bloccare l'uso quotidiano.
