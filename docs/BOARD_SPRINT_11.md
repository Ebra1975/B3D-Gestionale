# Board Sprint 11 - Rifinitura layout PDF cliente/interno

Questo board raccoglie lo stato operativo dello Sprint 11.

## Obiettivo

Rifinire i template base usati per generare proposta cliente consulenza e scheda interna dettagliata.

Il problema pratico e ottenere documenti piu leggibili nel flusso reale: una proposta cliente pronta da controllare prima dell'invio e una scheda interna utile per verificare costi, margine, ipotesi operative e note.

## In Corso / Completato

| Tema | Stato | Problema Pratico Da Risolvere | Esito |
|---|---|---|---|
| Template cliente consulenza | Completato come prima rifinitura | Rendere la proposta piu presentabile senza esporre i costi interni. | Aggiornato template base a versione v3 con intestazione, contatti, riepilogo compatto, sezione tecnica e sintesi economica. |
| Template interno dettagliato | Completato come prima rifinitura | Rendere piu rapido il controllo di costo, margine, voci e note. | Aggiornato template interno a versione v2 con riepilogo, economia interna, voci di costo con note e controlli. |
| Separazione dati | Completato | Evitare duplicazioni tra documento cliente e documento interno. | Entrambi i template continuano a usare gli stessi dati del preventivo e della configurazione scelta. |
| Test | Completato | Verificare che i nuovi template vengano usati nella generazione. | Aggiornati test automatici `apps.documents`, 4 test completati. |
| Documentazione | Completato | Tracciare la decisione e lo stato del layout. | Aggiornati decisioni, approvazioni, schermate e flussi. |

## Fuori Ambito Per Ora

| Tema | Motivo |
|---|---|
| Layout definitivo di brand | Serve validare il risultato su esempi reali, logo definitivo e preferenze grafiche. |
| Gestione template DOCX da interfaccia non amministrativa | Rimane uno sviluppo successivo: Sprint 11 rifinisce i template base generati automaticamente. |
| Nuovi dati o campi documento | Non necessari per la rifinitura del layout e richiederebbero approvazione sul modello dati. |

## Verifiche Previste

- Test automatici mirati `apps.documents`: completati.
- Controllo che proposta cliente e scheda interna restino documenti separati: completato.
- Controllo documentazione: completato.

## Criterio Di Chiusura

Lo sprint e considerato chiuso quando il gestionale genera una proposta consulenza e una scheda interna con layout base piu leggibile, usando gli stessi dati economici del preventivo e mantenendo il dettaglio costi solo nel documento interno.

## Chiusura Definitiva

Sprint 11 chiuso definitivamente il 2026-07-08.

Il prossimo sprint consigliato e **Sprint 12 - Gestione template DOCX da interfaccia**.
