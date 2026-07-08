# Comparazione - Stimalo, PreventiPiraz 3D e Gestionale B3D Lab

Documento preparato il 2026-07-07 per confrontare il gestionale B3D Lab con strumenti esistenti di preventivazione e gestione per stampa 3D.

## Obiettivo Della Comparazione

Capire cosa possiamo imparare da prodotti gia disponibili e quali scelte mantenere diverse nel gestionale B3D Lab.

Il problema pratico e non sviluppare funzioni inutili o troppo isolate: prima di continuare con listini, prezzi e flussi preventivo, conviene vedere come strumenti gia pubblici gestiscono costi, preventivi, clienti, magazzino e documenti.

## Fonti Consultate

- Stimalo: https://stimalo.com/
- PreventiPiraz 3D: https://www.help3d.it/preventipiraz-3d/

Le informazioni sono ricavate dalle pagine pubbliche consultate il 2026-07-07. Prezzi, funzioni e limiti possono cambiare.

## Sintesi Rapida

| Aspetto | Stimalo | PreventiPiraz 3D | Gestionale B3D Lab |
|---|---|---|---|
| Focus principale | Gestionale cloud/PWA per costi, preventivi, clienti, inventario e commesse. | Software desktop per preventivi stampa 3D con forte uso dei dati slicer. | Gestionale locale per B3D Lab, con preventivi, clienti, commesse, documenti e memoria commerciale. |
| Tipo installazione | Web app / PWA con account. | App desktop Windows/macOS. | Web app locale su mini PC BMAX in rete locale. |
| Calcolo stampa 3D | Inserimento peso/tempo e cataloghi stampanti/materiali; calcolo costi FDM/SLA/SLS. | Calcolo basato su slicer e caricamento file; forte su STL/STEP/OBJ/3MF e multicolore. | Per ora costi manuali/assistiti e voci automatiche base; import/slicing avanzato non ancora presente. |
| Preventivi PDF | Si, PDF cliente; branding avanzato nel piano Pro. | Si, esportazione PDF; versione free con watermark. | Si, DOCX e PDF consulenza; dati economici interni separati dal documento cliente. |
| Clienti | Gestione clienti inclusa. | Anagrafica clienti inclusa. | Gestione clienti con memoria commerciale, accordi e documenti collegati. |
| Magazzino | Inventario e FIFO indicati come funzioni. | Magazzino materiali e avvisi materiale in esaurimento. | Materiali e stampanti presenti; magazzino operativo ancora da evolvere. |
| Commesse / ordini | Job management dichiarato. | Preventivi salvati, ordini di lavorazione e workspace condiviso nei piani. | Commessa collegata a preventivo accettato, pensata per uso operativo interno. |
| Privacy / dati | Cloud con misure di sicurezza, isolamento utenti e GDPR dichiarati. | Dati locali sul PC, senza cloud dichiarato. | Locale su server BMAX, dati sotto controllo diretto dell'azienda. |
| Posizionamento commerciale | Gratuito con piano Pro per branding, template, analytics e funzioni avanzate. | Free/Lite/Pro, annuale o lifetime, con limiti crescenti. | Strumento interno su misura, non prodotto SaaS nella prima fase. |

## Cosa Fa Bene Stimalo

- Presenta un flusso completo: costo, preventivo PDF, cliente, inventario e commessa.
- Ha cataloghi di stampanti e materiali gia pronti.
- Offre strategie prezzo multiple, utili per non ragionare solo su costo + margine.
- Punta su PWA e uso da browser anche mobile.
- Ha un approccio cloud con sicurezza, account, isolamento dati e GDPR dichiarati.
- Include funzioni utili per un service: inventario, FIFO, batch mode, alert, analytics e portale pubblico maker.

## Osservazioni Da Screenshot Stimalo

Le schermate fornite il 2026-07-08 mostrano Stimalo come gestionale web/PWA organizzato per workspace, catalogo, magazzino e insight.

### Dashboard

- La dashboard mette subito in evidenza profitto, fatturato, commesse attive, ore stampante e materiali attivi.
- La sidebar separa chiaramente workspace, marketplace, catalogo, magazzino, insight e sistema.
- Il tono e piu gestionale/SaaS rispetto a PreventiPiraz, con focus su metriche e andamento.
- La presenza di notifiche, lingua, tema e profilo rende il prodotto piu vicino a un gestionale cloud.

