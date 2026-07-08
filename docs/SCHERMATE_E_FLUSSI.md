# Schermate E Flussi

## Scopo

Questo documento descrive le schermate principali della prima versione del gestionale e il modo in cui verranno usate.

L'obiettivo non e definire ancora la grafica definitiva, ma chiarire cosa deve comparire in ogni schermata e quali azioni devono essere semplici.

## Navigazione Principale

Menu iniziale consigliato:

- Dashboard
- Clienti
- Preventivi
- Commesse
- Materiali
- Stampanti
- Documenti
- Manuale
- Impostazioni

La prima versione deve restare semplice. Le voci possono crescere in futuro, ma all'inizio devono coprire il flusso reale di lavoro.

Su desktop la sidebar deve restare fissa durante lo scorrimento delle pagine lunghe, cosi la navigazione principale resta sempre disponibile.

## Dashboard

### Obiettivo

Dare una visione immediata della situazione.

### Contenuti

- Preventivi aperti.
- Commesse in corso.
- Lavori pronti.
- Prototipi da validare.
- Preventivi in scadenza entro 14 giorni o gia scaduti.
- Consegne commesse entro 14 giorni o gia scadute.
- Accordi cliente e documenti commerciali in scadenza entro 30 giorni o gia scaduti.
- Riepilogo economico base del mese.

### Azioni

- Nuovo preventivo.
- Nuovo cliente.
- Apri commessa.
- Apri preventivo in sospeso.

### Note

La dashboard non deve sembrare una pagina pubblicitaria. Deve essere uno strumento di lavoro, ordinato e leggibile.

La prima versione dello Sprint 06 usa soglie fisse e semplici: 14 giorni per preventivi e commesse, 30 giorni per accordi e documenti commerciali cliente. Le soglie potranno diventare configurabili dopo l'uso reale.

## Clienti

### Obiettivo

Tenere ordinati clienti, referenti e storico lavori.

### Lista Clienti

Mostrare:

- nome cliente;
- referente;
- email;
- telefono;
- numero preventivi;
- numero commesse;
- ultimo lavoro.

### Scheda Cliente

Mostrare:

- dati anagrafici;
- contatti;
- note;
- preventivi collegati;
- commesse collegate;
- documenti generati.
- accordi cliente;
- documenti commerciali cliente.

### Azioni

- Crea cliente.
- Modifica cliente.
- Crea preventivo per questo cliente.
- Apri storico.
- Crea accordo cliente.
- Crea documento commerciale cliente.

## Preventivi

### Obiettivo

Creare il cuore economico e tecnico del lavoro.

### Lista Preventivi

Mostrare:

- numero;
- cliente;
- oggetto;
- data;
- validita;
- stato;
- totale principale;
- profilo documento scelto.

La lista deve avere una ricerca per numero, cliente e oggetto. I preventivi gia convertiti in commessa devono essere visivamente attenuati e filtrabili separatamente.

Stati:

- bozza;
- inviato;
- da rivedere;
- accettato;
- rifiutato;
- scaduto;
- annullato.

### Scheda Preventivo

La scheda preventivo deve avere sezioni chiare:

- dati generali;
- cliente;
- descrizione tecnica;
- configurazioni/opzioni;
- prototipo;
- condizioni generali;
- documenti generati;
- note interne.

### Configurazioni

Ogni configurazione deve mostrare:

- nome;
- descrizione;
- durata attesa;
- materiale;
- peso materiale per unita;
- ore macchina per unita;
- processo;
- modalita operativa;
- quantita;
- prezzo totale;
- prezzo unitario;
- stato.

Azioni:

- aggiungi configurazione;
- duplica configurazione;
- modifica costi interni;
- importa dati tecnici da G-code/3MF;
- applica prezzo/margine;
- genera documento per questa configurazione;
- marca come configurazione scelta.

L'import G-code/3MF compila i campi tecnici della configurazione quando lo slicer fornisce peso materiale, tempo macchina e numero piatti. Non genera automaticamente costi o prezzo: dopo il controllo dell'operatore restano disponibili i pulsanti per generare costo materiale e costo macchina.

### Costi Interni

La sezione costi interni deve essere molto chiara e non visibile al cliente.

Voci consigliate:

- materiali;
- tempo macchina;
- elettricita;
- progettazione;
- setup;
- manodopera;
- trasferta;
- post-processing;
- trattamento;
- margine;
- altro.

