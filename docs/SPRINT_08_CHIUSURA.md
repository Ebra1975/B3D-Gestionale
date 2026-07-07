# Chiusura Sprint 08

## Titolo

Prezzo assistito e condizioni cliente.

## Obiettivo

Rendere piu guidata la revisione economica del preventivo usando la memoria commerciale del cliente.

Il problema pratico era evitare che accordi, listini collegati, NDA o condizioni commerciali restassero solo come promemoria mentale mentre si conferma il prezzo finale.

## Risultato

Il dettaglio preventivo ora permette di registrare una **revisione condizioni cliente** con:

- data e ora del controllo;
- note interne sul controllo effettuato;
- avviso nello stato preventivo se esiste memoria commerciale cliente ma il controllo non e ancora stato confermato;
- mantenimento della decisione economica in capo al titolare.

## Funzioni Consegnate

- Conferma manuale del controllo condizioni cliente dal dettaglio preventivo.
- Salvataggio di data e note interne sul preventivo.
- Avviso operativo prima della proposta quando il cliente ha accordi o documenti commerciali da controllare.
- Test automatici mirati sulla memoria commerciale e sulla conferma condizioni.
- Aggiornamento documentazione di progetto.
- Comparazione con Stimalo e PreventiPiraz 3D come benchmark per i prossimi sprint.

## Decisione Di Prodotto

Gli accordi cliente, i listini collegati e i documenti commerciali restano strumenti di supporto alla revisione.

Il gestionale non modifica automaticamente prezzo, margine o condizioni: aiuta a ricordare il controllo e a lasciarne traccia.

## Verifiche

- Controllo Django con `manage.py check`: completato.
- Test automatici `apps.estimates`: completati.
- Migrazione database locale: completata.
- Apertura dettaglio preventivo dal server locale: completata.

## Benchmark

Durante lo sprint e stata aggiunta una comparazione con:

- Stimalo;
- PreventiPiraz 3D.

La comparazione evidenzia che:

- PreventiPiraz 3D e un riferimento forte per calcolo rapido da file e slicer;
- Stimalo e un riferimento forte per gestione web, cataloghi, inventario e strategie prezzo;
- B3D Lab deve mantenere il proprio focus su consulenza, memoria commerciale, documenti personalizzati e controllo locale dei dati.

## Da Riprendere In Futuro

- Prova reale di un preventivo completo.
- Import o registrazione piu rapida dei dati tecnici da file/slicer.
- Cataloghi iniziali piu pronti per materiali e stampanti.
- Strategie prezzo piu ricche ma sempre confermate manualmente.
- Documento operativo interno da commessa.
