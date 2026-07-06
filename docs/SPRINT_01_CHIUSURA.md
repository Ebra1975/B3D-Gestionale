# Sprint 01 - Chiusura

Data chiusura: 2026-07-06

## Obiettivo Dello Sprint

Definire le basi del gestionale B3D Lab e avviare una prima versione locale utilizzabile da browser in ambiente di sviluppo Windows.

Lo sprint ha avuto anche lo scopo di trasformare le idee iniziali in documenti di progetto comprensibili, in modo che il lavoro possa essere ripreso in una nuova chat o consegnato in futuro a uno sviluppatore esterno.

## Contesto Confermato

- Il gestionale nasce per una attivita di stampa additiva e consulenza tecnica.
- La prima versione sara usata da una sola persona.
- L'ambiente di produzione previsto e un mini PC BMAX con Linux Server.
- L'ambiente di sviluppo attuale e Windows.
- L'utente non programma, quindi il progetto deve restare spiegabile, ordinato e manutenibile.

## Decisioni Principali Approvate

- Django e la base applicativa del progetto.
- In sviluppo si usa SQLite su Windows.
- In produzione si usera PostgreSQL sul BMAX Linux Server.
- GitHub sara il ponte tra sviluppo Windows e produzione BMAX.
- Il gestionale deve mantenere sempre il dettaglio economico interno.
- Lo stesso preventivo dovra poter essere prodotto in piu viste:
  - interna dettagliata;
  - consulenza;
  - fornitura/artigiano futura.
- Il profilo attuale verso cliente e consulenza.
- I template documento saranno caricabili in formato `.docx`.
- Il gestionale dovra produrre sia `.docx` compilati sia PDF.
- Backend, frontend e CSS devono restare separati nelle responsabilita.
- Il progetto deve restare compatibile con una futura evoluzione SaaS, senza complicare troppo la prima versione.
- Listini base, listini cliente, accordi commerciali e documenti collegati come NDA sono previsti come direzione futura.
- AI e automazioni saranno usate come copilota operativo, non come decisore autonomo.

## Documenti Creati O Aggiornati

- `docs/VISIONE_PRODOTTO.md`
- `docs/REQUISITI_MVP.md`
- `docs/REGOLE_PREVENTIVI.md`
- `docs/SCHERMATE_E_FLUSSI.md`
- `docs/MODELLO_DATI.md`
- `docs/ARCHITETTURA_TECNICA.md`
- `docs/INFRASTRUTTURA_E_AUTOMAZIONI.md`
- `docs/STACK_TECNICO_MVP.md`
- `docs/WORKFLOW_DEV_PROD.md`
- `docs/LISTINI_E_ACCORDI_CLIENTE.md`
- `docs/AI_E_AUTOMAZIONI_OPERATIVE.md`
- `docs/DECISIONI.md`
- `docs/APPROVAZIONI.md`

## Funzioni Gia Avviate Nel Gestionale

- Progetto Django creato.
- Ambiente virtuale Python creato.
- Dipendenze principali installate.
- Database locale SQLite creato.
- Pannello admin Django disponibile.
- Dashboard iniziale disponibile.
- Sezione clienti avviata.
- Sezione preventivi avviata.
- Sezione configurazioni tecniche avviata.
- Sezione voci di costo avviata.
- Sezione materiali avviata.
- Sezione stampanti avviata.
- Moduli base predisposti per commesse, documenti, file e automazioni.

## Preventivi E Costi

Nel flusso preventivo sono stati avviati:

- dati generali del preventivo;
- cliente collegato;
- configurazioni tecniche alternative;
- materiale;
- stampante;
- quantita;
- peso materiale per unita;
- tempo macchina per unita;
- voci di costo interne;
- calcolo totale configurazione;
- calcolo prezzo unitario.

Sono stati aggiunti tre pulsanti operativi:

- `Genera costo materiale`;
- `Genera costo macchina`;
- `Aggiungi setup`.

Questi pulsanti generano o aggiornano le relative voci di costo interne, evitando duplicazioni inutili quando vengono premuti piu volte.

## Stato Tecnico A Fine Sprint

- Controllo generale Django eseguito con esito positivo.
- I tre pulsanti automatici del preventivo sono stati verificati con simulazione locale.
- Il server locale e pensato per essere usato da browser all'indirizzo `http://127.0.0.1:8000/`.
- La cartella del progetto non risulta ancora inizializzata come repository Git.

## Aspetti Da Non Dimenticare

- Le diciture fiscali e commerciali importanti restano da validare con il commercialista.
- Il dettaglio economico completo deve restare interno.
- La proposta cliente in formato consulenza non deve esporre automaticamente tutte le voci interne.
- La modalita fornitura/artigiano resta prevista per il futuro.
- Listini cliente, accordi commerciali, NDA e documenti contrattuali saranno progettati dopo il primo flusso preventivo completo.
- Le automazioni dovranno aiutare a ridurre errori e dipendenza dalla memoria del titolare.

## Punti Aperti

- Inizializzare Git e collegare il progetto a GitHub.
- Definire una prima formula di prezzo e margine.
- Definire il layout del documento `.docx` per la proposta di consulenza.
- Generare il primo documento da template.
- Migliorare la schermata preventivo per renderla piu comoda nell'uso quotidiano.
- Scrivere la procedura di installazione sul BMAX Linux Server.
- Pianificare backup e ripristino.

## Proposta Per Sprint 02

Obiettivo consigliato: chiudere un primo flusso reale di preventivo.

Attivita consigliate:

- inizializzare Git;
- creare un template `.docx` base per proposta di consulenza;
- generare un primo `.docx` compilato dal gestionale;
- predisporre la conversione PDF;
- migliorare la pagina dettaglio preventivo;
- pulire o ricreare dati di esempio coerenti.

## Frase Di Ripartenza Per Nuova Chat

Sto costruendo un gestionale Django per B3D Lab, attivita di consulenza tecnica e stampa additiva. La prima versione e locale, in sviluppo su Windows con SQLite e futura produzione su BMAX Linux Server con PostgreSQL. Abbiamo chiuso lo Sprint 01 nel file `docs/SPRINT_01_CHIUSURA.md`. Ripartiamo dallo Sprint 02 con obiettivo: chiudere il primo flusso reale di preventivo e generazione documento `.docx` consulenza.
