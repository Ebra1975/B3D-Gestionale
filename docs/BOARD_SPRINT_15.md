# Board Sprint 15 - Numerazione Automatica Preventivi

## Obiettivo

Evitare che il numero preventivo venga scritto a mano a ogni nuova proposta.

## Problema Pratico Risolto

Ogni preventivo deve avere un riferimento stabile da usare con cliente, documenti generati, ricerche e commesse.

Prima di questo sprint il numero era obbligatorio e manuale: l'operatore doveva ricordare l'ultimo progressivo e rischiava duplicati o formati incoerenti.

## Incluso Nello Sprint

- Numero preventivo generato automaticamente quando il campo viene lasciato vuoto.
- Formato progressivo `B3D-ANNO-NNN`, ad esempio `B3D-2026-001`.
- Ricerca del prossimo numero disponibile nello stesso anno.
- Campo numero ancora modificabile per casi controllati o dati importati.
- Validazione del formato del numero preventivo.
- Migrazione database per rendere il campo numero non obbligatorio in inserimento.
- Test automatici sulla generazione del primo numero e del progressivo successivo.
- Manuale operativo aggiornato con il nuovo gesto pratico.
- Decisioni e approvazioni aggiornate.

## Non Incluso

- Configurazione da interfaccia del prefisso `B3D`.
- Serie numeriche diverse per consulenza e fornitura/artigiano.
- Blocco avanzato della modifica manuale dopo l'emissione.
- Gestione multiutente concorrente avanzata, rimandata alla futura evoluzione SaaS.

## Stato

Chiuso.

## Verifiche Di Chiusura

- Controllo Django completato.
- Test automatici del modulo preventivi completati.
- Test automatici completi del progetto completati.
- Migrazione applicata al database locale.
- Documentazione allineata.
