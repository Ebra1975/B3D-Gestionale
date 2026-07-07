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

## Decisioni Da Prendere

| Area | Tema | Opzioni | Note |
|---|---|---|---|
| Tecnologia | Framework applicazione | Django | Approvato come base ufficiale. |
| Database | Database principale | PostgreSQL | Approvato come base ufficiale. |
| Accesso | Solo rete locale o anche remoto | Locale, VPN, esposizione web | Per sicurezza, accesso remoto solo via VPN. |
| Documenti | Stile template | Sobrio tecnico, piu commerciale, personalizzato | Da definire con esempi reali. |
| Fiscalita | Dicitura definitiva documenti | Consulenza tecnica, prestazione, altro | Da validare con commercialista. |
| Interfaccia | Stile visivo | Sobrio operativo, tecnico, commerciale | Da decidere prima della realizzazione grafica. |
| Prodotto | Priorita listini/AI | MVP immediato o fase successiva | Da decidere dopo il primo flusso preventivo completo. |
| Prodotto | Implementazione documenti contrattuali cliente | Fase successiva | NDA, accordi quadro, condizioni particolari e allegati commerciali. |
| Prodotto | Manuale operativo nel gestionale | Markdown nel repository, pagine Django, soluzione ibrida | Prima bozza in `docs/MANUALE_OPERATIVO.md`; da decidere se esporlo anche nella sidebar. |

## Note

Le decisioni possono cambiare, ma ogni cambio deve essere motivato e registrato.
