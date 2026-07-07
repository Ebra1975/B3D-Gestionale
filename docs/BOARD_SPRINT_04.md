# Board Sprint 04

Questo board raccoglie lo stato operativo dello Sprint 04.

## Obiettivo

Iniziare la memoria commerciale del cliente senza complicare ancora il calcolo automatico dei preventivi.

Il problema pratico e evitare che accordi, NDA, listini firmati, condizioni particolari e scadenze restino sparsi fuori dal gestionale o nascosti nelle note libere.

## In Corso / Completato

| Tema | Stato | Problema Pratico Risolto | Esito |
|---|---|---|---|
| Scheda cliente | Completato come prima versione | Vedere in un solo punto dati cliente, note, preventivi, commesse e memoria commerciale. | Aggiunta pagina dettaglio cliente raggiungibile dalla lista clienti. |
| Accordi cliente | Completato come prima versione | Registrare condizioni commerciali, listino collegato, validita e stato dell'accordo. | Aggiunto archivio accordi cliente con creazione, modifica e visualizzazione in scheda cliente. |
| Documenti commerciali cliente | Completato come prima versione | Conservare NDA, accordi firmati, listini firmati e allegati commerciali collegati al cliente. | Aggiunto archivio documenti commerciali con file allegato, stato, date e scadenza. |
| Admin | Completato | Gestire i nuovi dati anche dal pannello amministratore Django. | Aggiunti accordi e documenti commerciali cliente all'admin. |
| Documentazione | Completato | Tenere allineate decisioni, approvazioni, manuale e modello dati. | Aggiornati documenti di progetto collegati allo sprint. |

## Fuori Ambito Per Ora

| Tema | Motivo |
|---|---|
| Listino completo con voci prezzo | Richiede una progettazione dedicata per non duplicare il dettaglio economico dei preventivi. |
| Applicazione automatica accordo al preventivo | La prima versione deve solo mostrare e conservare la memoria commerciale; la decisione resta manuale. |
| Avvisi automatici su accordi/documenti in scadenza | Utile, ma da aggiungere dopo aver verificato l'uso reale della scheda cliente. |
| Layout grafico definitivo di brand | Resta separato dalle funzioni operative di memoria cliente. |
| Backup automatico BMAX | Rimane un tema infrastrutturale da affrontare in uno sprint dedicato. |

## Verifiche Eseguite

- `python manage.py check` con esito positivo.
- Migrazione `customers.0002_customeragreement_customercommercialdocument` applicata al database locale.
- Controllo migrazioni residue con esito `No changes detected`.
- Compilazione Python di `config` e `apps` con esito positivo.
- Apertura lista clienti con esito HTTP 200.
- Apertura scheda cliente con esito HTTP 200.
- Apertura form nuovo accordo cliente con esito HTTP 200.
- Apertura form nuovo documento commerciale cliente con esito HTTP 200.
- Creazione e cancellazione di un accordo cliente di prova con esito positivo.
- Creazione e cancellazione di un documento commerciale cliente di prova con esito positivo.

## Verifiche Rimaste Manuali

- Upload e apertura di un file allegato reale da browser.
