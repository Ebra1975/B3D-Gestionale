# Board Sprint 03

Questo board raccoglie lo stato operativo dello Sprint 03.

## Obiettivo

Consolidare il flusso post-accettazione e preparare il gestionale a essere piu usabile negli archivi principali.

## In Corso / Completato

| Tema | Stato | Problema Pratico Risolto | Esito |
|---|---|---|---|
| Dettaglio commessa | Completato come prima versione | Seguire il lavoro dopo accettazione senza tornare sempre al preventivo. | Aggiunta scheda commessa con stato, date, note, cliente, preventivo, configurazione, costi previsti e documenti collegati. |
| Modifica dati commessa | Completato come prima versione | Aggiornare stato, date e note operative durante il lavoro. | Aggiunta pagina di modifica commessa. |
| Collegamento lista commesse | Completato | Aprire rapidamente una commessa dalla lista. | Il numero commessa porta al dettaglio. |
| Ricerca su clienti | Completato | Trovare clienti senza scorrere tutta la lista. | Ricerca per nome, referente, email, telefono, dati fiscali e note. |
| Ricerca su materiali | Completato | Trovare materiali per uso tecnico o fornitore. | Ricerca per nome, tipo, marca, colore, fornitore e note. |
| Ricerca su stampanti | Completato | Trovare rapidamente macchine o strumentazione. | Ricerca per nome, modello, volume/materiali e note. |
| Ricerca su documenti | Completato | Recuperare template e documenti generati. | Ricerca per template, preventivo, cliente e oggetto. |
| Formula prezzo/margine base | Completato come prima versione | Rendere il prezzo finale piu ripetibile partendo dai costi interni. | Aggiunto calcolo con costo interno, margine percentuale, arrotondamento e voce interna "Margine commerciale". |
| Backup locale | Completato come prima versione | Salvare dati e file durante lo sviluppo. | Aggiunto comando `python manage.py backup_local`, verificato con creazione zip. |
| Procedura backup/ripristino | Completato come prima bozza | Sapere cosa salvare e come ripristinare. | Creato `docs/BACKUP_E_RIPRISTINO.md` per Windows locale e BMAX Docker/PostgreSQL. |
| Procedura BMAX Linux Server | Completato come prima bozza | Preparare il passaggio al mini PC in rete locale. | Creato `docs/INSTALLAZIONE_BMAX_LINUX.md`. |
| Template consulenza base v2 | Completato come prima rifinitura | Rendere la proposta cliente piu leggibile senza esporre i costi interni. | Migliorato template automatico con intestazione, riepilogo, sezione tecnica, tabella economica sintetica e nota fiscale da validare. |
| Procedura GitHub | Completato | Preparare il ponte tra sviluppo Windows e BMAX. | Creato `docs/GITHUB_E_VERSIONAMENTO.md`, configurato remote `origin` e inviato `master` su GitHub. |

## Ancora Da Fare Nello Sprint 03

| Tema | Motivo |
|---|---|
| Layout DOCX definitivo di brand | Il template v2 e una base piu ordinata, ma resta sostituibile con modello personalizzato. |
| Backup automatico BMAX | Dopo la procedura manuale serve automatizzare frequenza e rotazione. |

## Verifiche Eseguite

- `python manage.py check` con esito positivo.
- Compilazione Python di `config` e `apps` con esito positivo.
- Apertura pagine clienti, materiali, stampanti, documenti, dettaglio commessa e modifica commessa con esito positivo.
- Applicazione regola prezzo/margine verificata su configurazione demo: costo interno 434,34 EUR, margine 30%, arrotondamento 5 EUR, totale 565 EUR.
- Backup locale verificato con creazione archivio zip in `backups/` e 31 file inclusi.
- Template consulenza base aggiornato a v2 e verificato generando DOCX/PDF consulenza v3 per il preventivo demo `B3D-2026-001`.
