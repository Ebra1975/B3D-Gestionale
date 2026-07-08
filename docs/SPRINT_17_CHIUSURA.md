# Chiusura Sprint 17 - Import dati tecnici da file G-code/3MF

## Risultato

Sprint chiuso con una prima versione operativa dell'import tecnico da slicer.

Dal dettaglio preventivo, dentro ogni configurazione, si puo caricare un file `.gcode`, `.gco` o `.3mf`. Il gestionale prova a leggere:

- peso materiale;
- tempo macchina;
- numero piatti, quando presente.

I valori riconosciuti aggiornano i campi tecnici della configurazione e vengono annotati nelle note interne con il nome del file importato.

## Scelta di prodotto

L'import non genera automaticamente i costi e non cambia il prezzo finale. Serve prima a compilare i dati tecnici; poi l'operatore decide se usare **Genera costo materiale**, **Genera costo macchina** e **Applica prezzo**.

Questa scelta evita automatismi nascosti e mantiene sempre controllabile il dettaglio economico interno.

## Controlli eseguiti

- Controllo generale Django completato senza errori.
- Test automatici mirati su preventivi e parser G-code/3MF completati.
- Suite completa dei test Django completata.
- Dettaglio preventivo locale verificato: pulsante **Importa G-code/3MF** e campi **Peso per unita** / **Ore per unita** presenti.

## Note operative

Il parser copre i metadati piu comuni, ma i diversi slicer possono scrivere i dati in formati differenti. Se un file viene letto ma non contiene dati riconosciuti, la configurazione resta invariata e viene mostrato un avviso.

L'archiviazione del file originale e la preview grafica restano evoluzioni future.

## Documentazione controllata

- `docs/DECISIONI.md`
- `docs/APPROVAZIONI.md`
- `docs/BOARD_SPRINT_17.md`
- `docs/MANUALE_OPERATIVO.md`
- `docs/SCHERMATE_E_FLUSSI.md`
