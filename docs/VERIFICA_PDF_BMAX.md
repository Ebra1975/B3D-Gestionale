# Verifica PDF BMAX

## Scopo

Questa procedura controlla che il BMAX generi davvero i documenti `.docx` e `.pdf` dal gestionale.

Il problema pratico e importante: un preventivo non basta crearlo nel gestionale, deve anche diventare un PDF apribile e inviabile.

## Verifica Automatica Consigliata

Entrare nel BMAX:

```bash
cd ~/gestionale-b3d
```

Aggiornare il codice:

```bash
git pull
```

Ricostruire il gestionale se sono arrivati aggiornamenti:

```bash
docker compose up -d --build
```

Controllare che LibreOffice sia presente nel container web:

```bash
docker compose exec web libreoffice --version
```

Controllare Django:

```bash
docker compose exec web python manage.py check
```

Lanciare la verifica:

```bash
docker compose exec web python manage.py verify_pdf_export
```

## Risultato Atteso

Il comando deve mostrare:

- LibreOffice trovato;
- numero del preventivo test creato;
- percorso DOCX cliente;
- percorso PDF cliente;
- percorso DOCX interno;
- percorso PDF interno;
- percorso DOCX fornitura/artigiano;
- percorso PDF fornitura/artigiano;
- messaggio finale di verifica completata.

Esempio di messaggio finale atteso:

```text
Verifica PDF completata: DOCX e PDF generati correttamente.
```

## Dove Vedere I File

Dal browser:

```text
http://b3d-gestionale.local:8000/documenti/
```

Il comando crea un cliente e un preventivo riconoscibili:

```text
TEST PDF BMAX - eliminabile
TEST PDF BMAX - verifica conversione LibreOffice
```

Questi dati sono di prova e possono essere eliminati piu avanti, quando verra aggiunta una procedura di pulizia ordinata.

## Se Il PDF Non Viene Generato

Se il comando crea il DOCX ma non il PDF, controllare:

```bash
docker compose exec web libreoffice --version
docker compose logs web
```

Se compare un errore simile a:

```text
Could not find config for 'default' in settings.STORAGES
```

aggiornare il codice e ricostruire:

```bash
git pull
docker compose up -d --build
```

Se LibreOffice non risponde, ricostruire:

```bash
docker compose up -d --build
```

Poi ripetere:

```bash
docker compose exec web python manage.py verify_pdf_export
```
