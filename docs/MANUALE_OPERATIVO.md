# Manuale Operativo

Questo manuale spiega come usare il gestionale B3D Lab nelle operazioni quotidiane.

Non e documentazione tecnica per sviluppatori: serve all'operatore per sapere cosa fare, in che ordine farlo e cosa controllare prima di passare allo step successivo.

## Procedure Disponibili

| Procedura | Stato | Scopo |
|---|---|---|
| Fare un preventivo consulenza | Bozza iniziale | Creare un preventivo completo e generare DOCX/PDF cliente. |
| Usare il preventivo demo | Bozza iniziale | Provare il flusso senza usare dati reali di clienti. |

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
14. Tornare al dettaglio preventivo.
15. Controllare il riquadro **Stato preventivo**.
16. Risolvere gli elementi indicati in **Da fare prima della proposta**.
17. Controllare gli avvisi in **Da controllare**.
18. Quando il totale e coerente, generare il **DOCX consulenza**.
19. Scaricare e controllare il DOCX.
20. Scaricare e controllare il PDF.
21. Se il documento e corretto, aggiornare lo stato del preventivo secondo il flusso reale, per esempio **Inviato**.

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

### Cosa Non Fare

- Non duplicare i dati economici in documenti esterni.
- Non modificare a mano il PDF come fonte principale.
- Non inviare al cliente la vista interna dettagliata.
- Non usare il documento consulenza per casistiche di fornitura/artigiano senza revisione del profilo.

### Risultato Atteso

Alla fine della procedura il gestionale deve contenere un preventivo completo e almeno un documento cliente generato in formato `.docx` e PDF.
