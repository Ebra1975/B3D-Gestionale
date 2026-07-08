# Chiusura Sprint 11

## Titolo

Rifinitura layout PDF cliente/interno.

## Obiettivo

Rendere piu leggibili e controllabili i documenti generati dal gestionale:

- proposta cliente consulenza;
- scheda interna dettagliata.

Il problema pratico era avere PDF/DOCX piu adatti al flusso reale, senza cambiare i dati economici e senza esporre al cliente il dettaglio interno.

## Risultato

Il template cliente consulenza e stato aggiornato alla versione base v3.

La proposta cliente ora mette meglio in evidenza:

- intestazione B3D Lab;
- contatti azienda;
- dati essenziali cliente/preventivo;
- oggetto;
- contesto e richiesta;
- soluzione tecnica;
- sintesi economica cliente;
- nota fiscale/commerciale da validare con commercialista.

Il template interno dettagliato e stato aggiornato alla versione base v2.

La scheda interna ora mette meglio in evidenza:

- riepilogo preventivo e cliente;
- costo interno;
- margine;
- margine percentuale;
- totale proposta;
- voci di costo con note;
- ipotesi operative;
- note interne;
- controlli documento.

## Decisione Di Prodotto

La rifinitura non cambia modello dati, architettura o calcolo economico.

Proposta cliente e scheda interna continuano a usare gli stessi dati del preventivo e della configurazione scelta, ma li presentano in modo diverso.

Il dettaglio costi resta interno e non deve comparire nel documento cliente.

## Verifiche

- Controllo Django con `manage.py check`: completato.
- Test automatici `apps.documents`: completati, 4 test.
- Controllo automatico che la proposta cliente non contenga etichette interne come costo interno, margine percentuale e voci di costo: completato.
- Controllo documentazione: completato.

## Documentazione Aggiornata

- `docs/DECISIONI.md`
- `docs/APPROVAZIONI.md`
- `docs/SCHERMATE_E_FLUSSI.md`
- `docs/MANUALE_OPERATIVO.md`
- `docs/BOARD_SPRINT_11.md`

## Prossimo Sprint Proposto

**Sprint 12 - Gestione template DOCX da interfaccia**

Obiettivo pratico: permettere di caricare, sostituire o disattivare i template DOCX dalla sezione Documenti, senza usare l'admin tecnico.

## Da Riprendere In Futuro

- Layout definitivo di brand con logo reale.
- Validazione del PDF su esempi reali da inviare a clienti.
- Template fornitura/artigiano.
- Eventuale anteprima PDF direttamente nel gestionale.
