# Board Sprint 02

Questo board raccoglie lo stato finale dello Sprint 02.

## Completato

| Tema | Stato | Problema Pratico Risolto | Esito |
|---|---|---|---|
| Flusso preventivo consulenza DOCX/PDF | Completato | Generare una proposta cliente partendo dai dati interni del preventivo. | Dal dettaglio preventivo si genera DOCX consulenza e PDF. |
| Dettaglio preventivo operativo | Completato | Capire subito se un preventivo e pronto o cosa manca. | Aggiunto riquadro stato preventivo con totale, configurazione usata, ultimo documento e controlli. |
| Dati demo realistici | Completato | Testare il gestionale con dati piu vicini al lavoro reale rispetto a `TEST-001`. | Aggiunto comando `python manage.py seed_demo_data --with-documents` e preventivo demo `B3D-2026-001`. |
| Azioni rapide stato preventivo | Completato | Aggiornare lo stato dopo invio o risposta cliente senza riaprire il form completo. | Aggiunte azioni Inviato, Da rivedere, Accettato e Rifiutato. |
| Creazione commessa da preventivo | Completato | Trasformare un preventivo accettato in lavoro operativo senza ricopiare dati. | Aggiunta creazione commessa dal preventivo accettato. |
| Ricerca e filtri liste | Completato | Trovare rapidamente preventivi e commesse, distinguendo quelli ancora da lavorare da quelli convertiti. | Aggiunti ricerca e filtri a preventivi e commesse; preventivi in commessa attenuati e filtrabili. |
| Manuale operativo per operatore | Completato come prima bozza | Spiegare passo passo come usare il gestionale nelle operazioni quotidiane. | Aggiunto `docs/MANUALE_OPERATIVO.md` e pagina Manuale nella sidebar. |

## Rimandato A Sprint 03

| Tema | Motivo |
|---|---|
| Dettaglio commessa | Serve dopo il primo collegamento preventivo-commessa. |
| Ricerca su clienti, materiali, stampanti e documenti | Ricerca avviata su preventivi e commesse, da estendere alle altre liste. |
| Formula prezzo/margine piu strutturata | Il flusso usa costi interni e margine manuale, ma serve una regola piu solida. |
| Layout DOCX consulenza piu curato | Il template base funziona, ma il layout finale resta da progettare. |
| Procedura BMAX, backup e ripristino | Tema infrastrutturale da affrontare dopo il flusso preventivo. |
| UX piu giovane e accattivante | Da valutare con skill dedicata, Lovable o revisione UI dopo consolidamento funzionale. |

## Verifica Documentazione

Controllati e aggiornati:

- `docs/DECISIONI.md`;
- `docs/APPROVAZIONI.md`;
- `docs/SCHERMATE_E_FLUSSI.md`;
- `docs/MANUALE_OPERATIVO.md`;
- `docs/BOARD_SPRINT_02.md`.
