# Architettura Tecnica

## Scopo

Questo documento definisce la direzione tecnica del gestionale.

L'obiettivo e costruire un software semplice da usare, ma anche ordinato e comprensibile per uno sviluppatore esterno che in futuro potrebbe occuparsi di nuove funzioni.

## Principio Guida

Il progetto deve evitare soluzioni troppo personali, difficili da mantenere o comprensibili solo a chi le ha create.

Le tecnologie e la struttura devono essere:

- diffuse;
- documentabili;
- adatte a gestionali;
- facili da consegnare a uno sviluppatore esterno;
- compatibili con una futura evoluzione SaaS.

## Separazione Delle Responsabilita

Backend, frontend e stile devono essere separati in modo chiaro.

Questa separazione non significa rendere subito il progetto complesso, ma organizzarlo bene fin dall'inizio.

## Backend

Il backend gestisce:

- database;
- clienti;
- preventivi;
- configurazioni;
- costi interni;
- commesse;
- materiali;
- stampanti;
- template documenti;
- generazione documenti;
- automazioni;
- utenti e permessi futuri.

### Tecnologia Candidata

Django e il candidato principale per il backend.

Motivi:

- e diffuso;
- e stabile;
- e adatto ai gestionali;
- ha un pannello amministrativo utile;
- gestisce bene database e utenti;
- e comprensibile per molti sviluppatori Python;
- permette una crescita progressiva verso API e SaaS.

La scelta definitiva andra approvata prima dell'avvio dello sviluppo.

## Frontend

Il frontend gestisce:

- schermate;
- form;
- tabelle;
- navigazione;
- interazioni dell'utente;
- visualizzazione stati;
- anteprime e download documenti.

### Prima Versione

Per la prima versione e consigliato partire con frontend integrato in Django, ma organizzato in modo modulare.

Questo significa:

- template separati per area funzionale;
- componenti riutilizzabili;
- JavaScript leggero solo dove serve;
- nessuna complessita eccessiva da applicazione SPA completa.

### Evoluzione Futura

Se il gestionale diventera SaaS o richiedera un'interfaccia piu ricca, il frontend potra evolvere verso una soluzione separata, ad esempio:

- React;
- Vue;
- Svelte;
- altra tecnologia moderna.

Per rendere possibile questa evoluzione, il backend dovra essere progettato con regole e dati ben separati dalla presentazione.

## CSS E Design System

Lo stile deve essere separato dalla logica.

La prima versione deve avere un CSS organizzato, con:

- colori base;
- spaziature;
- tipografia;
- bottoni;
- tabelle;
- form;
- badge di stato;
- layout principali;
- messaggi di errore e conferma.

I componenti visivi devono essere riutilizzabili.

Esempi:

- pulsante primario;
- pulsante secondario;
- tabella dati;
- scheda riepilogo;
- badge stato preventivo;
- badge stato commessa;
- campo form;
- area note.

## Struttura Modulare

Il progetto dovra essere diviso per aree funzionali.

Moduli previsti:

- clienti;
- preventivi;
- commesse;
- materiali;
- stampanti;
- documenti;
- file allegati;
- automazioni;
- impostazioni.

Ogni modulo dovra avere responsabilita chiare.

## Regole Economiche E Documentali

Le regole di calcolo e di trasformazione dei documenti non devono essere disperse nelle schermate.

Devono stare in funzioni o servizi dedicati, cosi uno sviluppatore puo modificarle senza rompere l'interfaccia.

Esempi:

- calcolo totale configurazione;
- calcolo prezzo unitario;
- preparazione dati per template consulenza;
- preparazione dati per template fornitura/artigiano;
- versionamento documenti;
- estrazione metadati file.

## Documentazione Per Sviluppatore Esterno

Il progetto dovra contenere documentazione chiara su:

- come installare l'ambiente;
- come avviare il gestionale;
- dove sono i moduli principali;
- dove sono i template documento;
- dove sono i CSS;
- dove sono le automazioni;
- come generare documenti;
- come eseguire backup;
- come fare test o controlli base.

## Scelte Da Evitare

Evitare:

- codice troppo personalizzato senza documentazione;
- logica economica scritta direttamente nelle pagine;
- template documento rigidi nel codice;
- CSS sparso in ogni pagina;
- dipendenze rare o poco mantenute;
- architettura troppo complessa per la prima versione;
- soluzioni difficili da spiegare a un nuovo sviluppatore.

## Decisione Operativa

La direzione tecnica approvata e:

- backend, frontend e CSS separati nelle responsabilita;
- Django come candidato principale;
- prima versione con frontend Django modulare;
- CSS organizzato come piccolo design system;
- predisposizione futura per API e frontend separato;
- documentazione pensata anche per sviluppatori esterni.

Lo stack tecnico proposto per l'MVP e dettagliato in `docs/STACK_TECNICO_MVP.md`.

## Nota Sulla Visione SaaS

La prima versione non sara un SaaS completo.

Tuttavia, alcune scelte devono gia preparare quella possibilita:

- template documenti personalizzabili;
- dati aziendali separati;
- utenti e permessi futuri;
- automazioni tracciabili;
- architettura modulare;
- possibilita futura di API.
