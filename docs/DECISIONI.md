# Decisioni

Questo documento registra le decisioni importanti del progetto.

## Decisioni Approvate

| Data | Area | Decisione | Motivo |
|---|---|---|---|
| 2026-07-06 | Prodotto | La prima versione sara usata da una sola persona. | Riduce complessita iniziale. |
| 2026-07-06 | Server | Il gestionale risiedera su mini PC BMAX con Linux Server. | Hardware gia disponibile e adeguato. |
| 2026-07-06 | Preventivi | Il sistema manterra una vista interna dettagliata. | Serve a controllare costi reali e marginalita. |
| 2026-07-06 | Preventivi | Il sistema generera almeno due modelli cliente: consulenza e fornitura/artigiano. | Il profilo attuale e consulenza, ma serve predisposizione futura. |
| 2026-07-06 | Fiscalita | Il modello principale attuale verso cliente e consulenza. | Coerente con l'inquadramento indicato dall'utente. |
| 2026-07-06 | Documenti | I dati economici non devono essere duplicati tra modelli documento. | Evita errori e incoerenze. |
| 2026-07-06 | Prodotto | Le schermate principali saranno dashboard, clienti, preventivi, commesse, materiali, stampanti, documenti e impostazioni. | Coprono il flusso reale dalla richiesta alla consegna. |
| 2026-07-06 | MVP | La priorita iniziale e su dashboard, clienti, preventivi, configurazioni, costi interni e PDF consulenza/interno. | Permette di usare il gestionale per un preventivo reale. |
| 2026-07-06 | Documenti | I template documento saranno caricabili in formato `.docx`. | Rende il sistema personalizzabile e piu adatto a una futura visione SaaS. |
| 2026-07-06 | Documenti | Il gestionale generera sia `.docx` compilati sia PDF. | Il `.docx` resta modificabile, il PDF e pronto per l'invio. |
| 2026-07-06 | Infrastruttura | Le preview di file 3MF/G-code saranno generate come dati derivati dai file originali. | Mantiene separati originali, anteprime e metadati. |
| 2026-07-06 | Infrastruttura | Le automazioni lente saranno gestite in background. | Evita di bloccare l'utente durante preview, documenti e backup. |
| 2026-07-06 | Prodotto | Anche la prima versione locale deve restare compatibile con una futura evoluzione SaaS. | Evita scelte iniziali troppo chiuse. |
| 2026-07-06 | Architettura | Backend, frontend e CSS saranno separati nelle responsabilita. | Rende il progetto piu ordinato e facile da affidare a sviluppatori esterni. |
| 2026-07-06 | Architettura | Django e il candidato principale per il backend. | E diffuso, stabile e adatto a gestionali. |
| 2026-07-06 | Architettura | La prima versione usera un frontend Django modulare, senza SPA separata obbligatoria. | Mantiene il progetto semplice ma evolvibile. |
| 2026-07-06 | Architettura | Il CSS sara organizzato come piccolo design system. | Evita stile sparso e facilita coerenza visiva. |
| 2026-07-06 | Stack MVP | PostgreSQL e il database consigliato. | E solido, diffuso e adatto a crescita futura. |
| 2026-07-06 | Stack MVP | Celery + Redis sono la scelta proposta per automazioni e lavori in background. | Sono standard diffusi nel mondo Django. |
| 2026-07-06 | Stack MVP | HTMX potra essere usato per interazioni dinamiche mirate. | Migliora l'esperienza senza introdurre subito una SPA complessa. |
| 2026-07-06 | Stack MVP | LibreOffice headless e la scelta proposta per convertire DOCX in PDF. | Permette conversione automatica sul server Linux. |
| 2026-07-06 | Stack MVP | Docker Compose e consigliato per installazione ripetibile. | Aiuta a gestire app, database, Redis e worker in modo ordinato. |
| 2026-07-06 | Stack MVP | Lo stack MVP e approvato: Django, PostgreSQL, Celery, Redis, HTMX mirato, DOCX/PDF e Docker Compose. | Base ufficiale per iniziare lo sviluppo. |
| 2026-07-06 | Ambienti | Windows sara usato come ambiente di sviluppo con SQLite. | Permette di lavorare senza installare PostgreSQL o Docker su Windows. |
| 2026-07-06 | Ambienti | Il BMAX Linux Server sara usato come ambiente di produzione con PostgreSQL. | Mantiene la produzione solida e coerente con lo stack approvato. |
| 2026-07-06 | Ambienti | GitHub sara il ponte tra sviluppo Windows e produzione BMAX. | Permette deploy ordinato e tracciabile. |
| 2026-07-06 | Prodotto | Il gestionale dovra prevedere listino base, listini cliente e accordi commerciali. | Utile per PMI e per rendere ripetibile la gestione commerciale. |
| 2026-07-06 | Prodotto | Il gestionale dovra prevedere anche documenti cliente/contrattuali come NDA e allegati commerciali. | Utile per PMI e relazioni continuative, da implementare in una fase successiva. |
| 2026-07-06 | Prodotto | AI e automazioni saranno usate come copilota operativo, non come decisore autonomo. | Aiutano a ridurre errori e dipendenza dalla memoria del titolare. |
| 2026-07-06 | Prodotto | Le casistiche di lavorazione saranno archiviate come regole/checklist riutilizzabili. | Trasforma esperienza pratica in metodo trasferibile. |
| 2026-07-06 | Sprint 02 | Il primo DOCX consulenza viene generato dal dettaglio preventivo in modo sincrono. | Permette di chiudere subito il primo flusso reale locale; lo spostamento in background resta possibile in seguito. |
| 2026-07-06 | Documenti | Se non esiste un template consulenza caricato, il gestionale crea un template base DOCX. | Evita di bloccare il flusso su un layout definitivo ancora da progettare. |
| 2026-07-06 | Documenti | La conversione PDF usa LibreOffice headless quando disponibile; su Windows viene preferito `soffice.com`. | `soffice.com` restituisce messaggi affidabili da terminale e funziona meglio per conversioni automatiche rispetto all'avvio grafico di Writer. |
| 2026-07-06 | Versionamento | Il progetto viene inizializzato come repository Git locale dopo il primo flusso DOCX/PDF funzionante. | Salva un punto stabile dello Sprint 02 prima di proseguire con nuove funzioni e future sincronizzazioni GitHub/BMAX. |
| 2026-07-06 | Preventivi | Il dettaglio preventivo mostra uno stato operativo con configurazione usata, totale, ultimo documento e controlli mancanti. | Aiuta a capire se la proposta consulenza e pronta senza cercare le informazioni in piu punti della pagina. |
| 2026-07-06 | Interfaccia | La sidebar resta fissa durante lo scorrimento delle pagine lunghe su desktop. | Mantiene la navigazione sempre disponibile, soprattutto nelle pagine preventivo ricche di informazioni. |
| 2026-07-07 | Manuale operativo | La "wiki" viene intesa come manuale operativo per l'operatore, con procedure passo passo. | Serve a spiegare come usare il gestionale, ad esempio come fare un preventivo, non a documentare il codice. |
| 2026-07-07 | Dati demo | Viene aggiunto un comando Django per creare un preventivo demo realistico `B3D-2026-001`. | Permette di testare e mostrare il flusso consulenza DOCX/PDF senza usare dati cliente reali. |
| 2026-07-07 | Manuale operativo | Il manuale viene esposto anche nella sidebar del gestionale con una prima pagina consultabile. | L'operatore deve poter leggere le procedure senza cercare file nella cartella di progetto. |
| 2026-07-07 | Preventivi | Il dettaglio preventivo include azioni rapide per aggiornare lo stato. | Dopo generazione e invio documento, l'operatore puo segnare rapidamente il preventivo come inviato, da rivedere, accettato o rifiutato. |
| 2026-07-07 | Commesse | Una commessa puo essere creata dal dettaglio di un preventivo accettato. | Evita ricopiature manuali e collega commessa, cliente, preventivo e configurazione scelta. |
| 2026-07-07 | Liste operative | Le liste preventivi e commesse hanno ricerca e filtri base. | Aiuta a trovare rapidamente record e separa i preventivi ancora da lavorare da quelli gia convertiti in commessa. |
| 2026-07-07 | Metodo di lavoro | Ogni chiusura sprint include controllo di allineamento documentazione. | Evita che manuale operativo, board, decisioni e schermate restino indietro rispetto al software. |
| 2026-07-07 | Sprint 03 | La prima parte dello sprint consolida la gestione commessa usando i campi gia presenti nel modello. | Permette di seguire il lavoro dopo accettazione senza introdurre complessita o migrazioni premature. |
| 2026-07-07 | Liste operative | La ricerca viene estesa a clienti, materiali, stampanti e documenti. | Riduce il tempo per trovare dati quando gli archivi iniziano a crescere. |
| 2026-07-07 | Calcolo | La prima formula prezzo/margine genera una voce interna "Margine commerciale" partendo da costo interno, percentuale e arrotondamento. | Mantiene un solo dettaglio economico interno e rende piu ripetibile il prezzo finale senza aggiungere nuovi campi al modello dati. |
| 2026-07-07 | Backup | Il backup locale di sviluppo viene gestito con un comando Django dedicato. | Permette di salvare database SQLite, media e documentazione in modo ripetibile durante lo sviluppo. |
| 2026-07-07 | Installazione | La prima procedura BMAX viene documentata come installazione Docker Compose in rete locale. | Prepara il passaggio al mini PC senza cambiare stack approvato. |
| 2026-07-07 | Documenti | Il template consulenza base generato dal gestionale viene rifinito come v2. | Migliora leggibilita e presentazione cliente, continuando a non esporre il dettaglio economico interno. |
| 2026-07-07 | Versionamento | GitHub viene preparato come repository privato da collegare al Git locale. | Serve come ponte tra sviluppo Windows e installazione BMAX, senza caricare dati, media, backup o segreti. |
| 2026-07-07 | Versionamento | Il repository GitHub `Ebra1975/B3D-Gestionale` viene collegato come `origin` e riceve il primo push. | Rende disponibile il codice per il futuro clone sul BMAX e per il passaggio ordinato dev/prod. |
| 2026-07-07 | Sprint 04 | La prima memoria commerciale cliente viene gestita nella scheda cliente. | Permette di registrare accordi, condizioni e documenti commerciali senza automatizzare ancora i prezzi. |
| 2026-07-07 | Clienti | Accordi cliente e documenti commerciali cliente sono archivi separati collegati al cliente. | Evita note libere troppo lunghe e mantiene tracciabili validita, stato, scadenze e file allegati. |
| 2026-07-07 | Preventivi | Gli accordi cliente non vengono ancora applicati automaticamente al preventivo. | La revisione del titolare resta obbligatoria finche listini e regole prezzo non sono progettati in dettaglio. |
| 2026-07-07 | Sprint 05 | Installazione, backup/ripristino, GitHub e manutenzione vengono documentati come procedure operative prima della prova reale sul BMAX. | Riduce il rischio operativo e rende il passaggio a produzione locale piu controllabile. |
| 2026-07-07 | Backup | Prima dell'uso reale sul BMAX deve essere provato almeno un ripristino su copia di test. | Un backup non verificato non garantisce recupero dei dati. |
| 2026-07-07 | Manutenzione | Gli aggiornamenti sul BMAX devono essere preceduti da backup e seguiti da controlli dal browser. | Evita aggiornamenti ciechi e rende chiaro se il gestionale resta utilizzabile. |
| 2026-07-07 | Sprint 06 | La dashboard diventa punto di controllo quotidiano con promemoria operativi. | Aiuta a seguire preventivi, commesse, accordi e documenti commerciali senza cercarli manualmente in piu sezioni. |
| 2026-07-07 | Dashboard | Le prime soglie operative sono 14 giorni per preventivi/commesse e 30 giorni per memoria commerciale cliente. | Sono soglie semplici, comprensibili e modificabili in futuro dopo l'uso reale. |
| 2026-07-07 | Sprint 07 | Il dettaglio preventivo mostra la memoria commerciale del cliente. | Prima di generare o inviare una proposta serve controllare accordi, listini collegati, NDA e documenti commerciali senza aprire manualmente piu schermate. |
| 2026-07-07 | Preventivi | Gli accordi cliente restano promemoria e non applicano ancora automatismi economici. | Evita prezzi modificati senza revisione del titolare finche listini e regole non sono progettati. |
| 2026-07-07 | Sprint 08 | Lo sprint viene intitolato "Prezzo assistito e condizioni cliente". | La prossima fase deve aiutare la revisione economica del preventivo usando la memoria commerciale, senza automatizzare ancora i prezzi. |
| 2026-07-07 | Preventivi | La revisione delle condizioni cliente viene confermata manualmente sul preventivo con data e note interne. | Mantiene tracciabile il controllo di accordi, listini e documenti commerciali senza applicare automatismi al prezzo. |
| 2026-07-07 | Benchmark | Prima di proseguire con prezzi e listini viene avviata una comparazione con Stimalo e PreventiPiraz 3D. | Serve a capire cosa imparare dagli strumenti esistenti senza snaturare il posizionamento consulenziale B3D Lab. |
| 2026-07-08 | Benchmark | Gli screenshot di PreventiPiraz 3D vengono usati per arricchire la comparazione funzionale. | Aiutano a valutare numerazione automatica, archivi configurabili, riassunto preventivo e flusso produzione prima di implementare. |
| 2026-07-08 | Benchmark | Gli screenshot di Stimalo vengono usati per arricchire la comparazione funzionale. | Aiutano a valutare preventivo guidato a step, prezzo live, import G-code/3MF, cataloghi e magazzino prima di implementare. |
| 2026-07-08 | Documenti | Le esportazioni PDF richiederanno dati di riempimento configurabili. | Senza dati azienda, cliente, condizioni standard, logo e note riutilizzabili il PDF rischia di essere generato ma non pronto per il cliente. |
| 2026-07-08 | Documenti | La comparazione dei PDF conferma la necessita di due esportazioni: cliente sintetica e interna dettagliata. | Permette di usare gli stessi dati economici in viste diverse, mantenendo il dettaglio interno separato dalla proposta cliente. |
| 2026-07-08 | Sprint 09 | Il prossimo sprint proposto e "Dati documento e PDF cliente/interno". | Le prove reali e il benchmark mostrano che prima di automatizzare altro servono dati di riempimento e controlli affidabili per i documenti. |
| 2026-07-08 | Sprint 09 | Viene aggiunto un profilo dati documento attivo per intestazione, condizioni standard e note fiscali/commerciali. | Centralizza i testi riutilizzati nei documenti e riduce il rischio di PDF incompleti o incoerenti. |
| 2026-07-08 | Sprint 09 | Dal dettaglio preventivo si generano due documenti separati: cliente consulenza e interno dettagliato. | Usa gli stessi costi del preventivo ma mantiene distinta la proposta cliente dalla scheda interna con costi e margine. |
| 2026-07-08 | Sprint 09 | Prima dell'export vengono mostrati controlli bloccanti e avvisi non bloccanti. | Evita documenti senza dati essenziali e lascia visibili le informazioni da ricontrollare prima dell'invio. |
| 2026-07-08 | Sprint 10 | I dati documento attivi sono modificabili dalla sezione Documenti senza usare l'admin tecnico. | Permette di aggiornare intestazione, contatti, condizioni standard e note prima di generare DOCX/PDF reali. |
| 2026-07-08 | Sprint 10 | Lo sprint viene chiuso con il prossimo focus su template documenti e layout PDF. | Dopo la modifica dei dati di riempimento, il passo naturale e rifinire template, logo e impaginazione cliente/interna. |
| 2026-07-08 | Sprint 11 | I template base cliente e interno vengono rifiniti come versioni consulenza v3 e interno v2. | Rende i PDF piu leggibili e usabili nel flusso reale, senza duplicare dati o cambiare il modello economico interno. |
| 2026-07-08 | Sprint 11 | Lo sprint viene chiuso con manuale operativo e documentazione allineati. | Il flusso d'uso non cambia, ma l'operatore deve sapere cosa aspettarsi dai nuovi documenti generati. |
| 2026-07-08 | Sprint 12 | I template DOCX sono gestibili dalla sezione Documenti senza usare l'admin tecnico. | Permette di caricare, modificare, attivare, disattivare e scaricare modelli Word dal flusso operativo. |
| 2026-07-08 | Documenti | Per ogni tipo documento viene mantenuto un solo template attivo alla volta. | Evita ambiguita quando il gestionale genera il prossimo DOCX/PDF. |
| 2026-07-08 | Documenti | Un template personalizzato attivo ha priorita sul template base generato dal gestionale. | Il caricamento da interfaccia deve influenzare realmente le prossime generazioni documento. |
| 2026-07-08 | Sprint 12 | Lo sprint viene chiuso con manuale operativo e documentazione allineati. | La gestione template entra nel flusso documenti e deve essere spiegata all'operatore. |
| 2026-07-08 | Sprint 13 | Il caricamento template DOCX valida il file reale e i segnaposto principali per consulenza e interno. | Evita di attivare modelli Word non leggibili o incompatibili con la generazione documento. |
| 2026-07-08 | Sprint 13 | La prova documento realistico diventa verifica automatica del flusso cliente/interno. | Conferma che la proposta cliente resta sintetica e che la scheda interna conserva costi, margine e note. |
| 2026-07-08 | Sprint 14 | Viene aggiunto un template base preparatorio per preventivo fornitura/artigiano. | Permette di predisporre la vista futura senza cambiare il profilo principale consulenza e senza duplicare i dati economici. |
| 2026-07-08 | Documenti | Il documento fornitura/artigiano usa le voci di costo marcate come visibili per fornitura e mantiene la dicitura da validare con commercialista. | Prepara un documento cliente piu vicino alla fornitura, ma segnala che l'uso reale richiede validazione fiscale/commerciale. |
| 2026-07-08 | Documenti | Il manuale operativo include una guida ai segnaposto dei template DOCX. | Permette di modificare i modelli Word partendo da variabili corrette e riduce errori nei template caricati. |
| 2026-07-08 | Sprint 15 | I preventivi ricevono automaticamente un numero progressivo `B3D-ANNO-NNN` quando il campo numero viene lasciato vuoto. | Evita numeri duplicati o scritti a mano e mantiene un riferimento stabile per clienti, documenti e commesse. |
| 2026-07-08 | Sprint 15 | Lo sprint viene chiuso con test completi e documentazione allineata. | La numerazione automatica e pronta per l'uso quotidiano nella creazione preventivo. |
| 2026-07-08 | Sprint 16 | Il prossimo sprint proposto e "Archivi guidati materiali e parametri tecnici". | Dopo la numerazione, il prossimo problema pratico e ridurre testo libero ripetuto in materiali, colori, marche e parametri usati nei preventivi. |
| 2026-07-08 | Sprint 16 | Materiali e stampanti hanno parametri economici espliciti usati dai costi automatici del preventivo. | Riduce costi arbitrari: materiale considera scarto/extra, stampante considera manutenzione, energia e rischio fallimento, mantenendo il dettaglio interno tracciabile. |
| 2026-07-08 | Sprint 16 | Lo sprint viene chiuso con migrazione locale, test e documentazione allineata. | I parametri economici sono pronti per essere provati su materiali, stampanti e preventivi reali. |
| 2026-07-08 | Sprint 17 | L'import G-code/3MF compila peso materiale e ore macchina sulla configurazione senza generare automaticamente costi o prezzo. | Riduce errori di inserimento dai dati slicer mantenendo il controllo manuale sul dettaglio economico interno. |
| 2026-07-08 | Sprint 17 | Il file tecnico originale non viene ancora archiviato; l'import salva una nota interna con nome file e valori letti. | Prima forma utile e semplice; archivio file e preview restano evoluzioni future. |
| 2026-07-08 | Sprint 17 | Lo sprint viene chiuso con test e documentazione allineata. | L'import tecnico e pronto per prove con file reali esportati dagli slicer usati da B3D Lab. |
| 2026-07-08 | Sprint 18 | Il backup BMAX viene gestito con script di sistema eseguibile da cron. | Il salvataggio deve funzionare anche se l'interfaccia web non e raggiungibile e deve essere facile da verificare sul server. |
| 2026-07-08 | Backup | Ogni backup BMAX automatico include database PostgreSQL, media, `.env`, manifesto e checksum in un archivio datato. | Serve a recuperare sia dati applicativi sia documenti/allegati, riducendo il rischio di backup incompleti. |
| 2026-07-08 | Ripristino | La prova di ripristino usa contenitori e volumi Docker temporanei, senza toccare i dati reali. | Permette di verificare il backup prima dell'uso reale del gestionale sul BMAX. |
| 2026-07-08 | Sprint 18 | Il gestionale viene avviato sul BMAX in rete locale su `192.168.1.143:8000`. | Conferma che il flusso Docker Compose funziona sul mini PC reale. |
| 2026-07-08 | Sprint 18 | Backup e prova ripristino sono stati eseguiti con successo sul BMAX. | Conferma che il salvataggio non e solo creato, ma anche recuperabile in ambiente temporaneo. |
| 2026-07-08 | Backup | Il cron giornaliero alle 02:30 viene configurato sul BMAX. | Rende il backup una routine automatica, da controllare periodicamente tramite log e archivi recenti. |
| 2026-07-08 | Sprint 18 | Lo sprint viene chiuso con prova reale BMAX, backup verificato e documentazione allineata. | La base operativa minima per proteggere i dati e pronta. |
| 2026-07-08 | Versionamento | Il recupero dello Sprint 17 viene pubblicato su GitHub e aggiornato sul BMAX fino al commit `9a65339`. | Chiude il disallineamento tra documentazione, GitHub e server BMAX: tutti i 18 sprint risultano presenti sulla macchina reale. |
| 2026-07-08 | Sprint 19 | I servizi Docker del gestionale usano `restart: unless-stopped` per il riavvio automatico dopo reboot del BMAX. | Riduce il rischio che il gestionale resti spento dopo mancanza corrente o riavvio del mini PC, senza cambiare stack tecnico. |
| 2026-07-08 | Infrastruttura | Il servizio systemd resta una procedura opzionale documentata, non obbligatoria per la prima stabilizzazione. | Docker Compose con restart policy copre il bisogno principale; systemd puo essere aggiunto se serve un controllo Linux piu esplicito. |
| 2026-07-08 | Sprint 19 | La procedura di avvio automatico richiede esplicitamente `git pull` sul BMAX prima del test di reboot. | Evita di provare il riavvio automatico su una configurazione non ancora aggiornata sul server. |
| 2026-07-08 | Sprint 19 | L'avvio automatico viene verificato sul BMAX dopo aggiornamento da GitHub. | Conferma che la prima stabilizzazione operativa funziona sul mini PC reale; systemd resta solo piano B. |
| 2026-07-08 | Sprint 19 | Il nome locale proposto per il gestionale e `b3d-gestionale.local:8000`. | Rende l'accesso quotidiano piu leggibile senza introdurre proxy o cambiare architettura; la rimozione di `:8000` resta evoluzione futura. |
| 2026-07-08 | Sprint 19 | Il nome locale `b3d-gestionale.local:8000` viene verificato da browser sulla rete reale. | Conferma che l'accesso quotidiano puo usare un nome leggibile al posto dell'IP `192.168.1.143`. |
| 2026-07-08 | Sprint 19 | La verifica PDF reale sul BMAX viene resa ripetibile con un comando Django dedicato. | Crea dati di test riconoscibili e controlla che LibreOffice generi PDF per cliente, interno e fornitura/artigiano. |
| 2026-07-08 | Documenti | In produzione viene configurato anche lo storage `default` per file media e documenti generati. | Django 5 richiede una configurazione esplicita quando si personalizza `STORAGES`; senza questa voce i DOCX/PDF non possono accedere ai file template/media. |
| 2026-07-08 | Sprint 19 | La verifica PDF reale sul BMAX viene completata con successo sul preventivo test `B3D-2026-002`. | Conferma che LibreOffice nel container web genera PDF per documento cliente, interno e fornitura/artigiano. |
| 2026-07-08 | Backup | La copia fuori dal disco principale del BMAX viene gestita con procedura manuale verificabile e script dedicato. | La prima destinazione scelta e un secondo HD interno; protegge dal guasto del disco principale ma non sostituisce una copia esterna al mini PC. |
| 2026-07-08 | Backup | Il secondo HD interno per backup e gia formattato ext4 e montato in `/mnt/backup`. | Non serve formattare: la partizione `sda1` con etichetta `b3d-backup` ha spazio sufficiente per la prima copia verificata. |

