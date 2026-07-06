# AI E Automazioni Operative

## Scopo

Questo documento definisce come usare AI e automazioni nel gestionale.

L'obiettivo non e sostituire il titolare, ma ridurre errori, dimenticanze e lavoro ripetitivo.

## Principio Guida

La AI deve essere un copilota, non il pilota.

Il gestionale puo suggerire, controllare, evidenziare e preparare bozze.

La decisione finale resta sempre al titolare.

## Problema Da Risolvere

Nel laboratorio piccolo molte decisioni restano nella testa di una sola persona:

- come classificare un lavoro;
- quali costi ricordarsi;
- quali rischi valutare;
- quale materiale proporre;
- quale listino applicare;
- quando proporre prototipo;
- quando avvisare il cliente;
- quando un prezzo e troppo basso.

AI e automazioni servono a trasformare esperienza e metodo in regole riutilizzabili.

## Tipi Di Aiuto

### Suggerimenti Tecnici

Esempi:

- per esposizione UV, valuta ASA o trattamento protettivo;
- per ASA, verifica stampante a camera chiusa;
- per componente estetico, valuta post-processing;
- per molte ore macchina, segnala rischio ristampa;
- per materiale cliente, segnala condizioni particolari.

### Suggerimenti Commerciali

Esempi:

- cliente con accordo attivo;
- listino cliente disponibile;
- accordo in scadenza;
- margine sotto soglia;
- preventivo simile gia fatto;
- cliente con condizioni speciali.

### Suggerimenti Documentali

Esempi:

- testo troppo orientato alla vendita di prodotto, meglio consulenza;
- manca fase di validazione prototipo;
- manca nota su disponibilita materiale;
- manca condizione su modifiche successive;
- manca nota su durata attesa.

### Promemoria Operativi

Esempi:

- preventivo in bozza da piu di 7 giorni;
- preventivo inviato senza risposta;
- commessa pronta da consegnare;
- accordo cliente in scadenza;
- backup non eseguito;
- file allegato non elaborato.

## Casistiche Di Lavorazione

Il gestionale potra avere un archivio di casistiche.

Esempi:

- FDM standard;
- FDM tecnico;
- ASA/ABS a camera chiusa;
- prototipo dimensionale;
- piccola serie;
- componente esposto UV;
- componente estetico;
- componente funzionale;
- lavorazione con post-processing;
- lavoro urgente;
- materiale cliente;
- macchina cliente;
- consulenza CAD;
- validazione tramite prototipo.

## Scheda Casistica

Ogni casistica puo contenere:

- nome;
- descrizione;
- materiali consigliati;
- stampanti consigliate;
- rischi;
- checklist;
- voci costo consigliate;
- note cliente consigliate;
- margine minimo;
- automazioni collegate.

## Esempio Casistica

### Componente Esposto UV

Checklist:

- verificare esposizione diretta;
- valutare ASA;
- valutare PETG con trattamento;
- indicare durata attesa;
- indicare eventuale disponibilita colore;
- valutare prototipo.

Voci costo consigliate:

- materiale tecnico;
- tempo macchina;
- progettazione/setup;
- trattamento UV se previsto;
- post-processing se previsto.

Avvisi:

- PLA non consigliato per esposizione UV diretta;
- stampante aperta non ideale per ASA;
- colore chiaro da verificare presso fornitori.

## Regole Automatiche

Esempi:

- se materiale = ASA e stampante senza camera chiusa, mostra avviso;
- se esposizione UV = alta e materiale = PLA, mostra avviso;
- se ore macchina sopra soglia, suggerisci rischio ristampa;
- se cliente ha accordo attivo, applica listino cliente;
- se margine sotto soglia, blocca o richiedi conferma;
- se preventivo ha profilo consulenza, evita dettaglio costo cliente;
- se manca prototipo per geometria nuova, suggerisci validazione.

## Livelli Di Automazione

### Livello 1 - Avvisi

Il sistema mostra un messaggio.

### Livello 2 - Suggerimenti

Il sistema propone una voce o una modifica, ma non la applica.

### Livello 3 - Azione Assistita

Il sistema prepara dati o documenti, poi il titolare approva.

### Livello 4 - Azione Automatica

Il sistema agisce automaticamente solo su attivita sicure e ripetitive, come backup o preview file.

## Cosa La AI Non Deve Fare

- Non deve decidere autonomamente il prezzo finale.
- Non deve inviare documenti al cliente senza approvazione.
- Non deve modificare accordi o listini senza conferma.
- Non deve sostituire la valutazione tecnica del titolare.
- Non deve inventare dati tecnici non presenti.

## Prima Implementazione Consigliata

Non partire subito con AI complessa.

Prima implementare:

- checklist lavorazioni;
- regole automatiche semplici;
- avvisi su dati mancanti;
- suggerimento voci costo;
- confronto con preventivi precedenti;
- template testuali guidati.

AI generativa solo dopo aver costruito dati e regole solide.

## Visione Futura

In futuro la AI potra aiutare a:

- leggere descrizione richiesta cliente;
- classificare lavorazione;
- proporre casistica;
- suggerire configurazioni;
- preparare bozza proposta consulenza;
- confrontare storico lavori;
- evidenziare rischi tecnici;
- suggerire domande da fare al cliente.

Ogni output AI deve restare revisionabile.
