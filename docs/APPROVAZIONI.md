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
| Benchmark | Screenshot PreventiPiraz 3D | Approvato come materiale di analisi | Da usare per progettare numerazione preventivi, archivi materiali e impostazioni operative. |
| Benchmark | Screenshot Stimalo | Approvato come materiale di analisi | Da usare per progettare flusso preventivo guidato, prezzo live, cataloghi e magazzino. |
| Sprint 09 | Dati documento configurabili | Approvato come prima versione | Profilo dati documento attivo con intestazione, condizioni standard, nota fiscale e nota interna. |
| Sprint 09 | Doppia generazione documento cliente/interno | Approvato come prima versione | Dal preventivo si genera il documento cliente consulenza e la scheda interna dettagliata. |
| Sprint 09 | Controlli prima export | Approvato come prima versione | Mancanze essenziali bloccano l'export; avvisi non bloccanti restano visibili nel dettaglio preventivo. |
| Sprint 10 | Modifica dati documento da interfaccia | Approvato come prima versione | La sezione Documenti permette di aggiornare il profilo attivo senza entrare nell'admin tecnico. |
| Sprint 10 | Chiusura sprint | Approvato | Sprint chiuso dopo test, verifica pagina locale e aggiornamento documentazione. |
| Sprint 11 | Rifinitura template PDF cliente/interno | Approvato come prima versione | Il template consulenza base passa a v3 e quello interno a v2, con layout piu leggibile e separazione confermata tra proposta cliente e dettaglio interno. |
| Sprint 11 | Chiusura sprint | Approvato | Sprint chiuso dopo test automatici, controllo Django e aggiornamento documentazione, incluso manuale operativo. |
| Sprint 12 | Gestione template DOCX da interfaccia | Approvato come prima versione | La sezione Documenti permette di caricare, modificare, attivare, disattivare e scaricare template DOCX senza usare l'admin tecnico. |
| Sprint 12 | Chiusura sprint | Approvato | Sprint chiuso dopo test automatici, controllo Django e aggiornamento documentazione, incluso manuale operativo e requisiti MVP. |
| Sprint 13 | Validazione template DOCX | Approvato come prima versione | Il caricamento blocca file DOCX non leggibili e segnaposto principali non riconosciuti per consulenza e interno. |
| Sprint 13 | Prova documento realistico | Approvato come verifica automatica | Il flusso genera proposta cliente e scheda interna da dati realistici, mantenendo separati documento cliente e dettaglio economico interno. |
| Sprint 13 | Chiusura sprint | Approvato | Sprint chiuso dopo test automatici, controllo Django e aggiornamento documentazione. |
| Sprint 14 | Template fornitura/artigiano preparatorio | Approvato come predisposizione | Dal dettaglio preventivo si puo generare un DOCX/PDF fornitura bozza, usando gli stessi dati del preventivo e le voci visibili per fornitura. |
| Sprint 14 | Validazione segnaposto fornitura/artigiano | Approvato come prima versione | I template caricati per fornitura/artigiano vengono controllati come consulenza e interno. |
| Sprint 14 | Guida variabili template DOCX nel manuale | Approvato come prima versione | Il manuale operativo elenca i campi disponibili e il modo consigliato per preparare tabelle ripetute in Word. |
| Sprint 15 | Numerazione automatica preventivi | Approvato come prima versione | Se il campo numero resta vuoto, il gestionale assegna il prossimo progressivo `B3D-ANNO-NNN`; il numero resta modificabile manualmente per casi controllati. |
| Sprint 15 | Chiusura sprint | Approvato | Sprint chiuso dopo test automatici completi, migrazione locale e aggiornamento documentazione. |
| Sprint 16 | Parametri economici stampanti/materiali | Approvato come prima versione | Materiali e stampanti espongono i parametri economici usati dai costi automatici del preventivo, con note interne di calcolo salvate sulle voci costo. |
| Sprint 16 | Chiusura sprint | Approvato | Sprint chiuso dopo test automatici, migrazione locale e aggiornamento documentazione. |
| Sprint 17 | Import dati tecnici G-code/3MF | Approvato come prima versione | Dal dettaglio preventivo si importa un file tecnico per compilare peso materiale e ore macchina della configurazione, lasciando all'operatore la generazione dei costi. |
| Sprint 17 | Chiusura sprint | Approvato | Sprint chiuso dopo test automatici, controllo Django e aggiornamento documentazione. |
| Sprint 18 | Backup automatico BMAX con script di sistema | Approvato come prima versione | Script eseguibile manualmente o da cron, con archivio datato, manifesto, checksum e rotazione. |
| Sprint 18 | Prova ripristino BMAX su ambiente temporaneo | Approvato come prima versione | Usa contenitori e volumi Docker di test per non toccare i dati reali. |
| Sprint 18 | Installazione reale BMAX e cron backup | Approvato | Gestionale raggiungibile in rete locale, backup verificato, ripristino provato e cron giornaliero alle 02:30 configurato. |
| Versionamento | Allineamento 18 sprint su GitHub e BMAX | Approvato | Recuperato lo Sprint 17 mancante su GitHub, pubblicato il commit `9a65339` e aggiornato il BMAX con `git pull`, rebuild Docker, migrazioni, statici e check Django. |
| Sprint 19 | Avvio automatico BMAX con restart policy Docker | Approvato e verificato su BMAX | I servizi principali usano `restart: unless-stopped`; dopo aggiornamento da GitHub il gestionale e ripartito correttamente sul BMAX. |
| Sprint 19 | Nome locale BMAX `b3d-gestionale.local:8000` | Approvato e verificato su rete locale | Rende piu semplice l'accesso in rete locale senza cambiare architettura; verificato dal browser dopo configurazione hostname, Avahi e `.env`. |
| Sprint 19 | Verifica PDF reale BMAX con comando dedicato | Approvato e verificato su BMAX | Il comando ha creato il preventivo test `B3D-2026-002` e generato DOCX/PDF cliente, interno e fornitura/artigiano. |
| Documenti | Storage media esplicito in produzione | Approvato come correzione tecnica | Necessario per generare documenti su BMAX con Django 5 quando `STORAGES` personalizza i file statici. |
| Backup | Copia ultimo backup fuori dal BMAX | Approvato come prima procedura manuale | Script dedicato copia l'ultimo backup su disco USB o NAS montato e verifica il checksum. |

