# Istruzioni Progetto

## Contesto

Questo repository contiene il gestionale per B3D Lab, attivita legata a consulenza tecnica, progettazione e manifattura additiva.

L'utente non programma: ogni scelta tecnica deve essere spiegata in modo semplice, con attenzione all'uso pratico del software.

## Obiettivo

Costruire una prima versione locale del gestionale, utilizzata inizialmente da una sola persona su mini PC BMAX con Linux Server.

Il gestionale deve aiutare a gestire clienti, preventivi, commesse, materiali, stampanti, configurazioni tecniche e documenti PDF.

## Regole Di Prodotto

- Il sistema deve mantenere sempre un dettaglio economico interno completo.
- Lo stesso preventivo deve poter essere presentato in piu modalita:
  - interno dettagliato;
  - proposta di consulenza;
  - fornitura/artigiano.
- Per il momento il profilo principale verso cliente e "consulenza".
- La modalita fornitura/artigiano deve restare prevista per uno sviluppo futuro.
- I dati non devono essere duplicati tra i diversi modelli documento.
- Le diciture fiscali e commerciali importanti vanno marcate come "da validare con commercialista" quando necessario.

## Regole Di Lavoro

- Prima di implementare una funzione, chiarire quale problema pratico risolve.
- Preferire schermate semplici, leggibili e adatte all'uso quotidiano.
- Evitare complessita non necessaria nella prima versione.
- Ogni modifica importante deve essere documentata in `docs/DECISIONI.md`.
- Ogni requisito approvato o in dubbio deve essere tracciato in `docs/APPROVAZIONI.md`.
- Non cambiare architettura, tecnologia principale o modello dati senza esplicita approvazione.
- Mantenere separate le responsabilita tra backend, frontend e stile.
- Preferire scelte tecniche diffuse, documentate e comprensibili da sviluppatori esterni.
- Evitare codice troppo personale o difficile da consegnare a terzi.

## Qualita Attesa

- Il gestionale deve funzionare in rete locale da browser.
- Deve essere installabile e manutenibile su Linux Server.
- Deve prevedere backup.
- Deve essere comprensibile da una persona non tecnica.
- Prima di considerare conclusa una funzione, verificare che sia utilizzabile nel flusso reale di lavoro.
