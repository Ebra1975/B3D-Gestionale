# Manuale Operativo

Questo manuale spiega come usare il gestionale B3D Lab nelle operazioni quotidiane.

Non e documentazione tecnica per sviluppatori: serve all'operatore per sapere cosa fare, in che ordine farlo e cosa controllare prima di passare allo step successivo.

## Procedure Disponibili

| Procedura | Stato | Scopo |
|---|---|---|
| Fare un preventivo consulenza | Bozza iniziale | Creare un preventivo completo e generare DOCX/PDF cliente e scheda interna. |
| Usare il preventivo demo | Bozza iniziale | Provare il flusso senza usare dati reali di clienti. |
| Creare una commessa da preventivo accettato | Bozza iniziale | Avviare il lavoro operativo dopo accettazione cliente. |
| Aggiornare una commessa | Bozza iniziale | Seguire stato, date e note del lavoro operativo. |
| Gestire memoria commerciale cliente | Bozza iniziale | Conservare accordi, NDA, listini firmati e condizioni particolari nella scheda cliente. |
| Controllare la dashboard | Bozza iniziale | Vedere ogni giorno preventivi, commesse e scadenze commerciali da seguire. |
| Aggiornare dati documento | Bozza iniziale | Modificare intestazione, contatti, condizioni e note usate nei DOCX/PDF. |
| Gestire template DOCX | Bozza iniziale | Caricare o sostituire i modelli Word usati per generare documenti cliente e interni. |
| Preparare template con variabili | Bozza iniziale | Usare i segnaposto corretti nei modelli Word. |
| Generare bozza fornitura/artigiano | Bozza preparatoria | Creare un documento futuro di fornitura usando gli stessi dati del preventivo. |
| Numerazione automatica preventivi | Bozza iniziale | Lasciare al gestionale il prossimo numero progressivo del preventivo. |
| Aggiornare parametri economici | Bozza iniziale | Tenere aggiornati costi materiali e stampanti usati dai preventivi. |
| Applicare prezzo e margine | Bozza iniziale | Generare un totale proposta piu ripetibile partendo dai costi interni. |
| Fare un backup locale | Bozza iniziale | Salvare dati e documenti durante lo sviluppo. |

## Procedura - Controllare La Dashboard

### Quando Usarla

Usare questa procedura all'inizio della giornata o prima di chiudere il lavoro, per capire se ci sono attivita da seguire.

### Passi Operativi

1. Aprire la **Dashboard**.
2. Controllare i numeri principali: preventivi aperti, commesse in corso, lavori pronti e prototipi da validare.
3. Nel riquadro **Da seguire**, controllare i **Preventivi in scadenza**.
4. Aprire i preventivi con data gia superata o vicina e decidere se aggiornare, sollecitare o chiudere.
5. Controllare le **Consegne commesse**.
6. Aprire le commesse con consegna vicina o superata e aggiornare stato, note o data prevista.
7. Controllare la **Memoria commerciale**.
8. Aprire accordi e documenti cliente in scadenza per verificare rinnovi, NDA, listini firmati o condizioni particolari.

### Risultato Atteso

La dashboard diventa il punto di partenza per non dimenticare scadenze operative e commerciali.

## Procedura - Usare Il Preventivo Demo

### Quando Usarla

Usare questa procedura per provare il gestionale, fare verifiche o mostrare il flusso senza inserire dati reali.

### Passi Operativi

1. Aprire la sezione **Preventivi**.
2. Cercare il preventivo `B3D-2026-001`.
3. Aprire il dettaglio preventivo.
4. Controllare il riquadro **Stato preventivo**.
5. Verificare che siano presenti totale, prezzo unitario e configurazione scelta.
6. Generare il documento **cliente** se serve una nuova versione della proposta.
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

## Procedura - Gestire Memoria Commerciale Cliente

### Quando Usarla

Usare questa procedura quando un cliente ha condizioni concordate, NDA, listini firmati, accordi commerciali o documenti che devono essere ricordati prima di preparare nuovi preventivi.

### Passi Operativi

