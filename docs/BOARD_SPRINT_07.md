# Board Sprint 07

Questo board raccoglie lo stato operativo dello Sprint 07.

## Obiettivo

Portare la memoria commerciale cliente dentro il lavoro sul preventivo.

Il problema pratico e ridurre il rischio di preparare o inviare una proposta senza controllare accordi attivi, listini collegati, NDA o documenti commerciali in scadenza.

## In Corso / Completato

| Tema | Stato | Problema Pratico Risolto | Esito |
|---|---|---|---|
| Memoria commerciale nel preventivo | Completato | Vedere accordi e documenti cliente mentre si prepara la proposta. | Aggiunto riquadro nel dettaglio preventivo. |
| Avvisi commerciali | Completato | Notare accordi o documenti scaduti o vicini alla scadenza. | Evidenza entro 30 giorni o gia scaduti. |
| Collegamento scheda cliente | Completato | Aprire rapidamente il cliente per aggiornare accordi e documenti. | Aggiunto link diretto alla scheda cliente. |
| Test automatico | Completato | Verificare che la memoria commerciale produca gli avvisi previsti. | Aggiunto test in `apps.estimates`. |
| Documentazione | Completato | Mantenere allineati decisioni, approvazioni, manuale e schermate. | Aggiornati documenti collegati allo sprint. |

## Fuori Ambito Per Ora

| Tema | Motivo |
|---|---|
| Applicazione automatica degli accordi al prezzo | Richiede listini strutturati e regole prezzo approvate. |
| Firma o gestione avanzata NDA | Prima basta archiviare e ricordare i documenti. |
| Notifiche automatiche | La dashboard e il dettaglio preventivo coprono gia il controllo manuale iniziale. |

## Verifiche Previste

- Controllo Django con `manage.py check`.
- Test automatico `apps.estimates`.
- Verifica visiva del dettaglio preventivo.

## Criterio Di Chiusura

Lo sprint e considerato chiuso quando il preventivo mostra gli accordi e i documenti commerciali del cliente senza applicare automatismi economici.