### Nuovo Preventivo

- Il preventivo e guidato a step: progetto e cliente, stampante e costi, stampe, lavorazioni extra, hardware, packaging, batch/multiplo.
- Il prezzo finale si aggiorna in tempo reale in una colonna laterale sempre visibile.
- Il breakdown separa materiale, energia, macchina, costo totale, margine, IVA e sconto.
- Il sistema distingue bene simulazione e salvataggio: senza salvataggio il preventivo non finisce nelle commesse.
- Sono previste anteprime/renders del progetto, massimo 5.
- L'import G-code/3MF e centrale: viene chiesto un file gia "sliced" per avere peso e tempo.
- La parte "Stampe" ragiona a piatti: ogni piatto puo avere stampante, materiale, peso e tempo.
- Lavorazioni extra, hardware e packaging sono blocchi separati dal costo di stampa.
- Il batch/multiplo e trattato come opzione specifica, utile per quantita di pezzi identici.

### Catalogo Materiali

- I materiali sono divisi per tecnologia: FDM, SLA, SLS.
- Il catalogo mostra schede compatte con nome, tipo, prezzo, scorta e azioni.
- Esiste un catalogo verificato con centinaia di materiali, da cui aggiungere materiali precompilati.
- Il materiale non e solo una stringa: densita, prezzo e specifiche possono arrivare gia pronti.

### Stampanti

- Le stampanti sono gestite come schede con nome, tipo, stato, costo orario, costo acquisto e ore stampate.
- Il catalogo verificato permette di aggiungere stampanti con specifiche tecniche precompilate.
- La modifica stampante separa dati tecnici di catalogo e dati economici dell'utente.
- I dati economici utili sono costo acquisto, vita stimata in ore, ore gia stampate, costo manutenzione, tasso fallimento, ricarico orario e potenza media misurata.
- Il costo orario non e solo un campo manuale: deriva da ammortamento, manutenzione ed eventuale ricarico.

### Magazzino

- Inventario, consumabili, prodotti ed eventi vendita sono funzioni separate.
- L'inventario ragiona su valore stock, materiali a basso stock, lotti aperti, acquisti e consumo FIFO.
- La "scorta rapida" permette aggiornamenti manuali semplici in grammi.
- I consumabili sono pensati per hardware/packaging e possono scaricarsi quando una commessa passa a "da incassare".
- I prodotti finiti e gli eventi vendita sono funzioni piu avanzate, interessanti ma non prioritarie per B3D Lab v1.

### Commesse E Insight

- Le commesse hanno stati gestionali chiari: preventivi, in corso, da incassare, pagate, archiviate.
- La lista commesse mostra numero, progetto, cliente, stato, data, importo e margine.
- Il confronto costi stampanti richiede almeno due stampanti e serve a capire quale macchina costa meno per uno specifico lavoro.
- Analytics, confronto e alert sono trattati come insight separati dal flusso base.

### Clienti

- La lista clienti mostra categoria, email, commesse, fatturato, margine medio e ultimo contatto.
- La creazione cliente puo essere rapida: nome/ragione sociale, email, telefono, indirizzo, categoria e note.
- Le categorie cliente possono avere un margine predefinito, applicabile automaticamente nel calcolatore ma modificabile.
- Per B3D Lab questa logica e interessante, ma va adattata: il margine cliente deve restare un suggerimento controllabile, non un automatismo cieco.

### Dati Per Esportazione PDF

- Le schermate mostrano che i PDF richiedono dati di contesto gia pronti: azienda, cliente, indirizzo, note, condizioni, progetto, stampante, materiale, costi, IVA, sconti e consegna.
- Senza dati di riempimento, il PDF rischia di essere formalmente generato ma povero o non inviabile.
- Per B3D Lab servira una sezione impostazioni con dati azienda, riferimenti, logo, condizioni standard, note fiscali/commerciali e testi riutilizzabili.
- Anche cliente, stampante e materiale devono avere campi sufficienti per alimentare il documento senza riscrivere tutto nel preventivo.

## Osservazioni Da PDF Esportati

File consultati il 2026-07-08:

