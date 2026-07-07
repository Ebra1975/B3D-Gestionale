# Sprint 02 - Chiusura

Data chiusura: 2026-07-07

## Obiettivo Dello Sprint

Chiudere il primo flusso reale di preventivo consulenza, dalla gestione dei dati interni alla generazione del documento cliente `.docx` e PDF.

Lo sprint ha avuto anche lo scopo di rendere il flusso piu usabile nella pratica quotidiana, aggiungendo stato operativo del preventivo, dati demo realistici, manuale operativo, ricerca nelle liste e primo collegamento verso le commesse.

## Risultato Sintetico

Obiettivo raggiunto.

Il gestionale ora permette di:

- creare o aprire un preventivo;
- collegare cliente e configurazione tecnica;
- mantenere costi interni completi;
- generare proposta consulenza `.docx`;
- generare PDF tramite LibreOffice;
- controllare cosa manca prima della proposta;
- segnare il preventivo come inviato, da rivedere, accettato o rifiutato;
- creare una commessa da un preventivo accettato;
- distinguere i preventivi ancora da lavorare da quelli gia convertiti in commessa.

## Funzioni Implementate

### Documenti Consulenza

- Generazione DOCX consulenza dal dettaglio preventivo.
- Creazione automatica di un template DOCX base se non esiste un template caricato.
- Conversione PDF tramite LibreOffice headless.
- Uso di `soffice.com` su Windows per conversioni affidabili da terminale.
- Collegamento dei documenti generati alla sezione Documenti e al dettaglio preventivo.

### Dettaglio Preventivo

- Riquadro **Stato preventivo** con:
  - configurazione usata;
  - totale proposta;
  - prezzo unitario;
  - ultimo documento generato;
  - elementi mancanti;
  - avvisi da controllare.
- Azioni rapide per cambiare stato:
  - Inviato;
  - Da rivedere;
  - Accettato;
  - Rifiutato.

### Dati Demo

- Aggiunto comando:

```text
python manage.py seed_demo_data --with-documents
```

- Creato preventivo demo realistico:

```text
B3D-2026-001 - Supporti tecnici personalizzati per attrezzatura
```

- Il caso demo genera DOCX/PDF e puo essere trasformato in commessa.

### Commesse

- Creazione commessa da preventivo accettato.
- Collegamento commessa a:
  - preventivo;
  - cliente;
  - configurazione scelta.
- Numero commessa generato automaticamente con formato `COM-2026-001`.
- Lista commesse aggiornata con collegamento al preventivo.

### Ricerca E Filtri

- Lista Preventivi:
  - ricerca per numero, cliente, oggetto e descrizione;
  - filtro Da lavorare;
  - filtro Convertiti in commessa;
  - filtro Tutti;
  - righe attenuate per preventivi gia convertiti in commessa.
- Lista Commesse:
  - ricerca per numero commessa, cliente, preventivo, oggetto e configurazione;
  - filtro per stato.

### Manuale Operativo

- Creato `docs/MANUALE_OPERATIVO.md`.
- Aggiunta pagina **Manuale** nella sidebar del gestionale.
- Prime procedure documentate:
  - fare un preventivo consulenza;
  - usare il preventivo demo;
  - creare una commessa da preventivo accettato.

### Interfaccia

- Sidebar fissa su desktop durante lo scorrimento delle pagine lunghe.
- Prima organizzazione operativa della pagina dettaglio preventivo.

### Versionamento

- Repository Git locale inizializzato.
- Primo punto stabile salvato.
- Commit successivi creati per ogni blocco funzionale rilevante.

## Verifiche Eseguite

- `python manage.py check` con esito positivo.
- Compilazione Python di `config` e `apps` con esito positivo.
- Generazione DOCX consulenza verificata.
- Conversione PDF verificata con LibreOffice su Windows.
- Creazione preventivo demo verificata.
- Creazione commessa da preventivo accettato verificata.
- Ricerca e filtri su preventivi e commesse verificati con test interno Django.
- Git verificato pulito prima della chiusura documentale.

## Documentazione Allineata

In chiusura sprint sono stati controllati e aggiornati:

- `docs/DECISIONI.md`;
- `docs/APPROVAZIONI.md`;
- `docs/SCHERMATE_E_FLUSSI.md`;
- `docs/MANUALE_OPERATIVO.md`;
- `docs/BOARD_SPRINT_02.md`.

Questa verifica e ora parte esplicita della procedura di chiusura sprint.

## Decisioni Consolidate Nello Sprint

- Il primo documento cliente e il profilo consulenza.
- La generazione DOCX/PDF puo avvenire in modo sincrono nella prima versione locale.
- Il template consulenza base e provvisorio e serve a testare il flusso.
- Il dettaglio preventivo deve aiutare l'operatore a capire cosa manca.
- Il manuale operativo serve all'operatore, non agli sviluppatori.
- I preventivi gia convertiti in commessa devono essere distinguibili e filtrabili.
- Ogni chiusura sprint deve includere controllo di allineamento documentazione.

## Aspetti Da Non Dimenticare

- Le diciture fiscali e commerciali restano da validare con commercialista.
- Il documento consulenza non deve esporre il dettaglio economico interno.
- La modalita fornitura/artigiano resta prevista ma non e il profilo principale attuale.
- Il template DOCX base non e il layout definitivo.
- I dati demo non rappresentano clienti reali.
- Database SQLite e file generati restano locali e non vanno tracciati in Git.

## Rimandato A Sprint 03

- Dettaglio commessa.
- Ricerca su clienti, materiali, stampanti e documenti.
- Formula prezzo/margine piu strutturata.
- Layout DOCX consulenza piu curato.
- Procedura BMAX Linux Server.
- Backup e ripristino.
- Collegamento GitHub.
- UX piu giovane e accattivante, da valutare piu avanti con skill dedicata, Lovable o revisione UI.

## Proposta Per Sprint 03

Obiettivo consigliato: consolidare il flusso post-accettazione e preparare il passaggio verso installazione/manutenzione.

Attivita consigliate:

- creare dettaglio commessa;
- aggiungere cambio stato commessa;
- aggiungere date operative commessa;
- estendere ricerca a clienti/materiali/stampanti/documenti;
- iniziare procedura backup;
- iniziare procedura installazione BMAX;
- valutare collegamento GitHub.

## Frase Di Ripartenza Per Nuova Chat

Sto costruendo un gestionale Django per B3D Lab, attivita di consulenza tecnica e stampa additiva. La prima versione e locale, in sviluppo su Windows con SQLite e futura produzione su BMAX Linux Server con PostgreSQL. Abbiamo chiuso lo Sprint 02 nel file `docs/SPRINT_02_CHIUSURA.md`. Il flusso preventivo consulenza genera DOCX/PDF, usa un preventivo demo realistico, puo creare una commessa da preventivo accettato e ha ricerca/filtri su preventivi e commesse. Ripartiamo dallo Sprint 03 con obiettivo consigliato: consolidare il flusso commessa e preparare backup/installazione BMAX.