Per ogni voce:

- descrizione;
- quantita;
- unita;
- costo unitario;
- totale;
- note.

La scheda configurazione mostra anche un riepilogo prezzo con:

- costo interno senza margine;
- margine commerciale;
- percentuale margine effettiva;
- totale proposta.

La prima regola prezzo/margine usa:

- percentuale di margine;
- arrotondamento al multiplo indicato;
- voce interna **Margine commerciale**.

### Documenti Cliente

Da ogni preventivo si deve poter generare:

- vista interna dettagliata;
- proposta consulenza;
- proposta fornitura/artigiano.

La scelta del profilo non deve cambiare i dati del preventivo: cambia solo come vengono presentati.

Il template consulenza base generato dal gestionale e stato rifinito in versione v3 con:

- intestazione B3D Lab;
- riepilogo cliente/preventivo piu compatto;
- sezione tecnica;
- sintesi economica cliente;
- nota fiscale/commerciale marcata come da validare.

Il template interno dettagliato generato dal gestionale e stato rifinito in versione v2 con:

- riepilogo preventivo e cliente;
- blocco economia interna con costo, margine e totale;
- tabella voci di costo con note;
- ipotesi operative, note interne e controlli documento.

I template Sprint 11 non sono ancora il layout definitivo di brand, ma sono piu adatti a controllare il flusso reale cliente/interno rispetto ai template provvisori iniziali.

Dal dettaglio preventivo e disponibile anche **Genera fornitura bozza**. Il template fornitura/artigiano base v1 e preparatorio: usa gli stessi dati del preventivo e le voci marcate come visibili per fornitura, ma le diciture commerciali/fiscali restano da validare prima dell'uso reale.

## Commesse

### Obiettivo

Seguire il lavoro dopo l'accettazione del preventivo.

### Lista Commesse

Mostrare:

- numero commessa;
- cliente;
- oggetto;
- configurazione scelta;
- stato;
- data avvio;
- consegna prevista;
- avanzamento.

La lista deve avere una ricerca per numero commessa, cliente e preventivo, oltre a un filtro per stato.

Stati:

- da fare;
- in progettazione;
- in stampa;
- in post-processing;
- pronto;
- consegnato;
- sospeso;
- annullato.

### Scheda Commessa

Mostrare:

- dati cliente;
- preventivo collegato;
- configurazione scelta;
- documenti collegati al preventivo;
- note operative;
- costi previsti interni della configurazione scelta;
- date operative;
- note finali.

### Azioni

- cambia stato;
- aggiungi nota;
- aggiorna data avvio;
- aggiorna consegna prevista;
- registra data consegna;
- chiudi commessa.

Nella prima versione Sprint 03 la scheda commessa non registra ancora costi finali effettivi o file allegati dedicati alla commessa. Questi restano passaggi successivi.

## Materiali

### Obiettivo

Gestire dati utili per calcolare costi e fare scelte tecniche.

### Lista Materiali

Mostrare:

- nome;
- tipo;
- marca;
- colore;
- costo;
- disponibilita;
- resistenza UV;
- note.

La lista deve avere una ricerca per nome, tipo, marca, colore, fornitore e note.

### Scheda Materiale

Mostrare:

- dati tecnici;
- costo al kg o al litro;
- fornitore;
- note di utilizzo;
- lavori in cui e stato usato.

## Stampanti

### Obiettivo

Tenere traccia delle macchine disponibili e dei parametri economici.

### Lista Stampanti

Mostrare:

- nome;
- modello;
- proprieta;
- volume;
- camera chiusa;
- costo orario stimato;
- stato.

La lista deve avere una ricerca per nome, modello, materiali supportati e note.

### Scheda Stampante

Mostrare:

- caratteristiche;
- materiali supportati;
- costo orario;
- consumo elettrico stimato;
- note;
- lavori collegati.

## Documenti

### Obiettivo

Raccogliere i documenti generati e gestire i template caricabili.

### Lista Documenti

Mostrare:

- data;
- cliente;
- preventivo;
- tipo documento;
- versione;
- file `.docx`;
- file PDF.

La lista deve avere una ricerca per template, preventivo, cliente e oggetto.

Tipi:

- interno dettagliato;
- consulenza;
- fornitura/artigiano.

### Template Documenti

La sezione documenti deve permettere di gestire template `.docx`.

Mostrare:

- dati documento attivi: azienda, contatti, condizioni standard e nota fiscale;
- nome template;
- tipo documento;
- profilo;
- versione;
- stato attivo/non attivo;
- data caricamento.

Azioni:

- modifica dati documento attivi;
- carica template;
- modifica template;
- attiva template;
- disattiva template;
- scarica template;
- genera documento da template;
- scarica `.docx` generato;
- scarica PDF generato.

Nella prima gestione da interfaccia, un solo template per tipo documento resta attivo alla volta. Se viene attivato un template personalizzato di consulenza o interno, quel modello viene usato nelle prossime generazioni al posto del template base generato dal gestionale.

Dallo Sprint 13, al salvataggio di un template il gestionale controlla che il file sia un DOCX leggibile. Per proposta consulenza e scheda interna controlla anche che i segnaposto principali usati nel Word siano compatibili con quelli disponibili.

Dallo Sprint 14 lo stesso controllo dei segnaposto viene applicato anche ai template fornitura/artigiano.

## Impostazioni

### Obiettivo

Impostare dati generali senza toccare codice.

Contenuti iniziali:

- dati B3D Lab;
- logo;
- condizioni generali standard;
- aliquote o note fiscali testuali;
- costi macchina predefiniti;
- costo energia;
- margine predefinito;
- profilo documento predefinito.
- template documento predefiniti.

## Manuale Operativo

### Obiettivo

Spiegare all'operatore come usare il gestionale nelle operazioni quotidiane, con procedure passo passo.

### Stato

Prima bozza in `docs/MANUALE_OPERATIVO.md` e prima schermata consultabile dalla sidebar del gestionale.

### Contenuti Possibili

- come creare un cliente;
- come fare un preventivo consulenza;
- come generare DOCX e PDF;
- come controllare cosa manca prima dell'invio;
- come trasformare un preventivo accettato in commessa;
- come gestire documenti e template.

## Flusso 1 - Nuovo Preventivo Consulenza

1. Apro la dashboard.
2. Creo un nuovo cliente o seleziono un cliente esistente.
3. Creo un nuovo preventivo.
4. Controllo nel dettaglio preventivo la memoria commerciale del cliente.
5. Inserisco oggetto, quantita e descrizione tecnica.
6. Aggiungo una o piu configurazioni.
7. Importo eventuale G-code/3MF per compilare peso e ore macchina.
8. Inserisco o genero i costi interni per ogni configurazione.
9. Applico prezzo e margine dopo aver controllato le condizioni cliente.
10. Confermo nel preventivo la revisione di accordi, listini e documenti commerciali.
11. Aggiungo eventuale prototipo.
12. Scelgo profilo documento "consulenza".
13. Se serve un layout personalizzato, apro **Documenti** e attivo il template `.docx` di consulenza.
14. Controllo eventuali mancanze nel blocco export PDF/DOCX.
15. Se i dati documento non sono corretti, apro **Documenti** e uso **Modifica dati documento**.
16. Genero proposta cliente `.docx` e PDF.
17. Genero la scheda interna dettagliata se serve controllare costi e margine.
18. Se serve una prova futura del profilo fornitura/artigiano, genero **fornitura bozza** e la tengo come documento da validare.
19. Segno il preventivo come inviato.

## Flusso 2 - Preventivo Accettato

1. Apro il preventivo.
2. Segno lo stato come accettato.
3. Scelgo la configurazione confermata.
4. Uso l'azione **Crea commessa** dal dettaglio preventivo.
5. Inserisco data avvio e consegna prevista.
6. Seguo gli stati fino alla consegna.

## Flusso 3 - Confronto Interno

1. Apro un preventivo o una commessa.
2. Guardo i costi interni.
3. Confronto costo previsto e costo reale.
4. Aggiorno eventuali parametri per lavori futuri.

## Priorita Per La Prima Versione

Priorita alta:

- dashboard;
- clienti;
- preventivi;
- configurazioni;
- costi interni;
- PDF consulenza;
- PDF interno dettagliato.
- template `.docx` per consulenza e interno dettagliato.
- template `.docx` preparatorio per fornitura/artigiano.

Priorita media:

- commesse;
- materiali;
- stampanti;
- rifinitura e validazione reale PDF fornitura/artigiano.

Priorita futura:

- multiutente;
- statistiche avanzate;
- integrazione stampanti;
- fatturazione elettronica;
- accesso remoto.