- `Q-1 - Azienda [prova[.pdf`
- `preventivo_2225 (preventivo cliente).pdf`
- `preventivo_2225 (stima costi - interno).pdf`

### PreventiPiraz 3D

- La finestra di export distingue almeno due documenti: preventivo cliente e ordine di lavorazione.
- Il PDF cliente include dati azienda/brand, numero preventivo, data, anagrafica cliente, dati fiscali, modello 3D, materiale, quantita, prezzo unitario, IVA, totale, spedizione, acconto e metodo pagamento.
- Nella licenza/free o con flusso incompleto il PDF puo contenere watermark/nota del software e valori a zero.
- Per B3D Lab e importante evitare PDF "formalmente generati" ma non pronti: servono controlli prima dell'export.

### Stimalo - Preventivo Cliente

- Il PDF cliente mostra intestazione, numero commessa/preventivo, data, validita, cliente, progetto, descrizione e dettaglio economico sintetico.
- Espone solo macro-voci come materiale e stampa, non il calcolo interno completo.
- Include totale preventivo, nota fiscale/commerciale e condizioni standard.
- Il documento e breve e leggibile, adatto all'invio cliente.

### Stimalo - Stima Costi Interna

- Il PDF interno mantiene stesso numero, cliente e progetto, ma cambia titolo e contenuto.
- Mostra dettaglio costi di produzione: materiale, elettricita, ammortamento, costo totale, costi vivi, margine e totale offerto.
- E un buon riferimento per B3D Lab: stesso dato economico, due viste diverse, senza duplicare informazioni.

### Implicazioni Per B3D Lab

| Area | Implicazione |
|---|---|
| PDF cliente | Deve mostrare proposta leggibile, dati cliente, oggetto, sintesi economica e condizioni, senza dettaglio interno completo. |
| PDF interno | Deve mostrare costi, margine, ipotesi tecniche, materiale, macchina, tempi e note operative. |
| Controlli prima export | Prima di generare PDF cliente servono numero, cliente, configurazione scelta, totale, condizioni, dati azienda e note fiscali minime. |
| Dati condivisi | Cliente, progetto, configurazione, importi e condizioni devono alimentare entrambi i documenti senza duplicazioni. |
| Dati di riempimento | Dati azienda, logo, testi standard, pagamento, validita, consegna e note fiscali devono stare in impostazioni/template. |

## Requisiti Emersi Dagli Screenshot Stimalo

| Requisito | Stato | Nota |
|---|---|---|
| Preventivo guidato a step | Da valutare | Potrebbe rendere piu semplice il caso Arcipelago rispetto a una pagina unica lunga. |
| Prezzo live laterale | Da valutare | Utile per vedere subito totale, margine, IVA e sconto mentre si modificano costi/scenari. |
| Import dati da G-code/3MF | Da progettare | Stimalo conferma che il primo import utile non deve per forza partire da STL: puo partire da file gia sliced. |
| Blocchi extra separati | Da progettare | Lavorazioni extra, hardware e packaging andrebbero separati dai costi puri di stampa. |
| Materiali per tecnologia | Da progettare | FDM/SLA/SLS aiutano a tenere pulito il catalogo materiali. |
| Catalogo materiali precompilato | Da valutare | Riduce inserimenti manuali, ma per B3D Lab puo partire da una lista interna minima. |
| Catalogo stampanti precompilato | Da valutare | Utile per volume, tecnologia e specifiche base; i dati economici restano specifici dell'azienda. |
| Parametri costo stampante | Da progettare | Costo acquisto, vita stimata, ore stampate, manutenzione, fallimento e potenza aiutano a calcolare costo orario. |
| Inventario con scorta rapida | Da valutare | Utile per MVP magazzino senza introdurre subito FIFO completo. |
| Stati commessa economici | Da valutare | "Da incassare" e "Pagate" sono utili, ma vanno coordinati con gestione fiscale e fatturazione. |
| Dati di riempimento per PDF | Da progettare | Servono dati azienda, cliente, condizioni, logo, note standard e testi fiscali/commerciali riutilizzabili. |
| Categorie cliente con margine suggerito | Da valutare | Utile come suggerimento, ma nel profilo B3D Lab deve restare confermato manualmente. |
| Doppia esportazione cliente/interno | Da progettare | Stimalo conferma la necessita di PDF cliente sintetico e PDF interno dettagliato basati sugli stessi dati. |
| Controlli prima export PDF | Da progettare | Evitare PDF con dati mancanti, importi a zero o testi placeholder. |

