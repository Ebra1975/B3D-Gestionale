# Requisiti MVP

## Scopo Della Prima Versione

La prima versione deve permettere di gestire il ciclo base di un lavoro: cliente, preventivo, configurazioni tecniche, costi interni, proposta cliente e stato della commessa.

Deve essere utile anche se usata da una sola persona.

## Funzioni Incluse

### Clienti

- Creazione cliente.
- Dati anagrafici essenziali.
- Contatti.
- Note.
- Storico preventivi e lavori.

### Preventivi

- Creazione preventivo.
- Oggetto del lavoro.
- Quantita.
- Descrizione tecnica.
- Validita offerta.
- Stato del preventivo.
- Una o piu configurazioni/opzioni.

### Configurazioni Tecniche

Ogni preventivo deve poter contenere piu configurazioni, ad esempio:

- PETG con trattamento UV;
- PETG standard;
- ASA ad alta resistenza UV;
- variante con macchina del cliente.

Per ogni configurazione servono:

- nome;
- descrizione;
- durata attesa;
- materiale;
- processo;
- modalita operativa;
- quantita;
- totale;
- prezzo unitario;
- note tecniche.

### Costi Interni

Ogni configurazione deve avere voci di costo interne, ad esempio:

- materiali;
- ore macchina;
- elettricita;
- progettazione;
- setup;
- manodopera;
- trasferte;
- post-processing;
- verniciatura;
- margine;
- altri costi.

Queste voci restano visibili internamente anche quando il documento cliente e sintetico.

### Profili Documento

Il preventivo deve poter essere esportato o visualizzato in tre modalita:

- interno dettagliato;
- consulenza;
- fornitura/artigiano.

### Prototipo

Il sistema deve prevedere una fase preliminare di prototipo:

- descrizione;
- materiale;
- costo interno;
- compenso/prezzo;
- note;
- stato di validazione.

### Commesse

Quando un preventivo viene accettato, deve poter diventare commessa.

Stati minimi:

- da fare;
- in progettazione;
- in stampa;
- in post-processing;
- pronto;
- consegnato;
- annullato.

### Dashboard

La dashboard iniziale deve mostrare:

- lavori in corso;
- preventivi aperti;
- lavori pronti;
- scadenze principali;
- riepilogo economico essenziale.

### Documenti E PDF

Il sistema deve generare documenti coerenti con il profilo documento scelto.

La direzione scelta e usare template caricabili in formato `.docx`.

Da un template il sistema deve poter generare:

- documento `.docx` compilato;
- PDF pronto da inviare.

I documenti devono avere:

- intestazione B3D Lab;
- cliente;
- oggetto;
- data;
- validita;
- configurazioni;
- totale;
- condizioni generali.

La proposta cliente deve restare sintetica e non mostrare costi interni o margine.

La scheda interna deve mostrare il dettaglio economico completo, incluse voci di costo, margine e controlli.

Ogni documento generato deve essere versionato e archiviato.

I dati documento riutilizzati nei DOCX/PDF devono essere modificabili da interfaccia operativa, almeno per:

- intestazione azienda;
- contatti;
- logo;
- condizioni standard;
- nota fiscale/commerciale;
- nota interna.

I template DOCX devono essere gestibili da interfaccia operativa, almeno per:

- caricare un nuovo file `.docx`;
- modificare nome, tipo documento, profilo, versione e note;
- attivare o disattivare un template;
- scaricare il file template caricato;
- mantenere un solo template attivo per tipo documento.

Il controllo automatico dei segnaposto interni al DOCX puo restare fuori dalla prima versione, ma il sistema deve almeno impedire il caricamento di file non `.docx`.

Dallo Sprint 13 il sistema controlla anche che il file caricato sia un DOCX realmente leggibile e, per i template consulenza e interno, che i segnaposto principali siano compatibili con i dati disponibili.

Dallo Sprint 14 e disponibile anche un template base preparatorio per fornitura/artigiano. Questo profilo usa gli stessi dati del preventivo e resta da validare commercialmente/fiscalmente prima dell'uso reale verso cliente.

## Fuori Dalla Prima Versione

Non sono necessari nella prima versione:

- fatturazione elettronica completa;
- gestione multiutente completa;
- pagamento online;
- app mobile nativa;
- integrazione automatica con stampanti;
- marketplace;
- gestione licenze.
- AI generativa avanzata;
- listini cliente completi;
- accordi commerciali completi.

Queste funzioni restano pero parte della visione futura e non devono essere rese impossibili dalle scelte iniziali.

## Criterio Di Successo

La prima versione e riuscita se permette di creare un preventivo reale, vedere i costi interni, scegliere il profilo consulenza e generare una proposta cliente professionale da template `.docx`, con output `.docx` e PDF.
