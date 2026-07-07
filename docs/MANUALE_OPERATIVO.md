# Manuale Operativo

Questo manuale spiega come usare il gestionale B3D Lab nelle operazioni quotidiane.

Non e documentazione tecnica per sviluppatori: serve all'operatore per sapere cosa fare, in che ordine farlo e cosa controllare prima di passare allo step successivo.

## Procedure Disponibili

| Procedura | Stato | Scopo |
|---|---|---|
| Fare un preventivo consulenza | Bozza iniziale | Creare un preventivo completo e generare DOCX/PDF cliente. |
| Usare il preventivo demo | Bozza iniziale | Provare il flusso senza usare dati reali di clienti. |
| Creare una commessa da preventivo accettato | Bozza iniziale | Avviare il lavoro operativo dopo accettazione cliente. |
| Aggiornare una commessa | Bozza iniziale | Seguire stato, date e note del lavoro operativo. |
| Applicare prezzo e margine | Bozza iniziale | Generare un totale proposta piu ripetibile partendo dai costi interni. |
| Fare un backup locale | Bozza iniziale | Salvare dati e documenti durante lo sviluppo. |

## Procedura - Usare Il Preventivo Demo

### Quando Usarla

Usare questa procedura per provare il gestionale, fare verifiche o mostrare il flusso senza inserire dati reali.

### Passi Operativi

1. Aprire la sezione **Preventivi**.
2. Cercare il preventivo `B3D-2026-001`.
3. Aprire il dettaglio preventivo.
4. Controllare il riquadro **Stato preventivo**.
5. Verificare che siano presenti totale, prezzo unitario e configurazione scelta.
6. Generare il **DOCX consulenza** se serve una nuova versione del documento.
7. Scaricare DOCX e PDF per verificare il risultato.

### Nota

Il preventivo demo non rappresenta un cliente reale. Serve solo a testare il flusso operativo.

## Procedura - Creare Una Commessa Da Preventivo Accettato

### Quando Usarla

Usare questa procedura quando il cliente conferma un preventivo e il lavoro deve diventare una commessa operativa.

### Passi Operativi

1. Aprire il preventivo confermato dal cliente.
2. Verificare che la configurazione scelta sia corretta.
3. Usare l'azione rapida **Accettato**.
4. Nel riquadro **Stato preventivo**, usare **Crea commessa**.
5. Aprire la sezione **Commesse**.
6. Aprire la commessa appena creata.
7. Verificare cliente, preventivo collegato e configurazione scelta.
8. Aggiornare date operative e note dalla pagina **Aggiorna commessa**.
9. Tornare alla lista **Preventivi** e verificare che il preventivo sia filtrabile tra quelli convertiti in commessa.

### Ricerca E Filtri

- Nella lista **Preventivi**, usare la vista **Da lavorare** per nascondere i preventivi gia diventati commessa.
- Usare **Convertiti in commessa** per recuperare i preventivi gia trasformati in lavoro operativo.
- Nella lista **Commesse**, usare la ricerca per numero commessa, cliente o preventivo.
- Nelle liste **Clienti**, **Materiali**, **Stampanti** e **Documenti**, usare il campo **Cerca** per ritrovare rapidamente i dati gia inseriti.

### Risultato Atteso

Il gestionale crea una commessa collegata al preventivo, al cliente e alla configurazione scelta.

## Procedura - Aggiornare Una Commessa

### Quando Usarla

Usare questa procedura mentre il lavoro avanza, ad esempio quando passa in progettazione, stampa, post-processing o consegna.

### Passi Operativi

1. Aprire la sezione **Commesse**.
2. Cercare la commessa per numero, cliente o preventivo.
3. Aprire il dettaglio commessa.
4. Controllare stato, cliente, preventivo origine e configurazione confermata.
5. Controllare i costi previsti interni ereditati dalla configurazione.
6. Usare **Aggiorna commessa**.
7. Modificare stato, data avvio, consegna prevista, data consegna e note operative.
8. Salvare.

### Risultato Atteso

La commessa mostra lo stato operativo aggiornato e resta collegata ai dati del preventivo senza ricopiare informazioni.

## Procedura - Fare Un Preventivo Consulenza

### Quando Usarla

Usare questa procedura quando arriva una richiesta cliente da trasformare in una proposta di consulenza tecnica, progettazione, validazione e realizzazione.

### Obiettivo

Arrivare a un preventivo con:

- cliente collegato;
- dati generali compilati;
- almeno una configurazione tecnica;
- costi interni presenti;
- totale configurazione diverso da zero;
- proposta cliente generata in `.docx` e PDF.

