# Listini E Accordi Cliente

## Scopo

Questo documento definisce la visione per gestire listini base, listini personalizzati per cliente e accordi commerciali.

L'obiettivo e trasformare l'esperienza commerciale in regole riutilizzabili, riducendo la dipendenza dalla memoria del titolare.

## Perche Serve

Il laboratorio e pensato per lavorare con PMI del territorio.

Con le PMI puo essere utile avere:

- condizioni concordate;
- listini personalizzati;
- scontistiche per cliente;
- durata degli accordi;
- regole commerciali chiare;
- preventivi coerenti nel tempo.

Questo approccio aiuta anche a gestire il problema "uomo solo al comando": il gestionale conserva metodo, condizioni e memoria commerciale.

## Concetto Base

Il prezzo non nasce ogni volta da zero.

Il gestionale deve poter partire da:

1. listino base;
2. eventuale listino cliente;
3. eventuale accordo attivo;
4. regole di sconto o maggiorazione;
5. revisione finale del titolare.

## Listino Base

Il listino base contiene i valori standard del laboratorio.

Esempi:

- costo orario progettazione;
- costo orario setup;
- costo orario macchina;
- costo materiale;
- costo post-processing;
- costo urgenza;
- margine standard;
- soglia minima di marginalita.

Il listino base serve come riferimento generale.

## Listino Cliente

Il listino cliente deriva dal listino base, ma puo avere condizioni personalizzate.

Esempi:

- sconto su progettazione;
- sconto su produzione ripetitiva;
- prezzo orario macchina dedicato;
- margine diverso;
- costo minimo commessa;
- condizioni speciali su prototipi;
- prezzi concordati per lavorazioni ricorrenti.

Ogni cliente puo avere zero, uno o piu listini nel tempo.

## Accordo Cliente

L'accordo cliente collega un cliente a un listino e definisce una validita.

Campi previsti:

- cliente;
- nome accordo;
- data inizio;
- data fine;
- listino collegato;
- condizioni generali;
- note commerciali;
- stato.

Stati possibili:

- bozza;
- attivo;
- scaduto;
- sospeso;
- rinnovato;
- chiuso.

## Documenti Commerciali E Contrattuali Collegati

Oltre agli accordi commerciali, il gestionale dovra poter conservare documenti collegati al cliente o alla relazione commerciale.

Esempi:

- NDA;
- accordi quadro;
- condizioni particolari;
- lettere di incarico;
- documenti di collaborazione;
- allegati contrattuali;
- listini firmati;
- rinnovi o revisioni accordo.

Questa funzione non e prioritaria nel primo MVP, ma va considerata nella struttura futura.

Ogni documento dovrebbe avere:

- cliente collegato;
- tipo documento;
- data firma o emissione;
- data scadenza se presente;
- stato;
- file allegato;
- note.

Stati possibili:

- bozza;
- inviato;
- firmato;
- attivo;
- scaduto;
- sostituito;
- archiviato.

## Applicazione Al Preventivo

Quando viene creato un preventivo:

1. il gestionale controlla il cliente;
2. verifica se esiste un accordo attivo;
3. applica il listino collegato;
4. se non esiste accordo, usa il listino base;
5. mostra eventuali avvisi;
6. permette sempre revisione manuale.

## Tracciabilita

Ogni preventivo dovrebbe conservare:

- listino usato;
- accordo usato;
- eventuali sconti applicati;
- eventuali correzioni manuali;
- motivazione della correzione se rilevante.

Questo serve per capire in futuro perche e stato fatto un certo prezzo.

## Scontistiche

Le scontistiche possono essere:

- percentuali;
- importi fissi;
- per categoria;
- per materiale;
- per lavorazione;
- per quantita;
- per urgenza;
- per accordo commerciale.

## Esempi Di Regole

- Cliente con accordo attivo: applica listino cliente.
- Cliente senza accordo: applica listino base.
- Quantita sopra soglia: suggerisci sconto produzione ripetitiva.
- Lavoro urgente: applica maggiorazione.
- Margine sotto soglia: mostra avviso.
- Accordo in scadenza: mostra promemoria.

## Relazione Con AI E Automazioni

AI e automazioni possono aiutare a:

- rilevare accordi attivi;
- segnalare documenti cliente mancanti o scaduti;
- suggerire listino corretto;
- segnalare margini bassi;
- confrontare preventivi simili;
- ricordare condizioni cliente;
- suggerire rinnovo accordo.

La decisione finale resta sempre del titolare.

## Priorita

Per la prima versione il listino completo puo essere rimandato.

Pero il modello dati e l'architettura devono lasciare spazio a:

- listino base;
- listino cliente;
- accordo cliente;
- regole di sconto;
- tracciabilita della fonte prezzo.
