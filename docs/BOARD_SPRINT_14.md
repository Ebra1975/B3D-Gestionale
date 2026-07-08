# Board Sprint 14 - Template Fornitura/Artigiano Preparatorio

## Obiettivo

Predisporre una prima generazione documento per il profilo futuro fornitura/artigiano, senza cambiare il profilo principale attuale di consulenza.

## Problema Pratico Risolto

Il gestionale deve poter presentare lo stesso preventivo in piu modi, ma oggi il flusso operativo usa soprattutto la consulenza.

Questo sprint prepara una bozza fornitura/artigiano usando gli stessi dati del preventivo, cosi non si creano copie o calcoli separati.

## Incluso Nello Sprint

- Template DOCX base per preventivo fornitura/artigiano.
- Generazione dal dettaglio preventivo con pulsante dedicato "Genera fornitura bozza".
- Uso delle voci di costo marcate come visibili per fornitura/artigiano.
- Segnalazione nel documento che la dicitura commerciale/fiscale e da validare con commercialista.
- Validazione dei segnaposto anche per template fornitura/artigiano caricati dall'interfaccia.
- Numerazione robusta delle versioni documento anche dopo generazioni ripetute.
- Apertura dei PDF in nuova scheda del browser.
- Guida operativa ai campi e variabili dei template DOCX nel manuale.
- Tabelle economiche dei template base preparate con righe ripetute Word/docxtpl.
- Test automatico su generazione documento fornitura/artigiano.

## Non Incluso

- Uso del profilo fornitura/artigiano come profilo principale verso cliente.
- Revisione fiscale definitiva delle diciture.
- Layout grafico definitivo di brand.
- Regole commerciali specifiche per produzione artigianale o listini futuri.

## Stato

Chiuso.

## Verifiche Di Chiusura

- Controllo Django completato.
- Test automatici del modulo documenti completati.
- Test automatici del modulo preventivi completati.
- Pagine locali Documenti, Preventivi e Manuale controllate dal browser.
- Documentazione allineata.
