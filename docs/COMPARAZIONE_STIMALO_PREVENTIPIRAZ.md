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

## Cosa Fa Bene PreventiPiraz 3D

- E molto focalizzato sul problema concreto del service: tanti file da preventivare velocemente.
- Punta sul collegamento con slicer e profili reali, quindi riduce inserimenti manuali di peso e tempo.
- Supporta caricamento multiplo e formati legati alla stampa 3D, inclusi STL, STEP, OBJ e 3MF.
- Ha attenzione forte al multicolore e ai flussi Bambu/Orca/Prusa.
- Tiene i dati locali sul PC, aspetto coerente con chi non vuole cloud.
- Include clienti, materiali, stampanti, PDF, ordini di lavorazione, etichette, tabelle sconto e integrazioni gestionali.

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
