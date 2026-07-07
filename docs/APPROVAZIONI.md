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
| Sprint 02 | Manuale operativo nella sidebar | Approvato come prima versione | Serve all'operatore per seguire procedure come preventivo e commessa. |
| Sprint 02 | Creazione commessa da preventivo accettato | Approvato come primo flusso | Collega preventivo, cliente e configurazione scelta senza ricopiare dati. |
| Sprint 02 | Ricerca e filtri su preventivi e commesse | Approvato come prima versione | Aiuta a distinguere lavoro aperto, convertito e commesse operative. |
| Sprint 03 | Dettaglio commessa operativo | Approvato come prima versione | Mostra stato, date, note, preventivo, configurazione scelta, costi previsti e documenti collegati. |
| Sprint 03 | Ricerca estesa sugli archivi principali | Approvato come prima versione | Aggiunge ricerca a clienti, materiali, stampanti e documenti. |
| Sprint 03 | Formula prezzo/margine base | Approvato come prima versione | Calcola una voce interna di margine commerciale da costo interno, percentuale e arrotondamento. |
| Sprint 03 | Backup locale di sviluppo | Approvato come prima versione | Comando `backup_local` per salvare SQLite, media e documentazione in uno zip. |
| Sprint 03 | Procedura BMAX Linux Server | Approvato come prima bozza | Guida iniziale per installazione Docker Compose in rete locale. |
| Sprint 03 | Template consulenza base v2 | Approvato come prima rifinitura | Layout piu ordinato con intestazione, riepilogo cliente/preventivo, sezione tecnica, sintesi economica e nota fiscale da validare. |
| Sprint 03 | Collegamento GitHub | Approvato | Repository `Ebra1975/B3D-Gestionale` configurato come `origin` e primo push completato. |
| Sprint 04 | Scheda cliente con memoria commerciale | Approvato come prima versione | Mostra dati cliente, note, preventivi, commesse, accordi e documenti commerciali collegati. |
| Sprint 04 | Accordi cliente | Approvato come prima versione | Archivio collegato al cliente con stato, validita, listino collegato, condizioni e note commerciali. |
| Sprint 04 | Documenti commerciali cliente | Approvato come prima versione | Archivio collegato al cliente per NDA, accordi, listini firmati e allegati con file e scadenze. |
| Sprint 05 | Procedure installazione, backup, ripristino, GitHub e manutenzione | Approvato come base operativa | Prima guida per passare al BMAX senza perdere controllo su dati, codice e aggiornamenti. |
| Backup | Prova di ripristino prima dei dati reali | Approvato come obbligatoria | Serve a verificare che il backup sia realmente recuperabile. |
| Sprint 06 | Dashboard operativa con promemoria | Approvato come prima versione | Mostra preventivi, commesse, accordi e documenti commerciali da seguire. |
| Dashboard | Soglie 14/30 giorni per promemoria | Approvato come prima versione | 14 giorni per preventivi/commesse, 30 giorni per accordi/documenti commerciali. |
| Sprint 07 | Memoria commerciale cliente nel dettaglio preventivo | Approvato come prima versione | Mostra accordi, listini collegati e documenti commerciali prima della proposta. |
| Preventivi | Accordi cliente come promemoria non automatico | Approvato come prima versione | La revisione del titolare resta obbligatoria prima di applicare condizioni economiche. |
| Sprint 08 | Prezzo assistito e condizioni cliente | Approvato come titolo e direzione | Lo sprint prepara una revisione economica piu guidata, mantenendo la conferma manuale del titolare. |
| Sprint 08 | Conferma manuale condizioni cliente sul preventivo | Approvato come prima versione | Salva data e note del controllo senza modificare automaticamente prezzi o margini. |
| Benchmark | Comparazione con Stimalo e PreventiPiraz 3D | Approvato come riferimento di analisi | Da usare per orientare i prossimi sprint, non come copia funzionale. |

## In Revisione

| Area | Elemento | Stato | Note |
|---|---|---|---|
| Interfaccia | Dettaglio grafico schermate | Da definire | Layout, colori, logo, densita delle informazioni. |
| Documenti | Layout grafico template `.docx` definitivo | Da definire | Il template base v2 e una prima rifinitura, non il layout finale di brand. |
| Backup | Backup automatico BMAX | Da definire | Dopo la procedura manuale serve automatizzare frequenza, rotazione e controllo esito. |
| Installazione | Rifinitura produzione stabile | Da definire | Verificare direttamente sul BMAX Docker, LibreOffice PDF, IP locale e riavvio automatico. |
| Manutenzione | Avvio automatico del gestionale dopo riavvio BMAX | Da definire | Valutare dopo la prima installazione reale. |
| Prodotto | Implementazione listini e accordi | Da pianificare | Dopo flusso preventivo base. |
| Prodotto | Implementazione documenti contrattuali cliente | Da pianificare | NDA, accordi quadro, condizioni particolari, listini firmati. |
| Prodotto | Implementazione AI e regole lavorazione | Da pianificare | Prima regole semplici, poi AI generativa. |
| Prodotto | Applicazione automatica accordi ai preventivi | Da pianificare | Richiede listini strutturati, regole prezzo e tracciabilita della fonte prezzo. |

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

Uno sprint puo essere chiuso solo dopo aver controllato che la documentazione sia allineata a quanto implementato, in particolare:

- `docs/DECISIONI.md`;
- `docs/APPROVAZIONI.md`;
- board dello sprint;
- manuale operativo, se il flusso cambia;
- schermate e flussi, se cambia l'uso del gestionale.
