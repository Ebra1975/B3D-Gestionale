# Board Sprint 05

Questo board raccoglie lo stato operativo dello Sprint 05.

## Obiettivo

Preparare l'uso reale del gestionale sul mini PC BMAX, con procedure semplici per installazione, backup, ripristino, GitHub e manutenzione ordinaria.

Il problema pratico e ridurre il rischio di perdere dati o restare bloccati quando il gestionale passa dallo sviluppo Windows al server locale.

## In Corso / Completato

| Tema | Stato | Problema Pratico Risolto | Esito |
|---|---|---|---|
| Installazione BMAX | Completato come procedura | Sapere quali passaggi fare per avviare il gestionale in rete locale. | Aggiornata procedura con checklist, primo avvio, avvio stabile e controlli dopo installazione. |
| Backup BMAX | Completato come procedura manuale | Salvare database, allegati/documenti e configurazione prima dell'uso reale. | Aggiornata procedura distinguendo sviluppo Windows, Docker Compose e volumi Docker. |
| Ripristino BMAX | Completato come prova obbligatoria | Verificare che un backup sia davvero utilizzabile, non solo creato. | Inserita procedura di ripristino su installazione di prova prima dei dati reali. |
| GitHub | Completato come routine operativa | Tenere ordinato il passaggio tra sviluppo Windows e server BMAX. | Aggiornata routine: verifica, commit, push, pull sul BMAX, migrazioni e riavvio. |
| Manutenzione | Completato come prima procedura | Avere una lista chiara di controlli settimanali, mensili e prima degli aggiornamenti. | Aggiunto documento `docs/PROCEDURA_MANUTENZIONE.md`. |
| Documentazione | Completato | Tracciare decisioni e requisiti dello sprint. | Aggiornati decisioni, approvazioni e riferimenti README. |

## Fuori Ambito Per Ora

| Tema | Motivo |
|---|---|
| Automazione completa del backup BMAX | Prima serve provare manualmente backup e ripristino sul BMAX reale. |
| Esposizione internet diretta | Non necessaria per la prima versione e piu rischiosa. Accesso remoto solo via VPN. |
| Monitoraggio avanzato | Utile in futuro, ma per ora bastano controlli semplici e leggibili. |
| Servizio systemd definitivo | Da configurare dopo prova concreta sul BMAX, se Docker Compose non viene gia gestito all'avvio. |
| Migrazione completa dei dati Windows verso PostgreSQL | Da fare solo quando si decide il primo passaggio reale in produzione. |

## Verifiche Previste Sul BMAX

- Clone del repository GitHub.
- Creazione `.env` con password non predefinite.
- Avvio `docker compose up -d --build`.
- Migrazioni Django.
- Creazione utente amministratore.
- Apertura da altro PC della rete locale.
- Generazione di almeno un documento DOCX/PDF.
- Backup manuale database e media.
- Ripristino su copia di prova.

## Criterio Di Chiusura

Lo sprint e considerato chiuso a livello documentale quando l'utente ha una procedura unica per:

- installare;
- aggiornare;
- salvare;
- ripristinare;
- controllare lo stato del gestionale.

La chiusura tecnica definitiva richiede una prova reale sul BMAX.
