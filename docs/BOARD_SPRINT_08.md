# Board Sprint 08 - Prezzo assistito e condizioni cliente

Questo board raccoglie lo stato operativo dello Sprint 08.

## Obiettivo

Rendere piu guidata la revisione economica del preventivo usando la memoria commerciale del cliente.

Il problema pratico e aiutare il titolare a controllare condizioni, listini collegati, accordi e note commerciali prima di confermare il prezzo finale, senza applicare modifiche automatiche e senza duplicare i dati economici.

## In Corso / Completato

| Tema | Stato | Problema Pratico Da Risolvere | Esito |
|---|---|---|---|
| Prezzo assistito | Completato come prima versione | Evidenziare se nel cliente ci sono condizioni commerciali da considerare prima del prezzo finale. | Lo stato preventivo avvisa quando la memoria commerciale esiste ma non e stata confermata. |
| Revisione condizioni cliente | Completato come prima versione | Rendere chiaro quali accordi o listini sono solo promemoria e quali sono stati considerati nel preventivo. | Aggiunta conferma manuale nel riquadro memoria commerciale. |
| Tracciabilita della revisione | Completato come prima versione | Lasciare memoria interna del controllo fatto dal titolare senza cambiare automaticamente i prezzi. | Salvate data e note interne di revisione condizioni cliente sul preventivo. |
| Documentazione | Completato come prima versione | Mantenere allineati decisioni, approvazioni, manuale e schermate se il flusso cambia. | Aggiornati board, decisioni, approvazioni, manuale operativo e flussi. |

## Fuori Ambito Per Ora

| Tema | Motivo |
|---|---|
| Applicazione automatica degli accordi al prezzo | Richiede listini strutturati, regole approvate e tracciabilita completa della fonte prezzo. |
| Motore listini completo | Puo diventare complesso; prima serve capire il controllo minimo utile nel flusso reale. |
| AI decisionale sui prezzi | L'AI resta copilota operativo, non decisore autonomo. |

## Verifiche Previste

- Controllo Django con `manage.py check`: completato.
- Test automatici mirati `apps.estimates`: completati.
- Apertura dettaglio preventivo dal server locale: completata.
- Controllo documentazione: completato per la prima versione.

## Criterio Di Chiusura

Lo sprint e considerato chiuso quando il preventivo aiuta a rivedere condizioni cliente e prezzo finale in modo tracciabile, mantenendo obbligatoria la conferma manuale del titolare.