1. Aprire la sezione **Clienti**.
2. Cercare il cliente per nome, referente, email o telefono.
3. Aprire la scheda cliente dal nome.
4. Controllare il riquadro **Accordi cliente**.
5. Se serve, usare **Nuovo accordo**.
6. Inserire nome accordo, eventuale listino collegato, date di validita, stato, condizioni generali e note commerciali.
7. Tornare alla scheda cliente.
8. Controllare il riquadro **Documenti commerciali**.
9. Se serve, usare **Nuovo documento**.
10. Inserire tipo documento, date, stato, eventuale file allegato e note.
11. Prima di creare un nuovo preventivo per quel cliente, rileggere accordi e documenti attivi o in scadenza.

### Risultato Atteso

La scheda cliente diventa il punto in cui recuperare la memoria commerciale: condizioni, allegati e scadenze non restano dispersi in cartelle o note esterne.

### Nota

In questa prima versione gli accordi non modificano automaticamente il prezzo del preventivo. Servono come promemoria operativo: il titolare controlla le condizioni e decide cosa applicare.

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
- proposta cliente generata in `.docx` e PDF;
- scheda interna generata in `.docx` e PDF quando serve controllare costi e margine.

### Passi Operativi

1. Aprire la sezione **Clienti**.
2. Verificare se il cliente esiste gia.
3. Se il cliente non esiste, creare una nuova scheda cliente.
4. Aprire la sezione **Preventivi**.
5. Se il cliente ha accordi o documenti commerciali collegati, controllarli nella scheda cliente.
6. Creare un nuovo preventivo.
7. Lasciare vuoto il campo **Numero** per far assegnare al gestionale il prossimo progressivo automatico.
8. Inserire cliente, oggetto, data, quantita e descrizione della richiesta.
9. Lasciare il profilo documento su **Consulenza**, salvo caso diverso.
10. Salvare il preventivo.
11. Controllare il numero assegnato, ad esempio `B3D-2026-001`.
12. Aggiungere una configurazione tecnica.
13. Compilare nome configurazione, descrizione, materiale, stampante/strumentazione, processo, quantita e dati tecnici disponibili.
14. Se la configurazione e quella da proporre al cliente, marcarla come scelta.
15. Generare i costi automatici disponibili:
    - costo materiale;
    - costo macchina;
    - setup/progettazione.
16. Completare manualmente eventuali importi mancanti, soprattutto setup, progettazione, post-processing, trattamenti o margine.
17. Applicare la regola prezzo/margine se serve un margine percentuale con arrotondamento.
18. Tornare al dettaglio preventivo.
19. Controllare il riquadro **Stato preventivo**.
20. Controllare il riquadro **Memoria commerciale cliente**.
21. Se ci sono accordi, listini collegati, NDA o documenti in scadenza, aprire la scheda cliente e verificarli.
22. Nel riquadro **Memoria commerciale cliente**, usare **Conferma controllo condizioni** e aggiungere una nota interna se serve.
23. Risolvere gli elementi indicati in **Da fare prima della proposta**.
24. Controllare gli avvisi in **Da controllare**.
25. Controllare il blocco **Controlli export PDF/DOCX**.
26. Se intestazione, contatti, condizioni o note documento non sono corretti, aprire **Documenti** e usare **Modifica dati documento**.
27. Quando il totale e coerente, usare **Genera cliente**.
28. Scaricare e controllare DOCX e PDF cliente.
29. Se serve un controllo economico completo, usare **Genera interno** e conservare il documento solo per uso interno.
30. Solo per prove o casi futuri, usare **Genera fornitura bozza** e controllare che la dicitura sia ancora da validare con commercialista.
31. Se il documento cliente e corretto, usare l'azione rapida **Segna inviato** nel dettaglio preventivo.

### Controlli Prima Di Inviare

Prima di inviare una proposta al cliente, verificare:

- il cliente e corretto;
- il numero preventivo e presente e segue il formato `B3D-ANNO-NNN`;
- l'oggetto descrive bene il lavoro;
- la descrizione e comprensibile;
- la configurazione scelta e quella giusta;
- il totale non e zero;
- il prezzo unitario ha senso rispetto alla quantita;
- accordi cliente e documenti commerciali sono stati controllati;
- il controllo condizioni cliente e stato confermato nel dettaglio preventivo;
- il documento cliente non mostra il dettaglio economico interno;
- la scheda interna, se generata, mostra costi e margine e non va inviata al cliente;
- eventuali diciture fiscali o commerciali importanti sono da validare con commercialista se non gia confermate.
- dopo l'invio, lo stato del preventivo e aggiornato a **Inviato**.
- il layout DOCX/PDF e leggibile e non contiene dettagli economici interni.

