# Board Sprint 20 - Pulizia dati test e preparazione uso reale

## Obiettivo

Preparare il gestionale all'uso reale dopo le verifiche BMAX, eliminando i dati test in modo controllato e lasciando un ambiente leggibile e delegabile.

## Problema Pratico

I test PDF, demo e backup hanno creato dati riconoscibili ma non reali. Prima di usare il gestionale con clienti veri serve una procedura che dica cosa verra pulito, richieda conferma e non tocchi configurazioni utili come template, dati documento e backup.

## Attivita

| Stato | Attivita | Risultato |
|---|---|---|
| Fatto | Comando di anteprima dati test | `prepare_real_use` mostra cosa verrebbe rimosso senza cancellare nulla. |
| Fatto | Pulizia protetta da conferma | La cancellazione richiede `--apply --confirm "PULISCI DATI TEST"`. |
| Fatto | Protezione dati potenzialmente reali | Clienti demo con collegamenti reali non vengono eliminati. |
| Fatto | Documentazione operativa | Procedura dedicata, manuale, manutenzione e README aggiornati. |
| Fatto | Test automatici | Verificano anteprima e protezione dei dati reali collegati. |

## Criterio Di Chiusura

Lo sprint e chiuso quando:

- la pulizia e prima visibile in anteprima;
- la cancellazione reale richiede conferma esplicita;
- i dati utili all'uso reale non vengono svuotati;
- la procedura e comprensibile e delegabile;
- la documentazione e allineata.
