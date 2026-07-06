# Regole Preventivi

## Principio Base

Un preventivo contiene sempre dati interni completi.

Da questi dati il sistema genera viste e documenti diversi, senza duplicare le informazioni.

## Modelli Disponibili

I modelli documento devono essere gestiti tramite template caricabili, preferibilmente in formato `.docx`.

Il gestionale prepara i dati e li inserisce nel template scelto, generando un documento `.docx` compilato e un PDF.

### Interno Dettagliato

Serve al titolare per capire costi, prezzo e marginalita.

Mostra:

- materiali;
- ore macchina;
- elettricita;
- progettazione;
- setup;
- manodopera;
- trasferte;
- post-processing;
- trattamenti;
- margine;
- totale;
- prezzo unitario;
- utile stimato.

Questa vista non e pensata per il cliente.

### Consulenza

E il modello principale nella fase attuale.

Il cliente vede una proposta di consulenza tecnica con compenso sintetico.

Linguaggio consigliato:

> Compenso per consulenza tecnica, progettazione, validazione e realizzazione.

Caratteristiche:

- evita il dettaglio eccessivo delle singole voci di costo;
- usa "compenso" invece di "prezzo materiale" o "costo stampa";
- presenta materiali e lavorazione come parte del servizio;
- valorizza progettazione, scelta tecnica e validazione;
- mantiene un tono professionale e consulenziale.

Da validare con commercialista:

- diciture fiscali definitive;
- uso di "compenso";
- descrizione in fattura;
- eventuali limiti legati al codice ATECO e regime forfettario.

### Fornitura / Artigiano

E il modello previsto per una possibile evoluzione futura.

Il cliente puo vedere un dettaglio piu vicino alla produzione:

- materiali;
- lavorazioni;
- trattamenti;
- quantita;
- prezzo unitario;
- totale fornitura.

Questo profilo non e quello principale nella fase attuale.

## Regola Di Conversione

Le stesse voci interne possono essere presentate in modo diverso.

Esempio interno:

- Materiali: 338,20 EUR
- Tempo macchina: 345,72 EUR
- Progettazione e setup: 588,00 EUR
- Verniciatura: 350,00 EUR
- Totale: 1.621,92 EUR

Nel modello consulenza diventa:

> Compenso per consulenza tecnica, progettazione, validazione e realizzazione di 20 unita: 1.621,92 EUR

Nel modello fornitura/artigiano diventa:

- Materiali: 338,20 EUR
- Tempo macchina: 345,72 EUR
- Progettazione e setup: 588,00 EUR
- Verniciatura: 350,00 EUR
- Totale fornitura: 1.621,92 EUR

La conversione tra vista interna, consulenza e fornitura/artigiano deve essere gestita dal gestionale, non duplicando i dati nel template.

## Template DOCX

Ogni profilo documento puo avere uno o piu template `.docx`.

Esempi:

- preventivo consulenza;
- preventivo fornitura/artigiano;
- preventivo interno dettagliato;
- relazione tecnica;
- documento di consegna;
- futura fattura.

I template useranno segnaposto come:

```text
{{ cliente.nome }}
{{ preventivo.numero }}
{{ preventivo.oggetto }}
{{ configurazione.nome }}
{{ configurazione.totale }}
```

La logica economica resta nel gestionale. Il template serve a presentare i dati.

## Configurazioni Multiple

Un preventivo puo contenere piu configurazioni tecniche.

Ogni configurazione deve avere:

- nome chiaro;
- descrizione;
- durata attesa;
- modalita operativa;
- totale;
- prezzo unitario;
- note e condizioni.

## Prototipo

Il prototipo e una fase preliminare.

Va presentato come validazione tecnica prima della produzione definitiva.

Nel modello consulenza e preferibile chiamarlo:

> Fase preliminare - Validazione tramite prototipo.

## Terminologia Consigliata

Preferire:

- configurazione;
- realizzazione;
- validazione;
- progettazione;
- consulenza tecnica;
- compenso;
- strumentazione;
- processo di manifattura additiva.

Usare con attenzione:

- vendita pezzi;
- costo bobina;
- costo stampa;
- fornitura artigianale;
- produzione.

Questi termini possono essere utili nel profilo artigiano, ma non devono dominare il profilo consulenza.