### Cosa Non Fare

- Non duplicare i dati economici in documenti esterni.
- Non modificare a mano il PDF come fonte principale.
- Non inviare al cliente la vista interna dettagliata.
- Non usare il documento consulenza per casistiche di fornitura/artigiano senza revisione del profilo.

### Template Consulenza E Scheda Interna

Il gestionale usa un template consulenza base v3 se non viene caricato un template personalizzato.

Il template cliente contiene:

- intestazione B3D Lab;
- contatti azienda;
- riepilogo compatto di cliente e preventivo;
- contesto della richiesta;
- soluzione tecnica proposta;
- sintesi economica cliente;
- condizioni e note;
- nota fiscale/commerciale da validare con commercialista.

La scheda interna usa un template base v2 e contiene:

- riepilogo preventivo e cliente;
- costo interno, margine e totale proposta;
- voci di costo con eventuali note;
- ipotesi operative;
- note interne e controlli documento.

La scheda interna non va inviata al cliente.

Il template base resta sostituibile con un modello `.docx` personalizzato.

### Template Fornitura/Artigiano Preparatorio

Dal dettaglio preventivo e disponibile **Genera fornitura bozza**.

Questo documento usa gli stessi dati del preventivo e le voci di costo marcate come visibili per fornitura/artigiano. Serve per preparare il profilo futuro, non per sostituire oggi la proposta consulenza.

Prima di inviarlo a un cliente reale, diciture fiscali, commerciali e livello di dettaglio devono essere validati con commercialista.

### Risultato Atteso

Alla fine della procedura il gestionale deve contenere un preventivo completo, almeno un documento cliente generato in formato `.docx` e PDF e, quando utile, una scheda interna separata con dettaglio economico.

## Procedura - Aggiornare Dati Documento

### Quando Usarla

Usare questa procedura prima di generare documenti cliente o interni quando cambiano intestazione azienda, contatti, condizioni standard, nota fiscale/commerciale o nota interna.

### Passi Operativi

1. Aprire la sezione **Documenti**.
2. Controllare il riquadro **Dati documento**.
3. Usare **Modifica dati documento**.
4. Aggiornare solo i campi necessari.
5. Salvare.
6. Tornare al preventivo e generare una nuova versione DOCX/PDF.

### Nota

I documenti gia generati non vengono modificati. Le modifiche valgono per le prossime generazioni.

## Procedura - Gestire Template DOCX

### Quando Usarla

Usare questa procedura quando si vuole caricare un modello Word personalizzato, cambiare versione del template o scegliere quale modello usare per i prossimi documenti.

### Passi Operativi

1. Aprire la sezione **Documenti**.
2. Nel riquadro **Template DOCX**, controllare nome, tipo documento, versione e stato.
3. Usare **Nuovo template DOCX** per caricare un file Word `.docx`.
4. Compilare nome, tipo documento, profilo, versione e note.
5. Lasciare **attivo** se il modello deve essere usato subito.
6. Salvare.
7. Per sostituire o correggere un modello esistente, usare **Modifica**.
8. Per scegliere un modello gia caricato, usare **Attiva**.
9. Scaricare il DOCX dalla lista quando serve controllare il file originale.
10. Generare una nuova versione del documento dal preventivo e verificare il risultato.

### Note

- Per ogni tipo documento resta attivo un solo template alla volta.
- Il template personalizzato attivo ha priorita sul template base generato dal gestionale.
- Il caricamento verifica che il file sia un DOCX leggibile.
- Per i template consulenza, interno e fornitura/artigiano, il gestionale blocca i segnaposto principali non riconosciuti.
- Dopo ogni modifica importante al template, generare comunque un documento di prova e controllare il layout prima dell'invio al cliente.

## Guida - Campi E Variabili Template DOCX

### Quando Usarla

Usare questa guida quando si modifica un template Word `.docx` o quando si prepara un nuovo modello da caricare nella sezione **Documenti**.

