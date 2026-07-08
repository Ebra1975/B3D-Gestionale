# Board Sprint 13 - Validazione Template E Prova Documento Reale

## Obiettivo

Rendere piu sicuro il caricamento dei template DOCX e verificare il flusso documento su un preventivo realistico.

## Problema Pratico Risolto

Un file Word puo avere estensione `.docx` ma non essere leggibile dal gestionale, oppure puo contenere segnaposto scritti male.

Questo sprint evita di scoprire il problema solo quando si prova a generare una proposta cliente.

## Incluso Nello Sprint

- Controllo reale del file DOCX al caricamento.
- Rifiuto dei file `.docx` rinominati ma non validi.
- Controllo dei segnaposto principali per template consulenza e interno.
- Messaggio operativo nella pagina template.
- Test automatico su preventivo realistico con documento cliente e scheda interna.
- Verifica che il documento cliente non esponga costi interni.
- Verifica che la scheda interna mantenga dettaglio costi, margine e nota interna.

## Non Incluso

- Editor visuale dei template Word.
- Anteprima PDF direttamente dalla pagina template.
- Elenco guidato di tutti i segnaposto disponibili nell'interfaccia.
- Validazione avanzata del layout grafico del DOCX/PDF.

## Stato

Chiuso.

## Verifiche Di Chiusura

- Controllo Django completato.
- Test automatici del modulo documenti completati.
- Prova documento realistico coperta da test automatico.
- Documentazione allineata.
