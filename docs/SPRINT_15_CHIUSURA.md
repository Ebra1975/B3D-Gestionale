# Sprint 15 - Chiusura

## Titolo

Numerazione automatica preventivi.

## Obiettivo Raggiunto

Il gestionale assegna automaticamente un numero progressivo ai nuovi preventivi quando il campo **Numero** viene lasciato vuoto.

Il numero segue il formato `B3D-ANNO-NNN`, ad esempio `B3D-2026-001`, e resta il riferimento unico del preventivo per lista, dettaglio, documenti generati e commesse collegate.

## Cosa E Stato Implementato

- Generazione automatica del numero preventivo al salvataggio.
- Ricerca del prossimo progressivo disponibile nello stesso anno.
- Campo numero facoltativo nella schermata di creazione/modifica preventivo.
- Testo di aiuto nella maschera: lasciare vuoto per assegnazione automatica.
- Validazione del formato `B3D-ANNO-NNN`.
- Migrazione database `estimates.0003_auto_estimate_number`.
- Test automatici dedicati alla numerazione.
- Aggiornamento di manuale operativo, decisioni e approvazioni.

## Scelte Di Prodotto Confermate

- Il formato iniziale approvato e `B3D-ANNO-NNN`.
- Il numero viene generato solo se il campo e vuoto.
- Il numero resta modificabile manualmente per casi controllati, ad esempio import di dati storici o correzioni deliberate.
- Non vengono introdotte serie separate per profilo consulenza e fornitura/artigiano nella prima versione.

## Verifiche

- `python -m compileall config apps`
- `python manage.py check`
- `python manage.py test apps.estimates`
- `python manage.py test`
- Migrazione applicata al database locale con `python manage.py migrate`.

## Documentazione Aggiornata

- `docs/DECISIONI.md`
- `docs/APPROVAZIONI.md`
- `docs/MANUALE_OPERATIVO.md`
- `docs/BOARD_SPRINT_15.md`
- `docs/SPRINT_15_CHIUSURA.md`

## Prossimo Sprint Proposto

**Sprint 16 - Archivi guidati materiali e parametri tecnici**

Obiettivo pratico: ridurre testo libero ripetuto in materiali, marche, colori e parametri tecnici usati nei preventivi, preparando una gestione piu ordinata del magazzino e delle configurazioni.