### Passi Operativi

1. Aprire la sezione **Clienti**.
2. Verificare se il cliente esiste gia.
3. Se il cliente non esiste, creare una nuova scheda cliente.
4. Aprire la sezione **Preventivi**.
5. Creare un nuovo preventivo.
6. Inserire numero, cliente, oggetto, data, quantita e descrizione della richiesta.
7. Lasciare il profilo documento su **Consulenza**, salvo caso diverso.
8. Salvare il preventivo.
9. Aggiungere una configurazione tecnica.
10. Compilare nome configurazione, descrizione, materiale, stampante/strumentazione, processo, quantita e dati tecnici disponibili.
11. Se la configurazione e quella da proporre al cliente, marcarla come scelta.
12. Generare i costi automatici disponibili:
    - costo materiale;
    - costo macchina;
    - setup/progettazione.
13. Completare manualmente eventuali importi mancanti, soprattutto setup, progettazione, post-processing, trattamenti o margine.
14. Applicare la regola prezzo/margine se serve un margine percentuale con arrotondamento.
15. Tornare al dettaglio preventivo.
16. Controllare il riquadro **Stato preventivo**.
17. Risolvere gli elementi indicati in **Da fare prima della proposta**.
18. Controllare gli avvisi in **Da controllare**.
19. Quando il totale e coerente, generare il **DOCX consulenza**.
20. Scaricare e controllare il DOCX.
21. Scaricare e controllare il PDF.
22. Se il documento e corretto, usare l'azione rapida **Segna inviato** nel dettaglio preventivo.

### Controlli Prima Di Inviare

Prima di inviare una proposta al cliente, verificare:

- il cliente e corretto;
- l'oggetto descrive bene il lavoro;
- la descrizione e comprensibile;
- la configurazione scelta e quella giusta;
- il totale non e zero;
- il prezzo unitario ha senso rispetto alla quantita;
- il documento cliente non mostra il dettaglio economico interno;
- eventuali diciture fiscali o commerciali importanti sono da validare con commercialista se non gia confermate.
- dopo l'invio, lo stato del preventivo e aggiornato a **Inviato**.
- il layout DOCX/PDF e leggibile e non contiene dettagli economici interni.

### Cosa Non Fare

- Non duplicare i dati economici in documenti esterni.
- Non modificare a mano il PDF come fonte principale.
- Non inviare al cliente la vista interna dettagliata.
- Non usare il documento consulenza per casistiche di fornitura/artigiano senza revisione del profilo.

### Template Consulenza Base

Il gestionale usa un template consulenza base v2 se non viene caricato un template personalizzato.

Il template contiene:

- intestazione B3D Lab;
- riepilogo cliente e preventivo;
- contesto della richiesta;
- soluzione tecnica proposta;
- sintesi economica cliente;
- condizioni e note;
- nota fiscale/commerciale da validare con commercialista.

Il template base resta sostituibile con un modello `.docx` personalizzato.

### Risultato Atteso

Alla fine della procedura il gestionale deve contenere un preventivo completo e almeno un documento cliente generato in formato `.docx` e PDF.

## Procedura - Applicare Prezzo E Margine

### Quando Usarla

Usare questa procedura quando le voci di costo interne sono state inserite e si vuole generare un prezzo proposta con una regola ripetibile.

### Passi Operativi

1. Aprire il dettaglio preventivo.
2. Scendere alla configurazione tecnica da prezzare.
3. Controllare il valore **Costo interno**.
4. Inserire il margine percentuale desiderato.
5. Inserire l'arrotondamento, ad esempio `5` per arrotondare al multiplo di 5 EUR.
6. Usare **Applica prezzo**.
7. Controllare **Margine** e **Totale proposta**.

### Note

- La regola crea o aggiorna una voce interna chiamata **Margine commerciale**.
- Il dettaglio economico resta interno e non viene esposto nel documento consulenza.
- Se esistevano vecchie voci margine, la regola evita il doppio conteggio mantenendo attivo un solo margine.

## Procedura - Fare Un Backup Locale

### Quando Usarla

Usare questa procedura prima di modifiche importanti, prima di prove delicate o a fine giornata di lavoro.

### Passi Operativi

1. Verificare che il gestionale non stia generando documenti in quel momento.
2. Eseguire il comando:

```bash
python manage.py backup_local
```

3. Controllare che venga creato uno zip nella cartella `backups/`.
4. Conservare una copia dello zip anche fuori dal PC, se contiene dati importanti.

### Risultato Atteso

Il backup contiene database locale, file generati/caricati e documentazione.
