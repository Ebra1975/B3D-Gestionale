# Chiusura Sprint 10

## Titolo

Modifica dati documento da interfaccia.

## Obiettivo

Rendere modificabili dalla sezione **Documenti** i dati usati per generare DOCX/PDF, senza passare dall'admin tecnico.

Il problema pratico era evitare che intestazione, contatti, condizioni standard e note fiscali/commerciali restassero configurabili solo da una schermata tecnica poco adatta all'uso quotidiano.

## Risultato

La sezione **Documenti** ora include un accesso diretto a **Modifica dati documento**.

Da questa pagina si puo aggiornare il profilo dati attivo con:

- nome profilo;
- nome azienda;
- sottotitolo;
- indirizzo;
- email;
- telefono;
- sito web;
- codice fiscale / partita IVA;
- logo;
- condizioni standard consulenza;
- nota fiscale/commerciale;
- nota interna.

Le modifiche valgono per i prossimi documenti generati. I documenti gia creati restano archiviati come versioni storiche.

## Funzioni Consegnate

- Form operativo per modificare il profilo dati documento attivo.
- Pulsante **Modifica dati documento** nella sezione Documenti.
- Messaggio di conferma dopo il salvataggio.
- Test automatico per verificare la modifica del profilo attivo da interfaccia.
- Manuale operativo aggiornato con la procedura dedicata.
- Decisioni, approvazioni, schermate e flussi aggiornati.

## Decisione Di Prodotto

I dati documento restano centralizzati in un unico profilo attivo.

La generazione di proposta cliente e scheda interna continua a usare gli stessi dati di partenza, evitando duplicazioni tra template e documenti.

## Verifiche

- Controllo Django con `manage.py check`: completato.
- Test automatici `apps.documents`: completati, 3 test.
- Apertura pagina `/documenti/dati-documento/modifica/` dal server locale: completata con risposta 200.

## Prossimo Sprint Proposto

**Sprint 11 - Template documenti e layout PDF**

Obiettivo pratico: rifinire la gestione dei template e il layout dei documenti cliente/interno, partendo dai dati documento ora modificabili da interfaccia.

## Da Riprendere In Futuro

- Caricamento e gestione template DOCX da interfaccia non amministrativa.
- Layout definitivo PDF cliente.
- Layout definitivo scheda interna.
- Logo e impaginazione di brand con esempi reali.