Il template deve contenere segnaposto scritti tra doppie parentesi graffe, ad esempio:

```text
{{ cliente.nome }}
```

Il gestionale sostituisce questi segnaposto con i dati del preventivo quando genera il DOCX.

### Regole Pratiche

- Scrivere i segnaposto esattamente come indicati.
- Non cambiare mai i nomi prima del punto, ad esempio `cliente`, `preventivo`, `configurazione`, `proposta`, `b3d`.
- Per iniziare, scaricare un template base dalla sezione **Documenti**, modificarlo in Word e ricaricarlo come nuovo template.
- Dopo il caricamento, generare un documento di prova e controllare sempre il PDF.
- Se Word spezza graficamente un segnaposto, riscriverlo a mano nello stesso punto del documento.

### Campi Azienda

Questi campi arrivano dai **Dati documento**.

| Segnaposto | Contenuto |
|---|---|
| `{{ b3d.nome }}` | Nome azienda |
| `{{ b3d.sottotitolo }}` | Sottotitolo aziendale |
| `{{ b3d.indirizzo }}` | Indirizzo |
| `{{ b3d.email }}` | Email |
| `{{ b3d.telefono }}` | Telefono |
| `{{ b3d.sito }}` | Sito web |
| `{{ b3d.codice_fiscale }}` | Codice fiscale o partita IVA |

### Campi Cliente

| Segnaposto | Contenuto |
|---|---|
| `{{ cliente.nome }}` | Nome cliente |
| `{{ cliente.referente }}` | Referente |
| `{{ cliente.email }}` | Email cliente |
| `{{ cliente.indirizzo }}` | Indirizzo cliente |
| `{{ cliente.codice_fiscale }}` | Codice fiscale o partita IVA cliente |

### Campi Preventivo

| Segnaposto | Contenuto |
|---|---|
| `{{ preventivo.numero }}` | Numero preventivo |
| `{{ preventivo.oggetto }}` | Oggetto |
| `{{ preventivo.descrizione }}` | Descrizione richiesta |
| `{{ preventivo.data }}` | Data preventivo |
| `{{ preventivo.validita }}` | Data validita |
| `{{ preventivo.quantita }}` | Quantita della configurazione usata |
| `{{ preventivo.condizioni }}` | Condizioni generali |

### Campi Configurazione Tecnica

| Segnaposto | Contenuto |
|---|---|
| `{{ configurazione.nome }}` | Nome configurazione |
| `{{ configurazione.descrizione }}` | Descrizione configurazione |
| `{{ configurazione.materiale }}` | Materiale o tecnologia |
| `{{ configurazione.processo }}` | Processo |
| `{{ configurazione.trattamento }}` | Trattamento |
| `{{ configurazione.durata }}` | Durata attesa |
| `{{ configurazione.modalita }}` | Modalita operativa |
| `{{ configurazione.note }}` | Note pubbliche |
| `{{ configurazione.totale }}` | Totale proposta |
| `{{ configurazione.unitario }}` | Prezzo unitario |

### Campi Proposta Cliente

| Segnaposto | Contenuto |
|---|---|
| `{{ proposta.voce }}` | Descrizione sintetica della proposta consulenza |
| `{{ proposta.totale }}` | Totale proposta |
| `{{ proposta.unitario }}` | Prezzo unitario |
| `{{ proposta.nota_fiscale }}` | Nota fiscale/commerciale |

### Campi Solo Scheda Interna

Questi campi vanno usati solo nei template di tipo **Preventivo interno**.

| Segnaposto | Contenuto |
|---|---|
| `{{ interno.costo_base }}` | Costo interno senza margine |
| `{{ interno.margine }}` | Margine commerciale |
| `{{ interno.margine_percentuale }}` | Percentuale margine |
| `{{ interno.note_preventivo }}` | Note interne del preventivo |
| `{{ interno.note_configurazione }}` | Note interne della configurazione |
| `{{ interno.nota_footer }}` | Nota interna di fondo pagina |

### Campi Fornitura/Artigiano

Questi campi vanno usati nei template di tipo **Preventivo fornitura/artigiano**.