## Cosa Fa Bene PreventiPiraz 3D

- E molto focalizzato sul problema concreto del service: tanti file da preventivare velocemente.
- Punta sul collegamento con slicer e profili reali, quindi riduce inserimenti manuali di peso e tempo.
- Supporta caricamento multiplo e formati legati alla stampa 3D, inclusi STL, STEP, OBJ e 3MF.
- Ha attenzione forte al multicolore e ai flussi Bambu/Orca/Prusa.
- Tiene i dati locali sul PC, aspetto coerente con chi non vuole cloud.
- Include clienti, materiali, stampanti, PDF, ordini di lavorazione, etichette, tabelle sconto e integrazioni gestionali.

## Osservazioni Da Screenshot PreventiPiraz 3D

Le schermate fornite il 2026-07-08 mostrano alcune scelte utili da considerare per B3D Lab.

### Preventivo

- Il numero preventivo viene proposto automaticamente e resta modificabile.
- L'anagrafica cliente e obbligatoria per attivare il salvataggio automatico.
- Il preventivo ha una intestazione compatta con numero, data, stato, consegna, cliente, pagamento e acconto.
- Il caricamento modelli 3D e centrale nel flusso.
- Il riassunto preventivo resta sempre visibile a destra con profit, materiale, ore stampa, totale stampa, servizi extra, spedizione, IVA e totale finale.
- Le azioni principali sono immediate: esporta PDF, stampa etichetta, avvia produzione.
- Il prezzo consigliato e separato dal totale, quindi resta un supporto e non una modifica nascosta.

### Materiali

- L'archivio materiali ha ricerca, importazione e creazione rapida.
- La scheda nuovo materiale e un pannello laterale, non una pagina isolata.
- Il materiale contiene profilo filamento, nome, codice prodotto/colore, colore, peso specifico, prezzo/kg, markup, rischio fallimento, magazzino, soglia scorte, consumo energia e link acquisto.
- Colore e codice prodotto sono trattati come dati importanti, non come semplici note.
- Prezzo/kg, magazzino e soglia scorte sono gia pensati per alimentare preventivi e alert.

### Impostazioni Operative

- Servizi extra, tariffe corrieri, metodi di pagamento, tabelle sconto e dati azienda sono gestiti come archivi configurabili.
- I servizi extra hanno importo predefinito, scelta se addebitarli e markup.
- Le tariffe corrieri separano corriere, servizio e costo spedizione.
- Questa impostazione evita di riscrivere sempre le stesse voci nel preventivo.

### Archivio E Produzione

- L'archivio preventivi ha ricerca per numero, cliente o note, filtro stato, importazione e creazione nuovo preventivo.
- La produzione e una sezione separata dai preventivi.
- La versione free mostra chiaramente i limiti della produzione, ma il flusso resta visibile come concetto operativo.

## Requisiti Emersi Dagli Screenshot

| Requisito | Stato | Nota |
|---|---|---|
| Numerazione automatica preventivi | Da progettare | Formato proposto: `B3D-PREV-2026-001`, con numero univoco e possibilita controllata di modifica manuale. |
| Liste editabili per materiali | Da progettare | Tipo materiale, marca, colore e altri valori ricorrenti non dovrebbero restare solo testo libero. |
| Archivi impostazioni operative | Da progettare | Servizi extra, corrieri, metodi pagamento e sconti possono diventare archivi semplici e riutilizzabili. |
| Riassunto preventivo sempre visibile | Da valutare | Utile nei preventivi lunghi o con piu scenari, per non perdere totale e margine. |
| Preventivo con righe/scenari confrontabili | Da valutare | Il caso Arcipelago puo evidenziare se le configurazioni attuali bastano o serve un confronto piu esplicito. |

## Dove Il Gestionale B3D Lab Deve Imparare

