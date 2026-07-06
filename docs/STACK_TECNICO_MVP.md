# Stack Tecnico MVP

## Scopo

Questo documento definisce lo stack tecnico consigliato per la prima versione del gestionale.

La scelta tiene insieme quattro esigenze:

- partire in modo semplice;
- usare tecnologie diffuse;
- lasciare il progetto comprensibile a sviluppatori esterni;
- non chiudere la strada a una futura evoluzione SaaS.

## Stack Consigliato

| Area | Scelta | Motivo |
|---|---|---|
| Sistema operativo | Linux Server | Target del mini PC BMAX. |
| Backend | Django | Diffuso, stabile, adatto a gestionali. |
| Database | PostgreSQL | Solido, professionale, adatto a crescita futura. |
| Frontend iniziale | Template Django modulari | Semplice da sviluppare e mantenere nella prima versione. |
| Interazioni dinamiche | HTMX, se utile | Permette interazioni moderne senza creare subito una SPA complessa. |
| CSS | CSS organizzato come design system leggero | Separazione chiara dello stile e componenti riutilizzabili. |
| Automazioni | Celery + Redis | Standard diffuso per lavori in background. |
| Template documenti | DOCX caricabili | Personalizzabili e adatti a una futura visione SaaS. |
| Compilazione DOCX | docxtpl / python-docx | Librerie Python diffuse per lavorare con Word. |
| Conversione PDF | LibreOffice headless | Conversione automatica da DOCX a PDF su Linux Server. |
| File allegati | Storage locale strutturato | Semplice nella prima installazione, evolvibile in futuro. |
| Deploy locale | Docker Compose oppure installazione diretta documentata | Docker consigliato per rendere l'installazione piu ripetibile. |

## Backend

### Scelta

Django.

### Perche

Django e adatto per:

- gestionali;
- pannelli amministrativi;
- utenti e permessi;
- database relazionali;
- modelli dati chiari;
- generazione documenti;
- sviluppo ordinato.

Inoltre e una tecnologia conosciuta da molti sviluppatori Python, quindi e piu facile passare il progetto a terzi.

## Database

### Scelta

PostgreSQL.

### Perche

PostgreSQL e piu adatto di SQLite per un gestionale che potrebbe crescere.

Vantaggi:

- affidabile;
- adatto a dati relazionali;
- supportato benissimo da Django;
- adatto a backup seri;
- compatibile con una futura evoluzione SaaS.

SQLite puo essere utile solo per prototipi molto iniziali, ma non e consigliato come base del progetto.

## Frontend

### Scelta MVP

Frontend integrato in Django, organizzato in template modulari.

### HTMX

HTMX puo essere usato per rendere alcune parti piu fluide senza introdurre un frontend separato.

Esempi utili:

- aggiornare una riga di tabella;
- salvare una voce di costo;
- cambiare stato preventivo;
- aggiungere una configurazione;
- mostrare anteprima documento;
- aggiornare badge e totali.

HTMX va usato dove semplifica l'esperienza, non ovunque.

### Evoluzione Futura

Se il gestionale diventera SaaS e richiedera interfacce piu complesse, il backend potra esporre API e il frontend potra diventare separato.

Questa evoluzione non deve essere obbligatoria nella prima versione.

## CSS E Componenti

### Scelta

CSS separato e organizzato come design system leggero.

Componenti minimi:

- bottoni;
- tabelle;
- form;
- layout pagina;
- navigazione;
- badge stato;
- messaggi;
- schede riepilogo;
- modali semplici.

### Regola

Lo stile non deve essere scritto casualmente dentro ogni pagina.

Deve essere ordinato in file dedicati, cosi uno sviluppatore esterno puo modificarlo senza cercare in tutto il progetto.

## Automazioni

### Scelta

Celery + Redis.

### Perche

Alcune attivita devono avvenire in background:

- estrazione preview da 3MF;
- analisi G-code;
- generazione DOCX;
- conversione PDF;
- backup;
- promemoria;
- controlli periodici.

Celery e uno standard molto conosciuto nel mondo Django. Redis funziona come supporto per la coda dei lavori.

## Documenti

### Template

I template saranno caricabili in formato `.docx`.

### Output

Il sistema generera:

- `.docx` compilato;
- PDF derivato.

### Librerie

Scelte candidate:

- `docxtpl` per compilare template con segnaposto;
- `python-docx` per operazioni semplici su documenti Word;
- LibreOffice headless per convertire in PDF.

## File 3MF E G-code

### 3MF

Prima versione:

- salvataggio file originale;
- estrazione thumbnail se presente;
- estrazione metadati base.

Futuro:

- preview 3D interattiva.

### G-code

Prima versione:

- salvataggio file originale;
- estrazione tempo stimato se presente;
- estrazione materiale stimato se presente;
- estrazione thumbnail se presente;
- riepilogo tecnico.

Futuro:

- visualizzazione layer e percorso.

## Storage File

### Prima Versione

Storage locale sul server.

I file devono essere organizzati per area:

- allegati originali;
- preview;
- template;
- documenti generati;
- backup.

### Evoluzione Futura

In una versione SaaS, lo storage potra essere spostato su servizi esterni compatibili con oggetti/file cloud.

La prima versione deve quindi evitare percorsi rigidi e difficili da cambiare.

## Installazione

### Direzione Consigliata

Docker Compose e consigliato per rendere l'installazione piu ripetibile.

Servizi previsti:

- applicazione Django;
- database PostgreSQL;
- Redis;
- worker Celery;
- servizio scheduler Celery;
- eventuale reverse proxy.

### Nota

Se Docker risultasse troppo complesso per la prima installazione personale, si potra documentare anche una installazione diretta su Linux Server.

## Scelte Da Confermare Prima Dello Sviluppo

| Area | Scelta proposta | Stato |
|---|---|---|
| Backend | Django | Approvato |
| Database | PostgreSQL | Approvato |
| Automazioni | Celery + Redis | Approvato |
| Documenti | DOCX + PDF via LibreOffice | Approvato |
| Frontend | Template Django modulari + HTMX mirato | Approvato |
| Deploy | Docker Compose | Approvato |

## Decisione Pratica

Questo stack e approvato come base della prima versione.

Il prossimo passo e creare lo scheletro applicativo coerente con queste scelte.

## Ambiente Di Sviluppo

In sviluppo su Windows il progetto puo usare SQLite tramite `DJANGO_ENV=dev`.

Questa scelta serve solo a semplificare il lavoro locale. La produzione sul BMAX resta basata su PostgreSQL tramite `DJANGO_ENV=prod`.
