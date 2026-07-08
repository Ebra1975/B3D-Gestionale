# Board Sprint 17 - Import dati tecnici da file G-code/3MF

## Problema pratico

Quando si prepara un preventivo, peso materiale e ore macchina arrivano spesso dallo slicer. Inserirli a mano espone a errori e rallenta il calcolo dei costi automatici.

## Fatto

- Aggiunto import file tecnico su ogni configurazione del preventivo.
- Supportati file `.gcode`, `.gco` e `.3mf`.
- L'import cerca peso materiale, tempo macchina e numero piatti nei metadati esportati dallo slicer.
- Peso e tempo aggiornano i campi gia esistenti della configurazione.
- Il dettaglio preventivo mostra peso e ore per unita accanto agli altri dati tecnici.
- La configurazione conserva una nota interna con origine del file e valori letti.
- I costi non vengono generati automaticamente: l'operatore usa poi **Genera costo materiale** e **Genera costo macchina** per mantenere controllo sul prezzo.

## Verifiche

- `python manage.py check`
- `python manage.py test apps.estimates`
- `python manage.py test`
- Controllo pagina locale dettaglio preventivo con pulsante **Importa G-code/3MF** e campi **Peso per unita** / **Ore per unita**.

## Rimandato

- Archiviazione del file tecnico originale.
- Preview grafica 3MF/G-code.
- Import completo multi-piatto con distribuzione per singolo pezzo.
- Riconoscimento avanzato specifico per ogni slicer.
