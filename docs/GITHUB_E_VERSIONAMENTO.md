# GitHub E Versionamento

## Scopo

GitHub serve come ponte ordinato tra sviluppo Windows e installazione sul BMAX Linux Server.

Il repository Git locale contiene il codice e la documentazione. Non deve contenere dati reali, database, file generati, backup o segreti.

## Stato Attuale

- Repository Git locale: presente.
- Branch locale: `master`.
- Remote GitHub: configurato.
- GitHub CLI: non installata sul PC al momento della verifica Sprint 03.
- Ultimo allineamento verificato GitHub/BMAX: commit `9a65339`, con recupero completo dello Sprint 17 e tutti i 18 sprint presenti sul BMAX.

Repository GitHub:

```text
https://github.com/Ebra1975/B3D-Gestionale
```

## File Da Non Caricare

Restano esclusi da Git:

- `.env`;
- `.venv/`;
- `db.sqlite3`;
- `media/`;
- `backups/`;
- `staticfiles/`;
- `__pycache__/`;
- log e file temporanei.

Questa scelta evita di caricare su GitHub dati cliente, documenti generati, password o backup.

## Creare Repository GitHub

Creare su GitHub un repository privato, ad esempio:

```text
gestionale-b3d-lab
```

Per questa fase e consigliato un repository privato.

## Collegare Il Repository Locale

Dopo aver creato il repository su GitHub, copiare l'URL del repository e configurare il remote:

```bash
git remote add origin URL_REPOSITORY_GITHUB
```

Esempio:

```bash
git remote add origin https://github.com/NOME_UTENTE/gestionale-b3d-lab.git
```

Verificare:

```bash
git remote -v
```

## Primo Invio Su GitHub

Inviare il branch locale:

```bash
git push -u origin master
```

Se GitHub chiede credenziali, usare il metodo consigliato da GitHub per Windows, ad esempio login via browser o token personale.

## Uso Sul BMAX

Quando il repository sara su GitHub, sul BMAX si usera:

```bash
git clone URL_REPOSITORY_GITHUB gestionale-b3d
```

Per aggiornare il BMAX dopo nuove modifiche:

```bash
git status
git pull
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py collectstatic --noinput
docker compose exec web python manage.py check
```

Prima di aggiornare il BMAX creare un backup seguendo `docs/BACKUP_E_RIPRISTINO.md`.

Dopo l'aggiornamento aprire il gestionale da browser e controllare almeno dashboard, clienti, preventivi e documenti.

## Regola Pratica

Prima di inviare modifiche a GitHub:

1. verificare il gestionale;
2. aggiornare la documentazione se cambia un flusso;
3. controllare `git status`;
4. creare un commit con messaggio chiaro;
5. inviare su GitHub.

## Completato Sprint 03

- Creato collegamento remote `origin`.
- Eseguito primo push del branch `master`.
- Il branch locale traccia `origin/master`.

## Verifica Sprint 18

- GitHub e BMAX sono stati controllati dopo il recupero dello Sprint 17.
- Il BMAX ha eseguito `git pull`, rebuild Docker, migrazioni, raccolta statici e `manage.py check` senza errori.
- Le pagine dashboard, preventivi e documenti hanno risposto correttamente da browser in rete locale.

## Da Fare

- Verificare che il repository resti privato.
- Continuare a usare GitHub come sorgente ufficiale per aggiornare il BMAX.
- Prima di ogni nuovo aggiornamento importante, creare un backup BMAX e poi verificare dashboard, preventivi e documenti.
