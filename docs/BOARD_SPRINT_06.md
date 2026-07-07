# Board Sprint 06

Questo board raccoglie lo stato operativo dello Sprint 06.

## Obiettivo

Rendere la dashboard piu utile nel lavoro quotidiano, trasformandola nel punto iniziale da cui capire cosa seguire.

Il problema pratico e ridurre il rischio di dimenticare preventivi in scadenza, consegne vicine, accordi cliente o documenti commerciali da controllare.

## In Corso / Completato

| Tema | Stato | Problema Pratico Risolto | Esito |
|---|---|---|---|
| Dashboard operativa | Completato come prima versione | Vedere subito le attivita da seguire senza aprire ogni archivio. | Aggiunto blocco **Da seguire** con preventivi, commesse e memoria commerciale in scadenza. |
| Preventivi in scadenza | Completato | Evitare che una proposta inviata o in revisione superi la validita senza controllo. | Mostrati i preventivi aperti con validita entro 14 giorni o gia superata. |
| Consegne commesse | Completato | Tenere sotto controllo lavori con consegna vicina o scaduta. | Mostrate le commesse attive con consegna prevista entro 14 giorni o gia superata. |
| Memoria commerciale | Completato | Ricordare accordi e documenti cliente da rinnovare o verificare. | Mostrati accordi e documenti commerciali con scadenza entro 30 giorni o gia superata. |
| Test automatico | Completato | Verificare che la dashboard includa i promemoria principali. | Aggiunto test della dashboard operativa. |
| Documentazione | Completato | Tenere allineate decisioni, approvazioni, manuale e schermate. | Aggiornati documenti collegati allo sprint. |

## Fuori Ambito Per Ora

| Tema | Motivo |
|---|---|
| Notifiche automatiche via email o messaggi | Prima serve verificare se la dashboard basta nel lavoro quotidiano. |
| Calendario completo | Sarebbe utile, ma puo complicare l'interfaccia della prima versione. |
| Regole configurabili dall'utente | Per ora le soglie 14/30 giorni sono semplici e comprensibili. |
| Cambio automatico stato preventivo a scaduto | Richiede una regola di processo separata e va approvata prima. |

## Verifiche Previste

- Controllo Django con `manage.py check`.
- Test automatici della dashboard.
- Apertura dashboard dal browser.
- Verifica visiva che le liste restino leggibili su desktop e mobile.

## Criterio Di Chiusura

Lo sprint e considerato chiuso quando la dashboard mostra correttamente le cose da seguire e la documentazione spiega il nuovo uso operativo.
