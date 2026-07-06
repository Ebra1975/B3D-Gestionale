# Infrastruttura E Automazioni

## Scopo

Questo documento raccoglie le decisioni infrastrutturali che influenzano il modo in cui il gestionale verra costruito.

Anche se la prima versione sara locale e usata da una sola persona, il progetto deve mantenere una visione futura da prodotto vendibile o SaaS.

## Visione Generale

La prima installazione sara locale su mini PC BMAX con Linux Server.

Il gestionale dovra pero essere progettato in modo da non chiudere la strada a:

- multiutente;
- piu aziende/clienti sullo stesso sistema;
- personalizzazione dei documenti;
- ruoli e permessi;
- installazioni presso terzi;
- futura modalita SaaS.

## Preview File 3D

### Principio

I file originali caricati dall'utente devono restare separati dalle anteprime generate dal sistema.

Il gestionale conserva:

- file originale;
- metadati estratti;
- preview o thumbnail generata;
- eventuali errori di elaborazione.

### File 3MF

Per i file 3MF, nella prima fase il sistema dovra provare a:

- salvare il file originale;
- estrarre eventuale thumbnail gia presente;
- leggere metadati disponibili;
- mostrare una anteprima base nella scheda preventivo o commessa.

Preview 3D interattiva avanzata rimandata a una fase successiva.

### File G-code

Per i file G-code, nella prima fase il sistema dovra provare a:

- salvare il file originale;
- estrarre eventuale thumbnail generata dallo slicer;
- leggere tempo stimato;
- leggere materiale stimato;
- leggere layer, temperature e altre informazioni se disponibili;
- mostrare una scheda tecnica riepilogativa.

La visualizzazione layer-per-layer del percorso utensile e considerata evoluzione futura.

## Automazioni

### Principio

Le operazioni lente o ripetitive non devono bloccare l'utente.

Esempi:

- generazione preview file;
- estrazione metadati;
- generazione documenti;
- conversione DOCX in PDF;
- backup;
- controlli periodici.

Queste attivita devono essere gestite come lavorazioni automatiche in background.

## Automazioni Interne

Automazioni previste:

- creazione preview file 3MF/G-code;
- estrazione dati tecnici dai file;
- generazione documento da template;
- conversione documento in PDF;
- salvataggio versione documento;
- aggiornamento riepiloghi economici;
- promemoria su preventivi scaduti;
- promemoria su commesse aperte.

## Automazioni Di Sistema

Automazioni previste:

- backup database;
- backup file allegati;
- controllo spazio disco;
- pulizia file temporanei;
- verifica periodica stato applicazione.

## Template Documenti

### Decisione

Il gestionale deve supportare template documenti caricabili in formato `.docx`.

Questa scelta rende il progetto piu flessibile e piu adatto a una futura vendita o evoluzione SaaS.

### Tipi Di Template

Template previsti:

- preventivo consulenza;
- preventivo fornitura/artigiano;
- preventivo interno dettagliato;
- fattura o documento fiscale futuro;
- documento di consegna;
- relazione tecnica;
- altri documenti personalizzati.

### Segnaposto

I template useranno segnaposto leggibili, ad esempio:

```text
{{ cliente.nome }}
{{ cliente.indirizzo }}
{{ preventivo.numero }}
{{ preventivo.data }}
{{ preventivo.oggetto }}
{{ configurazione.nome }}
{{ configurazione.descrizione }}
{{ configurazione.totale }}
{{ configurazione.prezzo_unitario }}
```

La logica complessa deve restare nel gestionale. Il template deve limitarsi a presentare dati gia preparati.

### Output

Da un template `.docx`, il gestionale dovra generare:

- documento `.docx` compilato e modificabile;
- documento `.pdf` pronto da inviare.

### Conversione PDF

Nella prima installazione locale, la conversione da `.docx` a `.pdf` potra essere gestita dal server Linux tramite LibreOffice in modalita automatica.

L'utente non dovra usare LibreOffice direttamente: il gestionale mostrera solo il risultato.

## Versionamento Documenti

Ogni documento generato deve essere salvato come versione storica.

Esempi:

- `Preventivo_2026-001_Consulenza_v1.docx`
- `Preventivo_2026-001_Consulenza_v1.pdf`
- `Preventivo_2026-001_Consulenza_v2.docx`
- `Preventivo_2026-001_Consulenza_v2.pdf`

Questo evita di perdere traccia dei documenti inviati al cliente.

## Visione SaaS

Anche se il progetto parte locale, alcune scelte devono essere compatibili con un futuro SaaS:

- template personalizzabili per azienda;
- dati aziendali separati dai dati cliente;
- documenti versionati;
- utenti e permessi in futuro;
- impostazioni per profilo commerciale/fiscale;
- file allegati organizzati;
- operazioni automatiche tracciabili.

## Fuori Dalla Prima Versione

Non sono priorita immediate:

- editor visuale avanzato dei template;
- gestione completa fatturazione elettronica;
- preview 3D avanzata nel browser;
- multi-tenant SaaS completo;
- ruoli utente complessi.

Queste possibilita devono pero restare compatibili con le scelte iniziali.
