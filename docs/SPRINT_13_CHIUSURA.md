# Chiusura Sprint 13

## Titolo

Validazione template e prova documento reale.

## Obiettivo

Ridurre il rischio di usare template Word non validi e confermare la generazione documento su un caso simile a un lavoro reale.

## Risultato

Il caricamento template ora controlla:

- che il file sia davvero un DOCX leggibile;
- che i template consulenza e interno non contengano segnaposto principali sconosciuti;
- che un file rinominato `.docx` ma non valido venga bloccato.

La pagina di caricamento template informa l'operatore che il gestionale esegue questi controlli al salvataggio.

E stata aggiunta una prova automatica con preventivo realistico: cliente, referente, materiale, processo, setup, tempo macchina, margine, proposta cliente e scheda interna.

## Decisione Di Prodotto

La validazione template diventa parte del flusso operativo di caricamento, senza introdurre un nuovo modello dati.

La proposta cliente resta sintetica e non mostra costi interni. La scheda interna resta il documento di controllo economico completo.

## Verifiche

- Controllo Django con `manage.py check`: completato.
- Test automatici `apps.documents`: completati, 11 test.
- Test rifiuto file `.docx` non valido: completato.
- Test rifiuto segnaposto sconosciuto su template consulenza: completato.
- Test generazione documento cliente e interno da preventivo realistico: completato.
- Controllo separazione dati cliente/interno: completato.

## Documentazione Aggiornata

- `docs/DECISIONI.md`
- `docs/APPROVAZIONI.md`
- `docs/REQUISITI_MVP.md`
- `docs/SCHERMATE_E_FLUSSI.md`
- `docs/MANUALE_OPERATIVO.md`
- `docs/BOARD_SPRINT_13.md`

## Prossimo Sprint Proposto

**Sprint 14 - Guida segnaposto e prova PDF visuale**

Obiettivo pratico: mostrare all'operatore quali segnaposto puo usare nei template e rendere piu semplice controllare il risultato PDF prima dell'invio.

## Da Riprendere In Futuro

- Anteprima PDF direttamente dalla pagina template.
- Elenco segnaposto disponibile in interfaccia.
- Validazione visuale di impaginazione e tabelle.
- Template fornitura/artigiano.
- Layout definitivo con logo reale.
