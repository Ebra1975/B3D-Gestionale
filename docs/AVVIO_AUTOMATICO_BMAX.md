# Avvio Automatico BMAX

## Scopo

Questa procedura serve a fare ripartire il gestionale B3D Lab automaticamente dopo un riavvio del mini PC BMAX.

Il problema pratico e semplice: se manca corrente, il server viene aggiornato o il BMAX si riavvia, il gestionale deve tornare raggiungibile in rete locale senza dover ricordare ogni volta i comandi Docker.

## Cosa Cambia Nel Gestionale

Nel file `docker-compose.yml` i servizi principali hanno `restart: unless-stopped`.

Questo significa:

- se Docker riparte dopo un riavvio, prova a riaccendere i contenitori;
- se un servizio si ferma per errore, Docker prova a riavviarlo;
- se l'operatore ferma volontariamente i servizi con `docker compose stop`, Docker rispetta lo stop.

Servizi coperti:

- `web`;
- `worker`;
- `beat`;
- `db`;
- `redis`.

## Prima Attivazione Sul BMAX

Prima di provare il riavvio automatico, assicurarsi che il BMAX abbia ricevuto l'ultima versione del progetto da GitHub:

```bash
cd /percorso/gestionale-b3d
git pull
```

Entrare nella cartella del gestionale sul BMAX:

```bash
cd /percorso/gestionale-b3d
```

Aggiornare i contenitori con la nuova regola di riavvio:

```bash
docker compose up -d --build
```

Controllare che siano accesi:

```bash
docker compose ps
```

Verificare il gestionale dal browser:

```text
http://192.168.1.143:8000
```

## Verifica Dopo Riavvio

Quando si vuole provare davvero l'avvio automatico:

```bash
sudo reboot
```

Dopo qualche minuto, rientrare sul BMAX e controllare:

```bash
cd /percorso/gestionale-b3d
docker compose ps
```

Poi aprire dal browser:

```text
http://192.168.1.143:8000
```

Controllare almeno:

- dashboard;
- clienti;
- preventivi;
- documenti.

Prima verifica reale Sprint 19:

- BMAX acceso dopo riavvio;
- gestionale aggiornato da GitHub;
- servizi riavviati con Docker Compose;
- gestionale nuovamente raggiungibile in rete locale.

## Servizio Systemd Opzionale

La regola `restart: unless-stopped` dovrebbe gia coprire l'avvio automatico nella maggior parte dei casi.

Se si vuole un controllo piu esplicito a livello Linux, si puo aggiungere anche un servizio `systemd` che esegue `docker compose up -d` all'avvio.

Creare il file:

```bash
sudo nano /etc/systemd/system/b3d-gestionale.service
```

Contenuto di esempio:

```ini
[Unit]
Description=Gestionale B3D Lab
Requires=docker.service
After=docker.service network-online.target
Wants=network-online.target

[Service]
Type=oneshot
WorkingDirectory=/percorso/gestionale-b3d
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose stop
RemainAfterExit=yes
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
```

Sostituire `/percorso/gestionale-b3d` con la cartella reale del progetto sul BMAX.

Attivare il servizio:

```bash
sudo systemctl daemon-reload
sudo systemctl enable b3d-gestionale.service
sudo systemctl start b3d-gestionale.service
```

Controllare lo stato:

```bash
systemctl status b3d-gestionale.service
```

## Se Dopo Il Riavvio Non Riparte

Se il BMAX e acceso ma il gestionale non si apre dal browser, fare questi controlli in ordine.

### 1. Riaccendere Subito Il Gestionale

```bash
cd /percorso/gestionale-b3d
docker compose up -d
docker compose ps
```

Poi riaprire:

```text
http://192.168.1.143:8000
```

### 2. Controllare Docker

```bash
systemctl status docker
```

Se Docker non e attivo:

```bash
sudo systemctl enable --now docker
```

Poi ripetere:

```bash
cd /percorso/gestionale-b3d
docker compose up -d
```

### 3. Controllare Che La Nuova Configurazione Sia Sul BMAX

```bash
cd /percorso/gestionale-b3d
git pull
grep -n "restart:" docker-compose.yml
```

Il comando deve mostrare piu righe `restart: unless-stopped`.

### 4. Se Serve, Attivare Systemd

Se Docker parte ma il gestionale non viene riportato su in modo affidabile dopo reboot, usare il servizio `systemd` documentato sopra.

## Quando Usare Solo Docker Compose

Per la gestione ordinaria restano validi i comandi gia documentati:

```bash
docker compose ps
docker compose restart
docker compose stop
docker compose up -d
```

## Cosa Non Fare

- Non cancellare volumi Docker per risolvere problemi di avvio.
- Non modificare `.env` senza sapere quale valore si sta cambiando.
- Non disattivare il backup automatico mentre si prova il riavvio.

Se dopo il riavvio il gestionale non si apre, creare prima un backup manuale se possibile e controllare i log prima di fare modifiche.
