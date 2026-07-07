# Board Sprint 02

Questo board raccoglie i temi emersi durante lo Sprint 02, separando cio che e in lavorazione da cio che va ragionato prima di diventare funzione.

## In Lavorazione

| Tema | Stato | Problema Pratico | Prossimo Passo |
|---|---|---|---|
| Flusso preventivo consulenza DOCX/PDF | In corso | Generare una proposta cliente partendo dai dati interni del preventivo. | Usare il preventivo demo realistico `B3D-2026-001` per verificare il flusso. |
| Dettaglio preventivo operativo | In corso | Capire subito se un preventivo e pronto o cosa manca. | Rifinire dati di esempio e controlli utili. |
| Dati demo realistici | In corso | Testare il gestionale con dati piu vicini al lavoro reale rispetto a `TEST-001`. | Creare/aggiornare il caso demo con `python manage.py seed_demo_data --with-documents`. |
| Azioni rapide stato preventivo | In corso | Aggiornare lo stato dopo invio o risposta cliente senza riaprire il form completo. | Verificare sul preventivo demo il passaggio a Inviato, Da rivedere, Accettato o Rifiutato. |
| Creazione commessa da preventivo | In corso | Trasformare un preventivo accettato in lavoro operativo senza ricopiare dati. | Verificare con il preventivo demo e poi aggiungere dettaglio commessa. |

## Da Ragionare

| Tema | Stato | Problema Pratico | Note |
|---|---|---|---|
| Manuale operativo per operatore | Da progettare | Spiegare passo passo come usare il gestionale nelle operazioni quotidiane, per esempio come fare un preventivo. | Partire con documenti Markdown nel repository e valutare poi una sezione "Manuale" dentro il gestionale. |

## Idee Per Il Manuale Operativo

Contenuti possibili:

- come creare un cliente;
- come fare un preventivo consulenza;
- come inserire configurazioni tecniche;
- come generare costi interni;
- come generare DOCX e PDF;
- come controllare cosa manca prima dell'invio;
- checklist materiali e tecnologie;
- come trasformare un preventivo accettato in commessa;
- come gestire documenti e template.

Prime domande da decidere:

- nella prima versione basta un manuale in `docs/` oppure serve gia una voce "Manuale" nella sidebar?
- il manuale deve essere stampabile in PDF?
- ogni schermata deve avere un link alla procedura relativa?
- quali procedure servono prima dell'installazione sul BMAX?