| Tema | Lezione |
|---|---|
| Calcolo costi | Servira arrivare a un calcolo piu rapido e meno manuale, almeno leggendo peso, tempo e dati slicer quando possibile. |
| Cataloghi | Un archivio stampanti/materiali precompilato riduce molto il lavoro iniziale. |
| Preventivi multipli/file multipli | Per lavori con molti pezzi, il caricamento multiplo diventa importante. |
| Strategie prezzo | Oltre al margine percentuale, potranno servire profili prezzo: competitivo, standard, premium, urgenza, cliente storico. |
| Magazzino | FIFO, lotti materiali e avvisi scorte sono funzioni da considerare dopo il flusso preventivo base. |
| Dashboard | La dashboard deve evolvere verso fatturato, materiale consumato, oggetti/lavori e scadenze operative. |
| PDF cliente | Il documento cliente deve essere sempre curato, personalizzabile e coerente con il posizionamento consulenziale. |

## Dove B3D Lab Resta Diverso

| Scelta B3D Lab | Motivo |
|---|---|
| Profilo principale "consulenza" | B3D Lab non vende solo stampa a pezzo: vende valutazione tecnica, progettazione, validazione e produzione quando serve. |
| Dettaglio economico interno separato | Il costo reale deve restare completo, ma il cliente vede una proposta coerente con il profilo scelto. |
| Memoria commerciale cliente | Accordi, NDA, listini firmati e condizioni particolari devono guidare il preventivo senza automatismi ciechi. |
| Documenti DOCX + PDF | Il DOCX modificabile e importante per template consulenza e documenti personalizzati. |
| Installazione locale su BMAX | Il primo uso reale deve funzionare in rete locale, con dati controllati direttamente. |
| Manuale operativo interno | Il gestionale deve essere comprensibile anche senza programmare o ricordare procedure esterne. |

## Gap Attuali Del Gestionale B3D Lab

| Priorita | Gap | Nota |
|---|---|---|
| Alta | Import file 3D e lettura dati tecnici | Peso, tempo macchina e anteprime oggi non sono automatici. |
| Alta | Cataloghi iniziali piu pronti | Materiali e stampanti vanno popolati meglio. |
| Alta | Prezzo assistito piu ricco | Oggi esiste margine + arrotondamento; mancano strategie prezzo e condizioni cliente strutturate. |
| Media | Magazzino reale | Mancano lotti, movimenti, FIFO, scorte minime e consumo materiale da commessa. |
| Media | Ordine di lavorazione | La commessa esiste, ma serve un documento operativo interno piu chiaro. |
| Media | Dashboard economica | Per ora e operativa; in futuro servono ricavi, margini, materiale consumato e lavori chiusi. |
| Futura | Integrazione fatturazione | Da valutare solo dopo aver stabilizzato preventivi, commesse e documenti. |

## Opportunita Da Valutare Per I Prossimi Sprint

1. **Sprint prova reale preventivo**  
   Usare un caso concreto e vedere quanto tempo richiede oggi rispetto a Stimalo/PreventiPiraz.

2. **Sprint dati tecnici da file/slicer**  
   Progettare import minimo di STL/3MF/G-code o almeno registrazione strutturata di peso, tempo, piatti e note slicing.

3. **Sprint cataloghi e parametri macchina/materiale**  
   Rendere piu veloce creare costi partendo da materiali e stampanti gia configurati.

4. **Sprint strategie prezzo**  
   Aggiungere profili prezzo manuali e tracciabili, senza applicazione automatica degli accordi cliente.

5. **Sprint documento operativo interno**  
   Generare un ordine di lavorazione interno da commessa con configurazione, materiale, note, file e controlli.

## Decisione Suggerita

Non conviene copiare Stimalo o PreventiPiraz 3D.

Conviene invece usare questa comparazione come bussola:

- PreventiPiraz e un riferimento forte per calcolo rapido da file/slicer.
- Stimalo e un riferimento forte per gestione web, cataloghi, inventario e strategie prezzo.
- B3D Lab deve mantenere il suo vantaggio specifico: preventivo consulenziale, memoria commerciale cliente, documenti personalizzati e controllo locale dei dati.

## Prossimo Passo Consigliato

Prima di aggiungere nuove automazioni, fare una prova reale con un preventivo tipo e misurare:

- quali dati devono essere inseriti a mano;
- quali passaggi fanno perdere tempo;
- quali informazioni mancano rispetto a Stimalo/PreventiPiraz;
- quali parti invece sono gia piu adatte al modo di lavorare B3D Lab.