## Decisioni Da Prendere

| Area | Tema | Opzioni | Note |
|---|---|---|---|
| Tecnologia | Framework applicazione | Django | Approvato come base ufficiale. |
| Database | Database principale | PostgreSQL | Approvato come base ufficiale. |
| Accesso | Solo rete locale o anche remoto | Locale, VPN, esposizione web | Per sicurezza, accesso remoto solo via VPN. |
| Documenti | Stile template | Sobrio tecnico, piu commerciale, personalizzato | Sprint 12 permette di caricare template personalizzati; layout finale e brand restano da validare con esempi reali. |
| Fiscalita | Dicitura definitiva documenti | Consulenza tecnica, prestazione, altro | Da validare con commercialista. |
| Interfaccia | Stile visivo | Sobrio operativo, tecnico, commerciale | Da decidere prima della realizzazione grafica. |
| Prodotto | Priorita listini/AI | MVP immediato o fase successiva | Da decidere dopo il primo flusso preventivo completo. |
| Prodotto | Implementazione documenti contrattuali cliente | Fase successiva | NDA, accordi quadro, condizioni particolari e allegati commerciali. |
| Prodotto | Manuale operativo nel gestionale | Markdown nel repository, pagine Django, soluzione ibrida | Prima bozza in `docs/MANUALE_OPERATIVO.md`; da decidere se esporlo anche nella sidebar. |
| Infrastruttura | Avvio automatico BMAX | Restart policy Docker Compose, servizio systemd opzionale | Prima stabilizzazione scelta e verificata: `restart: unless-stopped`; systemd resta piano B se emergono problemi futuri. |
| Infrastruttura | Nome locale BMAX | `b3d-gestionale.local:8000` | Prima scelta operativa verificata sulla rete reale tramite Avahi/mDNS. |
| File tecnici | Archivio originale e preview G-code/3MF | Salvataggio file, preview, riconoscimento slicer avanzato | Sprint 17 copre il primo import dati utile; restano da progettare conservazione file e anteprime. |
| Backup | Copia fuori dal BMAX | Disco esterno, NAS, cloud privato | Lo Sprint 18 crea backup locali automatici verificati; resta da decidere dove conservarne una copia esterna. |

## Note

Le decisioni possono cambiare, ma ogni cambio deve essere motivato e registrato.
