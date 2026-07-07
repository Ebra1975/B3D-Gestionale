# Sprint 03 - Chiusura

Data chiusura: 2026-07-07

## Obiettivo Dello Sprint

Consolidare il flusso post-accettazione del preventivo e preparare il gestionale al passaggio verso installazione, manutenzione e uso piu stabile.

Lo sprint aveva anche lo scopo di rendere gli archivi piu consultabili, introdurre una prima regola prezzo/margine, migliorare il documento consulenza e collegare il progetto a GitHub come ponte verso il BMAX.

## Risultato Sintetico

Obiettivo raggiunto.

Il gestionale ora permette di:

- aprire una scheda commessa dopo l'accettazione del preventivo;
- aggiornare stato, date e note operative della commessa;
- vedere nella commessa cliente, preventivo, configurazione scelta, costi previsti e documenti collegati;
- cercare rapidamente clienti, materiali, stampanti e documenti;
- applicare una regola prezzo/margine base con arrotondamento;
- creare backup locali di sviluppo;
- seguire una prima procedura di backup/ripristino;
- seguire una prima procedura di installazione BMAX Linux Server;
- generare una proposta consulenza con template base v2 piu ordinato;
- usare GitHub come repository remoto del progetto.

## Funzioni Implementate

### Commesse

- Aggiunta scheda dettaglio commessa.
- Aggiunta pagina modifica commessa.
- Collegamento dalla lista commesse al dettaglio.
- Dopo la creazione da preventivo accettato, il gestionale porta direttamente alla scheda commessa.
- La scheda commessa mostra:
  - stato;
  - date operative;
  - note operative e finali;
  - cliente;
  - preventivo origine;
  - configurazione scelta;
  - costi previsti interni;
  - documenti collegati al preventivo.

### Ricerca Archivi

- Ricerca su clienti.
- Ricerca su materiali.
- Ricerca su stampanti.
- Ricerca su documenti e template.

### Prezzo E Margine

- Aggiunto riepilogo economico nella configurazione:
  - costo interno;
  - margine commerciale;
  - percentuale margine effettiva;
  - totale proposta.
- Aggiunta regola prezzo con:
  - percentuale di margine;
  - arrotondamento;
  - aggiornamento della voce interna **Margine commerciale**.
- La regola evita il doppio conteggio di piu voci margine.

### Backup E Ripristino

- Aggiunto comando:

```text
python manage.py backup_local
```

- Il comando salva in uno zip:
  - database SQLite locale;
  - cartella `media/`;
  - documentazione `docs/`.
- Aggiunta esclusione `backups/` da Git.
- Creata guida `docs/BACKUP_E_RIPRISTINO.md`.

### Installazione BMAX

- Creata guida `docs/INSTALLAZIONE_BMAX_LINUX.md`.
- Documentati:
  - prerequisiti;
  - clone da GitHub;
  - configurazione `.env`;
  - avvio Docker Compose;
  - migrazioni;
  - creazione amministratore;
  - verifica applicazione;
  - note per rete locale.

### Documenti Consulenza

- Template consulenza automatico aggiornato a v2.
- Layout piu ordinato con:
  - intestazione B3D Lab;
  - riepilogo cliente/preventivo;
  - contesto richiesta;
  - soluzione tecnica;
  - tabella economica sintetica;
  - nota fiscale/commerciale da validare con commercialista;
  - footer.
- Generazione DOCX/PDF verificata sul preventivo demo.

### GitHub E Versionamento

- Creato documento `docs/GITHUB_E_VERSIONAMENTO.md`.
- Configurato remote:

```text
origin -> https://github.com/Ebra1975/B3D-Gestionale.git
```

- Primo push completato.
- Branch locale `master` collegato a `origin/master`.
- Sprint 03 salvato nei commit:
  - `022fee8 Completa flussi operativi Sprint 03`;
  - `67611fd Documenta collegamento GitHub`.

## Verifiche Eseguite

- `python manage.py check` con esito positivo.
- Compilazione Python di `config` e `apps` con esito positivo.
- Apertura pagine clienti, materiali, stampanti e documenti verificata.
- Apertura dettaglio commessa e modifica commessa verificata.
- Applicazione regola prezzo/margine verificata sul preventivo demo.
- Backup locale verificato con creazione archivio zip.
- Template consulenza v2 verificato generando DOCX/PDF.
- Push GitHub verificato.
- Repository Git locale pulito prima della chiusura.

## Documentazione Allineata

In chiusura sprint sono stati controllati e aggiornati:

- `docs/DECISIONI.md`;
- `docs/APPROVAZIONI.md`;
- `docs/SCHERMATE_E_FLUSSI.md`;
- `docs/MANUALE_OPERATIVO.md`;
- `docs/BOARD_SPRINT_03.md`;
- `docs/BACKUP_E_RIPRISTINO.md`;
- `docs/INSTALLAZIONE_BMAX_LINUX.md`;
- `docs/GITHUB_E_VERSIONAMENTO.md`.

## Decisioni Consolidate Nello Sprint

- La prima scheda commessa usa i campi gia presenti nel modello dati.
- La prima regola prezzo/margine resta dentro le voci di costo interne, senza duplicare dati economici.
- Il backup locale di sviluppo puo essere gestito con comando Django dedicato.
- La produzione BMAX resta basata su Docker Compose, PostgreSQL e Redis.
- GitHub e il ponte ufficiale tra sviluppo Windows e futuro BMAX.
- Il template consulenza v2 e una base migliorata, ma non ancora il layout definitivo di brand.

## Aspetti Da Non Dimenticare

- Database, media, backup e `.env` non vanno caricati su GitHub.
- Le diciture fiscali e commerciali restano da validare con commercialista.
- Il documento consulenza non deve esporre il dettaglio economico interno.
- Il backup BMAX e ancora manuale: l'automazione resta da fare.
- La procedura BMAX va verificata direttamente sul mini PC.

## Rimandato A Sprint 04

- Dashboard piu operativa.
- Scheda cliente piu completa con storico preventivi, commesse e documenti.
- Backup automatico BMAX con rotazione.
- Verifica reale installazione BMAX.
- Layout DOCX definitivo di brand.
- Prime impostazioni gestibili senza codice.

## Proposta Per Sprint 04

Obiettivo consigliato: rendere il gestionale piu comodo nell'uso quotidiano e prepararlo alla prima installazione reale.

Attivita consigliate:

- migliorare dashboard con preventivi aperti, commesse attive e scadenze;
- creare scheda cliente dettagliata;
- aggiungere impostazioni base B3D Lab;
- preparare backup automatico BMAX;
- verificare installazione sul BMAX;
- iniziare il layout definitivo del documento consulenza partendo da esempi reali.

## Frase Di Ripartenza Per Nuova Chat

Sto costruendo un gestionale Django per B3D Lab. Abbiamo chiuso lo Sprint 03 nel file `docs/SPRINT_03_CHIUSURA.md`. Il gestionale ora ha dettaglio commessa, ricerca estesa sugli archivi, regola prezzo/margine, backup locale, guide BMAX/GitHub, template consulenza v2 e repository GitHub collegato. Ripartiamo dallo Sprint 04 con obiettivo consigliato: dashboard operativa, scheda cliente completa, impostazioni base e preparazione installazione reale su BMAX.
