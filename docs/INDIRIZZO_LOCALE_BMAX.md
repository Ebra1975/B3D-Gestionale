# Indirizzo Locale BMAX

## Scopo

Questa procedura serve ad aprire il gestionale B3D Lab con un nome facile da ricordare, invece dell'indirizzo IP del BMAX.

Obiettivo prima versione:

```text
http://b3d-gestionale.local:8000
```

Il problema pratico che risolve e semplice: l'indirizzo `192.168.1.143:8000` funziona, ma e scomodo da ricordare e puo cambiare se la rete viene riconfigurata.

## Scelta Prima Versione

Per la prima stabilizzazione si usa il nome locale:

```text
b3d-gestionale.local
```

Questa scelta non cambia architettura e non espone il gestionale su internet.

Resta in rete locale e continua a usare la porta:

```text
8000
```

Togliere anche `:8000` richiede un passaggio successivo con un proxy locale, ad esempio Nginx o Caddy. Non e necessario per il primo uso quotidiano.

## Impostare Il Nome Del BMAX

Sul BMAX impostare il nome macchina:

```bash
sudo hostnamectl set-hostname b3d-gestionale
```

Subito dopo, aggiornare anche il file `/etc/hosts`. Questo evita l'avviso:

```text
sudo: unable to resolve host b3d-gestionale: Name or service not known
```

Aprire il file:

```bash
sudo nano /etc/hosts
```

Controllare che ci siano almeno queste righe:

```text
127.0.0.1 localhost
127.0.1.1 b3d-gestionale
```

Se nella riga `127.0.1.1` c'e ancora il vecchio nome, sostituirlo con `b3d-gestionale`.

Salvare con:

```text
CTRL+O
INVIO
CTRL+X
```

Controllare:

```bash
hostnamectl
```

## Attivare Il Nome `.local`

Sui sistemi Linux il nome `.local` viene normalmente gestito da Avahi/mDNS.

Installare e attivare Avahi:

```bash
sudo apt update
sudo apt install avahi-daemon
sudo systemctl enable --now avahi-daemon
```

Controllare lo stato:

```bash
systemctl status avahi-daemon
```

## Aggiornare `.env`

Nel file `.env` del BMAX, aggiungere il nome locale tra gli host permessi da Django.

Esempio:

```text
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,192.168.1.143,b3d-gestionale.local
```

Dopo la modifica riavviare il gestionale:

```bash
docker compose up -d --build
docker compose exec web python manage.py check
```

## Verifica Dal Browser

Da un PC collegato alla stessa rete aprire:

```text
http://b3d-gestionale.local:8000
```

Controllare almeno:

- dashboard;
- clienti;
- preventivi;
- documenti.

Prima verifica reale Sprint 19:

- hostname BMAX impostato a `b3d-gestionale`;
- Avahi attivo e in registrazione su `b3d-gestionale.local`;
- file `/etc/hosts` corretto per evitare avvisi `sudo`;
- gestionale raggiungibile da browser su `http://b3d-gestionale.local:8000`.

## Se Il Nome Non Si Apre

Prima controllare se il gestionale funziona ancora con l'IP:

```text
http://192.168.1.143:8000
```

Se l'IP funziona ma il nome no, il problema e nella risoluzione del nome locale, non nel gestionale.

Sul BMAX controllare:

```bash
hostname
systemctl status avahi-daemon
```

Su Windows, se il nome `.local` non viene risolto dalla rete, ci sono due alternative semplici:

- configurare una prenotazione DHCP e un nome nel router;
- aggiungere temporaneamente una riga nel file `hosts` del PC Windows.

Esempio file `hosts` Windows:

```text
192.168.1.143 b3d-gestionale.local
```

Questa seconda soluzione funziona, ma vale solo per quel PC. La soluzione migliore resta il nome gestito dalla rete o da mDNS.

## Da Valutare In Futuro

Possibile evoluzione:

```text
http://b3d-gestionale.local
```

senza `:8000`.

Per arrivarci serve esporre il gestionale sulla porta standard `80`, preferibilmente con un proxy locale. Va fatto solo dopo avere confermato che il nome locale funziona bene.