| Segnaposto | Contenuto |
|---|---|
| `{{ fornitura.titolo }}` | Titolo documento fornitura/artigiano |
| `{{ fornitura.voce }}` | Descrizione sintetica fornitura |
| `{{ fornitura.condizioni }}` | Condizioni del documento |
| `{{ fornitura.nota_fiscale }}` | Nota fiscale/commerciale |
| `{{ fornitura.nota_preparatoria }}` | Nota che ricorda la validazione futura |

### Tabelle Con Righe Ripetute

Per mostrare piu voci di costo in una tabella Word, serve una riga ripetuta.

Nei template Word e preferibile usare i marcatori speciali per righe tabella:

- `{%tr for voce in voci_fornitura %}`
- `{%tr endfor %}`

Questi marcatori dicono al gestionale di ripetere una riga della tabella per ogni voce.

Per il template **interno**, usare `voci_costo`:

```text
{%tr for voce in voci_costo %}
{{ voce.categoria }}
{{ voce.descrizione }}
{{ voce.quantita }}
{{ voce.unitario }}
{{ voce.totale }}
{{ voce.note }}
{%tr endfor %}
```

Per il template **fornitura/artigiano**, usare `voci_fornitura`:

```text
{%tr for voce in voci_fornitura %}
{{ voce.categoria }}
{{ voce.descrizione }}
{{ voce.quantita }}
{{ voce.unitario }}
{{ voce.totale }}
{{ voce.note }}
{%tr endfor %}
```

### Come Impostare La Tabella In Word

Il modo piu stabile e questo:

1. Creare una tabella con una riga intestazione e una riga dati.
2. Aggiungere una riga subito sotto l'intestazione con solo `{%tr for voce in voci_fornitura %}`.
3. Aggiungere la riga dati con i campi della voce.
4. Aggiungere una riga subito sotto con solo `{%tr endfor %}`.
5. Non mettere righe vuote tra `{%tr for ... %}` e `{%tr endfor %}`.
6. Generare un documento di prova e controllare sia DOCX sia PDF.

Esempio di tabella per fornitura/artigiano:

| Categoria | Descrizione | Quantita | Unitario | Totale |
|---|---|---|---|---|
| `{%tr for voce in voci_fornitura %}` |  |  |  |  |
| `{{ voce.categoria }}` | `{{ voce.descrizione }}` | `{{ voce.quantita }}` | `{{ voce.unitario }}` | `{{ voce.totale }}` |
| `{%tr endfor %}` |  |  |  |  |

### Variabili Ammesse Per Tipo Template

| Tipo template | Variabili principali ammesse |
|---|---|
| Preventivo consulenza | `cliente`, `preventivo`, `configurazione`, `proposta`, `b3d` |
| Preventivo interno | `cliente`, `preventivo`, `configurazione`, `proposta`, `b3d`, `interno`, `voci_costo` |
| Preventivo fornitura/artigiano | `cliente`, `preventivo`, `configurazione`, `proposta`, `b3d`, `fornitura`, `voci_fornitura` |

Se un template contiene una variabile non presente in questa lista, il gestionale blocca il caricamento per evitare documenti generati male.

## Procedura - Aggiornare Parametri Economici

### Quando Usarla

Usare questa procedura quando cambia il prezzo di un materiale, si vuole correggere lo scarto prudenziale o si aggiorna il costo reale di una stampante.

### Passi Operativi

1. Aprire **Materiali** o **Stampanti**.
2. Cercare la voce da aggiornare.
3. Aprire la scheda dal nome.
4. Per un materiale, aggiornare **Costo base per kg/litro** e **Scarto / extra materiale %**.
5. Per una stampante, aggiornare **Costo orario base**, **Manutenzione per ora**, **Consumo stimato watt**, **Costo energia kWh** e **Rischio fallimento %**.
6. Scrivere nelle note economiche il motivo del valore, ad esempio prezzo fornitore, stima prudenziale o controllo bolletta.
7. Salvare.
8. Nei nuovi preventivi, usare **Genera costo materiale** o **Genera costo macchina**: la voce costo usera i parametri aggiornati e salvera una nota interna con il riepilogo del calcolo.

### Nota

I preventivi gia calcolati non vengono modificati da soli. Se si vuole aggiornare un preventivo aperto, rigenerare la voce di costo dalla configurazione tecnica.

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
