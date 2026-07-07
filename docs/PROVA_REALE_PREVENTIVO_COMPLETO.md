# Prova Reale - Preventivo Completo

Documento preparato il 2026-07-07 dopo la chiusura dello Sprint 08.

## Obiettivo

Verificare se il gestionale permette gia di preparare un preventivo completo in un flusso realistico:

- cliente;
- memoria commerciale;
- materiale e stampante;
- configurazione tecnica;
- costi interni;
- margine;
- controllo condizioni cliente;
- documento consulenza DOCX/PDF.

## Caso Usato

| Campo | Valore |
|---|---|
| Preventivo | B3D-2026-REAL-001 |
| Cliente | Officina Rossi Srl - prova reale |
| Oggetto | Consulenza e realizzazione staffa tecnica PETG CF |
| Quantita | 6 pezzi |
| Materiale | PETG CF prova reale |
| Stampante | Bambu Lab X1C prova reale |
| Profilo documento | Consulenza |

## Configurazione Tecnica

Configurazione scelta: **Staffa funzionale PETG CF - lotto 6 pezzi**.

Dati inseriti:

- processo FDM con profilo tecnico PETG CF;
- trattamento: rimozione supporti e controllo visivo;
- durata attesa: 2 giorni lavorativi dalla conferma file;
- peso stimato per pezzo: 0,085 kg;
- tempo macchina per pezzo: 1,40 ore;
- quantita: 6 pezzi.

## Risultato Economico Interno

| Voce | Importo |
|---|---:|
| Costo interno | 187,42 EUR |
| Margine commerciale | 65,60 EUR |
| Totale proposta | 253,02 EUR |
| Prezzo unitario | 42,17 EUR |

Il dettaglio economico resta interno e non viene esposto come lista voci nel documento cliente.

## Memoria Commerciale

Per il cliente sono stati registrati:

- accordo consulenza prototipi 2026;
- NDA sviluppo staffa macchina.

Nel preventivo e stata confermata manualmente la revisione condizioni cliente con nota interna:

> Controllati accordo consulenza prototipi 2026 e NDA sviluppo staffa macchina. Prezzo confermato manualmente dopo revisione.

## Documenti Generati

| Tipo | Esito |
|---|---|
| DOCX consulenza | Generato |
| PDF consulenza | Generato |

File generati:

- `media/generated/B3D-2026-REAL-001/consulting/preventivo_B3D-2026-REAL-001_consulenza_v1.docx`
- `media/generated/B3D-2026-REAL-001/consulting/preventivo_B3D-2026-REAL-001_consulenza_v1.pdf`

## Verifiche

| Controllo | Esito |
|---|---|
| Creazione cliente | OK |
| Creazione accordo e documento commerciale | OK |
| Creazione materiale e stampante | OK |
| Creazione preventivo | OK |
| Creazione configurazione tecnica | OK |
| Inserimento costi interni | OK |
| Applicazione margine manuale | OK |
| Conferma condizioni cliente | OK |
| Generazione DOCX | OK |
| Generazione PDF | OK |
| Apertura pagina preventivo locale | OK, risposta 200 |

## Cosa Funziona Bene

- Il flusso consulenza e gia utilizzabile da inizio a documento.
- Il dettaglio interno mantiene costi e margine separati dalla proposta cliente.
- La memoria commerciale evita di ignorare accordi o documenti importanti.
- La conferma condizioni cliente lascia traccia del controllo fatto.
- Il documento DOCX/PDF viene generato correttamente.

## Cosa Rallenta Oggi

- Peso materiale e tempo macchina devono essere inseriti a mano.
- Il margine e stato inserito manualmente; manca una scelta guidata tra strategie prezzo.
- Non c'e ancora import da file/slicer, quindi il confronto con PreventiPiraz 3D evidenzia un gap pratico.
- I cataloghi materiali/stampanti sono ancora poveri e vanno popolati meglio.
- Il PDF e generato, ma il layout cliente resta un template base, non ancora un modello grafico definitivo B3D Lab.

## Confronto Con Benchmark

Rispetto a PreventiPiraz 3D, il gestionale B3D Lab e piu debole sulla rapidita di preventivazione da file e dati slicer.

Rispetto a Stimalo, il gestionale B3D Lab e piu debole su cataloghi pronti, inventario e strategie prezzo.

Il gestionale B3D Lab e invece gia piu centrato su:

- proposta consulenziale;
- memoria commerciale cliente;
- tracciabilita della revisione;
- DOCX modificabile oltre al PDF;
- controllo locale dei dati.

## Prossimo Passo Consigliato

Aprire uno sprint dedicato a rendere piu veloce la preparazione tecnica del preventivo:

- dati tecnici da file/slicer, anche in forma minima;
- cataloghi materiali e stampanti piu pronti;
- strategie prezzo manuali ma guidate;
- report interno dei passaggi che oggi richiedono inserimento manuale.
