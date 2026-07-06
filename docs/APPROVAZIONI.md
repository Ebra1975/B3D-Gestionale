# Approvazioni

Questo documento tiene traccia di cosa e approvato, cosa e in revisione e cosa richiede conferma esterna.

## Approvato

| Area | Elemento | Stato | Note |
|---|---|---|---|
| Prodotto | Prima versione per uso personale | Approvato | Multiutente rimandato. |
| Preventivi | Vista interna dettagliata | Approvato | Sempre disponibile. |
| Preventivi | Profilo documento consulenza | Approvato | Profilo principale attuale. |
| Preventivi | Profilo documento fornitura/artigiano | Approvato | Previsto per futuro. |
| Preventivi | Un solo dato economico, piu viste | Approvato | Evita duplicazioni. |
| Server | Mini PC BMAX con Linux Server | Approvato | Target iniziale. |
| Utenti | Singolo utente nella v1 | Approvato | Semplifica MVP. |
| Interfaccia | Menu principale con dashboard, clienti, preventivi, commesse, materiali, stampanti, documenti e impostazioni | Approvato come base | Potra essere semplificato durante lo sviluppo. |
| MVP | Priorita su preventivi e PDF consulenza/interno | Approvato come base | Prima utilita reale del gestionale. |
| Documenti | Template caricabili in formato `.docx` | Approvato | Base importante per personalizzazione e futura visione SaaS. |
| Documenti | Output documento in `.docx` e PDF | Approvato | `.docx` modificabile, PDF da inviare. |
| Prodotto | Visione futura SaaS da considerare gia nelle scelte iniziali | Approvato | Senza complicare troppo la prima versione. |
| File | Preview 3MF/G-code come elaborazioni derivate dai file originali | Approvato come direzione | Preview avanzate rimandate. |
| Automazioni | Lavori lenti in background | Approvato come direzione | Preview, documenti, conversioni e backup. |
| Architettura | Separazione responsabilita backend, frontend e CSS | Approvato | Pensata anche per sviluppatori esterni. |
| Architettura | Django come candidato principale backend | Approvato come direzione | Scelta definitiva prima dello sviluppo. |
| Architettura | Frontend Django modulare per la prima versione | Approvato come direzione | Evita complessita iniziale di una SPA separata. |
| Architettura | CSS organizzato come piccolo design system | Approvato | Componenti riutilizzabili e stile coerente. |
| Stack MVP | Django come backend | Approvato | Base ufficiale del progetto. |
| Stack MVP | PostgreSQL come database | Approvato | Base ufficiale del progetto. |
| Stack MVP | Celery + Redis per lavori in background | Approvato | Base ufficiale per automazioni. |
| Stack MVP | HTMX per interazioni dinamiche mirate | Approvato | Da usare solo dove semplifica. |
| Stack MVP | LibreOffice headless per conversione DOCX in PDF | Approvato | Da verificare in installazione Linux. |
| Stack MVP | Docker Compose per installazione ripetibile | Approvato | Base consigliata per installazione ordinata. |
| Ambienti | Windows come ambiente di sviluppo | Approvato | Usa SQLite per semplificare il lavoro locale. |
| Ambienti | BMAX Linux Server come produzione | Approvato | Usa PostgreSQL, Redis, Celery e Docker Compose. |
| Ambienti | GitHub come ponte dev/prod | Approvato | Permette passaggio ordinato verso produzione. |
| Versionamento | Repository Git locale | Approvato | Primo punto stabile creato durante Sprint 02 prima del collegamento GitHub. |
| Prodotto | Listini base, listini cliente e accordi commerciali | Approvato come direzione | Da progettare senza appesantire il primo MVP. |
| Prodotto | Documenti cliente/contrattuali come NDA e allegati commerciali | Approvato come direzione | Da implementare a tempo debito. |
| Prodotto | AI come copilota e non come decisore | Approvato | Ogni decisione importante resta al titolare. |
| Prodotto | Casistiche lavorazione con checklist e regole | Approvato come direzione | Base per automazioni e suggerimenti futuri. |
| Sprint 02 | Generazione DOCX consulenza dal dettaglio preventivo | Approvato come primo flusso | Generazione locale immediata, senza esporre il dettaglio economico interno. |

## In Revisione

| Area | Elemento | Stato | Note |
|---|---|---|---|
| Interfaccia | Dettaglio grafico schermate | Da definire | Layout, colori, logo, densita delle informazioni. |
| Calcolo | Margine e prezzi | Da definire | Serve formula iniziale. |
| Documenti | Layout grafico template `.docx` | Da definire | Partire dai PDF esistenti come riferimento. |
| Documenti | Template consulenza base generato dal gestionale | Provvisorio | Serve a testare il flusso reale; il layout finale resta da definire. |
| Installazione | Procedura Linux Server | Da definire | Scrivere guida passo passo. |
| Tecnologia | Prima struttura progetto applicativo | Da fare | Creare scheletro Django, moduli, configurazione e documentazione avvio. |
| Prodotto | Implementazione listini e accordi | Da pianificare | Dopo flusso preventivo base. |
| Prodotto | Implementazione documenti contrattuali cliente | Da pianificare | NDA, accordi quadro, condizioni particolari, listini firmati. |
| Prodotto | Implementazione AI e regole lavorazione | Da pianificare | Prima regole semplici, poi AI generativa. |

## Da Validare Con Commercialista

| Area | Elemento | Stato | Note |
|---|---|---|---|
| Fiscalita | Dicitura "compenso per consulenza tecnica, progettazione, validazione e realizzazione" | Da validare | Importante per ATECO e regime forfettario. |
| Fiscalita | Livello di dettaglio in proposta cliente | Da validare | Il dettaglio resta interno. |
| Fiscalita | Descrizione da usare in fattura | Da validare | Dipende dall'inquadramento. |
| Fiscalita | Eventuale passaggio futuro ad artigiano | Da validare | Impatta documenti e gestione commerciale. |

## Promemoria

Una funzione e pronta solo quando:

- e comprensibile per l'utente;
- risolve un caso reale;
- e stata verificata;
- se cambia una decisione importante, `docs/DECISIONI.md` e aggiornato.
