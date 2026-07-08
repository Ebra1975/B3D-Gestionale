# Sprint 14 - Chiusura

## Titolo

Template fornitura/artigiano preparatorio.

## Obiettivo Raggiunto

Il gestionale ora puo generare una bozza di preventivo fornitura/artigiano dal dettaglio preventivo.

La funzione e preparatoria: non sostituisce il profilo consulenza, non cambia i calcoli interni e non rende definitive le diciture fiscali o commerciali.

## Cosa E Stato Implementato

- Nuovo template base DOCX `preventivo_fornitura_base_v1.docx`, generato automaticamente se manca un template attivo.
- Nuovo contesto documento `fornitura`, con riepilogo cliente, specifiche tecniche, voci visibili per fornitura e totale.
- Nuova azione nel dettaglio preventivo: `Genera fornitura bozza`.
- Nuova generazione documento di tipo `Fornitura / artigiano`.
- Validazione segnaposto per template DOCX fornitura/artigiano caricati dalla sezione Documenti.
- Numerazione robusta delle versioni generate: una seconda generazione produce `v2`, non un errore.
- Link PDF aperti in una nuova scheda del browser, lasciando il gestionale aperto.
- Guida ai campi e alle variabili dei template DOCX nel manuale operativo e nella pagina Manuale del gestionale.
- Tabelle economiche dei template base impostate con righe ripetute per migliorare la resa in Word/PDF.
- Test automatici dedicati alla generazione fornitura/artigiano.

## Scelte Di Prodotto Confermate

- Il profilo principale verso cliente resta consulenza.
- Il documento fornitura/artigiano resta preparatorio.
- I dati economici restano unici: il documento legge le voci del preventivo, non crea un secondo calcolo.
- Le diciture fiscali/commerciali restano da validare con commercialista prima dell'uso reale.
- I template personalizzati restano il modo corretto per rifinire layout e impaginazione senza modificare i dati sorgente.

## Verifiche

- `python manage.py test apps.documents apps.estimates`
- `python manage.py check`
- Controllo browser locale di `/preventivi/1/`, `/documenti/` e `/manuale/`.

## Prossimo Passo Consigliato

Rifinire in Word un template fornitura/artigiano personalizzato partendo dal template base corretto, poi ricaricarlo dalla sezione Documenti e generare una nuova prova PDF.
