# Board Sprint 16 - Parametri economici stampanti/materiali

## Problema pratico

I costi automatici di materiale e tempo macchina non devono dipendere da numeri troppo generici o ricordati a memoria. Serve vedere e aggiornare negli archivi i parametri economici che influenzano i preventivi.

## Fatto

- Aggiunti parametri economici ai materiali:
  - costo base per kg/litro;
  - scarto / extra materiale %;
  - note costo materiale.
- Aggiunti parametri economici alle stampanti:
  - costo orario base;
  - manutenzione per ora;
  - consumo stimato watt;
  - costo energia kWh;
  - rischio fallimento %;
  - note economiche.
- Le liste materiali e stampanti mostrano sia costo base sia costo usato.
- Il dettaglio preventivo mostra i parametri economici usati dalla configurazione.
- I pulsanti automatici **Genera costo materiale** e **Genera costo macchina** usano i costi effettivi e salvano una nota interna sulla voce di costo.
- Aggiornati decisioni, approvazioni e manuale operativo.

## Verifiche

- `python manage.py check`
- `python manage.py test apps.inventory apps.estimates`
- `python manage.py migrate`

## Rimandato

- Calcolo completo ammortamento da costo acquisto, vita stimata e ore gia stampate.
- Liste guidate per marca, colore e tipo materiale.
- Import automatico da G-code/3MF per peso e tempo.