## In Revisione

| Area | Elemento | Stato | Note |
|---|---|---|---|
| Interfaccia | Dettaglio grafico schermate | Da definire | Layout, colori, logo, densita delle informazioni. |
| Documenti | Layout grafico template `.docx` definitivo | Da definire | I template base v3 consulenza e v2 interno sono una rifinitura operativa, non il layout finale di brand. |
| Installazione | Rifinitura produzione stabile | Da definire | Docker, rete locale, riavvio automatico, nome locale e PDF reali verificati sul BMAX; resta la copia backup fuori dal BMAX. |
| Prodotto | Implementazione listini e accordi | Da pianificare | Dopo flusso preventivo base. |
| Prodotto | Implementazione documenti contrattuali cliente | Da pianificare | NDA, accordi quadro, condizioni particolari, listini firmati. |
| Prodotto | Implementazione AI e regole lavorazione | Da pianificare | Prima regole semplici, poi AI generativa. |
| Prodotto | Applicazione automatica accordi ai preventivi | Da pianificare | Richiede listini strutturati, regole prezzo e tracciabilita della fonte prezzo. |
| Magazzino | Liste editabili per tipo materiale, marca e colore | Da progettare | Evita testo libero ripetuto e rende piu ordinati materiali e preventivi. |
| Magazzino | Liste guidate materiali, marche e colori | Da progettare | Dopo Sprint 16 i parametri economici sono presenti; resta da ridurre testo libero ripetuto negli archivi. |
| Preventivi | Preventivo guidato a step con riepilogo prezzo laterale | Da valutare | Stimalo mostra un flusso chiaro con prezzo finale e breakdown sempre visibili. |
| File tecnici | Archivio originale e preview G-code/3MF | Da progettare | Sprint 17 importa i dati principali; restano da progettare conservazione file, preview e casi avanzati multi-piatto/slicer. |
| Stampanti | Evoluzione calcolo ammortamento completo | Da progettare | Sprint 16 copre costo base, manutenzione, energia e rischio fallimento; costo acquisto, vita stimata e ore gia stampate restano una possibile evoluzione futura. |
| Documenti | Layout definitivo PDF cliente/interno | Da validare con esempi reali | Sprint 11 migliora i template base, ma grafica, logo e impaginazione definitiva restano da confermare su documenti reali. |
| Documenti | Guida completa ai segnaposto template DOCX in interfaccia | Da progettare | Sprint 14 aggiunge la guida nel manuale; resta da mostrare direttamente nella pagina caricamento template l'elenco dei segnaposto disponibili e mancanti. |
| Backup | Copia automatica fuori dal BMAX | Da pianificare | La procedura manuale esiste; automatizzare solo dopo aver scelto una destinazione esterna stabile. |

## Da Validare Con Commercialista

| Area | Elemento | Stato | Note |
|---|---|---|---|
| Fiscalita | Dicitura "compenso per consulenza tecnica, progettazione, validazione e realizzazione" | Da validare | Importante per ATECO e regime forfettario. |
| Fiscalita | Livello di dettaglio in proposta cliente | Da validare | Il dettaglio resta interno. |
| Fiscalita | Descrizione da usare in fattura | Da validare | Dipende dall'inquadramento. |
| Fiscalita | Eventuale passaggio futuro ad artigiano | Da validare | Impatta documenti e gestione commerciale. |
| Fiscalita | Dicitura documento fornitura/artigiano | Da validare | Il template Sprint 14 e preparatorio e non sostituisce la validazione commerciale/fiscale. |

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
