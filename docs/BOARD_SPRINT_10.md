# Board Sprint 10 - Modifica dati documento da interfaccia

Questo board raccoglie lo stato operativo dello Sprint 10.

## Obiettivo

Permettere di modificare i dati usati nei documenti DOCX/PDF dalla sezione **Documenti**, senza entrare nell'admin tecnico.

Il problema pratico e poter correggere intestazione azienda, contatti, condizioni standard, nota fiscale/commerciale e nota interna prima di generare una proposta reale per il cliente.

## In Corso / Completato

| Tema | Stato | Problema Pratico Da Risolvere | Esito |
|---|---|---|---|
| Modifica dati documento | Completato come prima versione | Aggiornare i dati riutilizzati nei documenti senza usare l'admin. | Aggiunta pagina **Modifica dati documento** collegata al profilo attivo. |
| Centralizzazione dati | Completato | Evitare duplicazioni tra proposta cliente, scheda interna e template. | La generazione continua a usare `DocumentProfile.get_active()`. |
| Flusso operatore | Completato | Rendere chiaro quando aggiornare i dati prima di generare DOCX/PDF. | Aggiornato manuale operativo e sezione Documenti. |
| Test | Completato | Verificare che il profilo attivo sia modificabile da interfaccia. | Aggiunto test automatico dedicato in `apps.documents`. |
| Documentazione | Completato | Chiudere lo sprint con decisioni, approvazioni, manuale e flussi allineati. | Aggiornati documenti principali e aggiunta chiusura sprint. |

## Fuori Ambito Per Ora

| Tema | Motivo |
|---|---|
| Gestione completa dei template DOCX da interfaccia | La priorita dello sprint era modificare i dati documento, non caricare o versionare template personalizzati. |
| Layout grafico definitivo dei PDF | Richiede esempi reali e validazione del formato cliente/interno. |
| Piu profili documento attivi selezionabili | Per la prima versione basta un profilo attivo centrale, coerente con l'uso singolo. |

## Verifiche Previste

- Controllo Django con `manage.py check`: completato.
- Test automatici mirati `apps.documents`: completati.
- Apertura pagina modifica dati documento dal server locale: completata.
- Controllo documentazione: completato.

## Criterio Di Chiusura

Lo sprint e considerato chiuso quando l'operatore puo aprire **Documenti**, modificare il profilo dati attivo e generare successivamente documenti che useranno quei dati aggiornati.

## Chiusura Definitiva

Sprint 10 chiuso definitivamente il 2026-07-08.

Il prossimo sprint consigliato e **Sprint 11 - Template documenti e layout PDF**.
