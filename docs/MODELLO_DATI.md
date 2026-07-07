# Modello Dati

## Scopo

Questo documento descrive le informazioni principali che il gestionale deve conservare.

Non e un documento tecnico definitivo: serve come mappa comprensibile dei dati.

## Cliente

Campi iniziali:

- nome;
- tipo cliente;
- referente;
- email;
- telefono;
- indirizzo;
- codice fiscale o partita IVA;
- note;
- data creazione.

## Preventivo

Campi iniziali:

- numero preventivo;
- cliente;
- oggetto;
- descrizione;
- data;
- validita;
- stato;
- quantita generale;
- profilo documento preferito;
- condizioni generali;
- note interne.

Stati possibili:

- bozza;
- inviato;
- da rivedere;
- accettato;
- rifiutato;
- scaduto;
- annullato.

## Configurazione Tecnica

Una configurazione appartiene a un preventivo.

Campi iniziali:

- nome;
- descrizione;
- materiale;
- processo;
- stampante o strumentazione;
- trattamento;
- durata attesa;
- modalita operativa;
- quantita;
- peso materiale per unita;
- tempo macchina per unita;
- totale;
- prezzo unitario;
- note pubbliche;
- note interne.

## Voce Di Costo

Una voce di costo appartiene a una configurazione.

Campi iniziali:

- categoria;
- descrizione;
- quantita;
- unita;
- costo unitario;
- totale;
- visibile nel modello interno;
- visibile nel modello consulenza;
- visibile nel modello fornitura/artigiano.

Categorie iniziali:

- materiale;
- tempo macchina;
- elettricita;
- progettazione;
- setup;
- manodopera;
- trasferta;
- post-processing;
- trattamento;
- margine;
- altro.

## Prototipo

Campi iniziali:

- preventivo;
- descrizione;
- materiale;
- costo interno;
- compenso/prezzo;
- stato;
- note;
- data validazione.

Stati possibili:

- non previsto;
- proposto;
- approvato;
- realizzato;
- validato;
- da modificare.

## Commessa

Una commessa nasce da un preventivo accettato.

Campi iniziali:

- numero commessa;
- preventivo collegato;
- cliente;
- configurazione scelta;
- stato;
- data avvio;
- data prevista consegna;
- data consegna;
- note operative.

Stati possibili:

- da fare;
- in progettazione;
- in stampa;
- in post-processing;
- pronto;
- consegnato;
- sospeso;
- annullato.

## Materiale

Campi iniziali:

- nome;
- tipo;
- marca;
- colore;
- costo al kg o al litro;
- fornitore;
- note tecniche;
- resistenza UV;
- temperatura;
- disponibilita.

## Stampante / Strumentazione

Campi iniziali:

- nome;
- modello;
- proprieta;
- volume di stampa;
- camera chiusa;
- materiali supportati;
- costo orario stimato;
- consumo elettrico stimato;
- note.

## Documento Generato

Campi iniziali:

- preventivo;
- tipo documento;
- data generazione;
- file PDF;
- versione;
- note.

Tipi documento:

- interno dettagliato;
- consulenza;
- fornitura/artigiano.

## Template Documento

Campi iniziali:

- nome;
- tipo documento;
- profilo;
- file template `.docx`;
- versione template;
- attivo;
- data caricamento;
- note.

Profili possibili:

- interno dettagliato;
- consulenza;
- fornitura/artigiano;
- fiscale futuro;
- consegna;
- relazione tecnica.

## File Allegato

Campi iniziali:

- nome file;
- tipo file;
- cliente collegato;
- preventivo collegato;
- commessa collegata;
- file originale;
- preview generata;
- metadati estratti;
- stato elaborazione;
- note.

Tipi file iniziali:

- 3MF;
- G-code;
- STL;
- PDF;
- DOCX;
- immagine;
- altro.

## Listino

Campi futuri:

- nome;
- tipo listino;
- cliente collegato opzionale;
- data inizio validita;
- data fine validita;
- stato;
- note.

Tipi listino:

- base;
- cliente;
- promozionale;
- storico.

## Voce Listino

Campi futuri:

- listino;
- categoria;
- descrizione;
- unita;
- prezzo;
- sconto;
- maggiorazione;
- note.

Categorie possibili:

- progettazione;
- setup;
- tempo macchina;
- materiale;
- post-processing;
- urgenza;
- consulenza;
- altro.

## Accordo Cliente

Campi prima versione:

- cliente;
- nome accordo;
- listino collegato;
- data inizio;
- data fine;
- stato;
- condizioni generali;
- note commerciali.

Stati possibili:

- bozza;
- attivo;
- scaduto;
- sospeso;
- rinnovato;
- chiuso.

## Documento Cliente / Contrattuale

Campi prima versione:

- cliente;
- nome documento;
- tipo documento;
- data emissione;
- data firma;
- data scadenza;
- stato;
- file allegato;
- note.

Tipi possibili:

- NDA;
- accordo commerciale;
- accordo quadro;
- condizioni particolari;
- listino firmato;
- lettera di incarico;
- altro.

Stati possibili:

- bozza;
- inviato;
- firmato;
- attivo;
- scaduto;
- sostituito;
- archiviato.

## Casistica Lavorazione

Campi futuri:

- nome;
- descrizione;
- categoria;
- materiali consigliati;
- stampanti consigliate;
- checklist;
- rischi;
- voci costo consigliate;
- note cliente consigliate;
- margine minimo;
- stato.

## Regola Automazione

Campi futuri:

- nome;
- descrizione;
- evento;
- condizione;
- azione;
- livello automazione;
- attiva;
- note.

Livelli automazione:

- avviso;
- suggerimento;
- azione assistita;
- azione automatica.
