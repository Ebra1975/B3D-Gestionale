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
- Scadenze o consegne previste.
- Riepilogo economico base del mese.

### Azioni

- Nuovo preventivo.
- Nuovo cliente.
- Apri commessa.
- Apri preventivo in sospeso.

### Note

La dashboard non deve sembrare una pagina pubblicitaria. Deve essere uno strumento di lavoro, ordinato e leggibile.

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

### Azioni

- Crea cliente.
- Modifica cliente.
- Crea preventivo per questo cliente.
- Apri storico.

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
- genera documento per questa configurazione;
- marca come configurazione scelta.

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

### Documenti Cliente

Da ogni preventivo si deve poter generare:

- vista interna dettagliata;
- proposta consulenza;
- proposta fornitura/artigiano.

La scelta del profilo non deve cambiare i dati del preventivo: cambia solo come vengono presentati.

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
- file collegati;
- note operative;
- fasi di lavoro;
- costi finali effettivi;
- differenza tra previsto e reale.

### Azioni

- cambia stato;
- aggiungi nota;
- allega file;
- registra tempo o costo extra;
- chiudi commessa.

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

Tipi:

- interno dettagliato;
- consulenza;
- fornitura/artigiano.

### Template Documenti

La sezione documenti deve permettere di gestire template `.docx`.

Mostrare:

- nome template;
- tipo documento;
- profilo;
- versione;
- stato attivo/non attivo;
- data caricamento.

Azioni:

- carica template;
- disattiva template;
- scarica template;
- genera documento da template;
- scarica `.docx` generato;
- scarica PDF generato.

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
4. Inserisco oggetto, quantita e descrizione tecnica.
5. Aggiungo una o piu configurazioni.
6. Inserisco i costi interni per ogni configurazione.
7. Aggiungo eventuale prototipo.
8. Scelgo profilo documento "consulenza".
9. Scelgo il template `.docx` di consulenza.
10. Genero proposta `.docx` e PDF.
11. Segno il preventivo come inviato.

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

Priorita media:

- commesse;
- materiali;
- stampanti;
- PDF fornitura/artigiano.

Priorita futura:

- multiutente;
- statistiche avanzate;
- integrazione stampanti;
- fatturazione elettronica;
- accesso remoto.
