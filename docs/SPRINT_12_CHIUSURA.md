# Chiusura Sprint 12

## Titolo

Gestione template DOCX da interfaccia.

## Obiettivo

Rendere gestibili dalla sezione **Documenti** i template Word usati per generare DOCX/PDF, senza passare dall'admin tecnico.

Il problema pratico era poter caricare, sostituire o disattivare un modello documento quando cambia layout o versione, mantenendo chiaro quale template verra usato nelle prossime generazioni.

## Risultato

La sezione **Documenti** ora permette di:

- caricare un nuovo template DOCX;
- modificare un template esistente;
- scaricare il file DOCX originale;
- attivare un template;
- disattivare un template;
- vedere tipo documento, profilo, versione, note e stato.

Il sistema mantiene un solo template attivo per tipo documento. Quando viene attivato un template, gli altri template dello stesso tipo vengono disattivati.

I template personalizzati attivi hanno priorita sui template base generati dal gestionale per:

- proposta cliente consulenza;
- scheda interna dettagliata.

Se non esiste un template personalizzato attivo, il gestionale continua a usare i template base gia disponibili.

## Decisione Di Prodotto

La gestione template entra nel flusso operativo della sezione **Documenti**.

Il modello dati non cambia: i template restano collegati al tipo documento e i documenti generati continuano a usare i dati del preventivo, della configurazione scelta e del profilo dati documento attivo.

La prima versione controlla il formato `.docx`, ma non valida ancora automaticamente tutti i segnaposto interni al file. Per ora il controllo finale resta generare un documento di prova e verificarlo.

## Verifiche

- Controllo Django con `manage.py check`: completato.
- Test automatici `apps.documents`: completati, 8 test.
- Test caricamento template da interfaccia: completato.
- Test rifiuto file non `.docx`: completato.
- Test attivazione con disattivazione degli altri template dello stesso tipo: completato.
- Test priorita template personalizzato rispetto al template base: completato.
- Controllo documentazione: completato.

## Documentazione Aggiornata

- `docs/DECISIONI.md`
- `docs/APPROVAZIONI.md`
- `docs/REQUISITI_MVP.md`
- `docs/SCHERMATE_E_FLUSSI.md`
- `docs/MANUALE_OPERATIVO.md`
- `docs/BOARD_SPRINT_12.md`

## Prossimo Sprint Proposto

**Sprint 13 - Validazione template e prova documento reale**

Obiettivo pratico: aiutare l'operatore a capire se un template DOCX caricato contiene i segnaposto necessari e verificare il risultato su un preventivo reale o demo prima dell'invio.

## Da Riprendere In Futuro

- Validazione guidata dei segnaposto disponibili e mancanti.
- Anteprima PDF direttamente dalla pagina template.
- Template fornitura/artigiano.
- Storico approvativo delle versioni template.
- Layout definitivo di brand con logo reale.
