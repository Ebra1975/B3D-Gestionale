# Copia Backup Fuori Dal BMAX

## Scopo

Questa procedura serve a conservare una copia dei backup fuori dal disco principale del mini PC BMAX.

Il problema pratico e semplice: se il disco principale del BMAX si rompe, un backup salvato solo sullo stesso disco non basta.

## Scelta Prima Versione

Prima soluzione consigliata:

- backup automatico giornaliero sul BMAX;
- copia periodica dell'ultimo backup su secondo disco interno, disco USB o NAS;
- verifica checksum dopo la copia.

La copia fuori dal BMAX non sostituisce il backup automatico: lo completa.

Nota importante: un secondo disco interno protegge dal guasto del disco principale, ma non protegge da furto, incendio o danno fisico dell'intero mini PC. Per dati reali importanti resta consigliata anche una copia periodica davvero esterna.

## Preparare Una Destinazione Esterna

Esempi di destinazione:

```text
/mnt/backup/b3d_backups
/mnt/b3d-backup
/mnt/b3d-backup-interno
/media/emanuele/NOME_DISCO
/mnt/nas-b3d-backup
```

La destinazione deve essere gia montata e visibile dal BMAX.

Per vedere dischi e mount disponibili:

```bash
lsblk
lsblk -f
df -h
```

Se e stato installato un secondo HD interno, prima non formattare nulla: controllare con `lsblk -f` come Debian vede il disco e quale partizione appartiene al sistema.

Prima verifica reale Sprint 19:

- secondo disco rilevato come `sda`;
- partizione utile `sda1`;
- filesystem `ext4`;
- etichetta `b3d-backup`;
- mount point `/mnt/backup`;
- cartella consigliata per i backup gestionali: `/mnt/backup/b3d_backups`;
- spazio disponibile circa 103 GB;
- nessuna formattazione necessaria.
- prima copia presente: `b3dlab_bmax_20260708_213425.tar.gz`.

Verifica successiva del 2026-07-09:

- backup creato: `b3dlab_bmax_20260709_075642.tar.gz`;
- copia completata in `/mnt/backup/b3d_backups`;
- checksum verificato dallo script;
- cartella dedicata controllata con `ls -lh /mnt/backup/b3d_backups`.
- Sprint 19 chiuso con copia su secondo disco verificata.

## Creare Un Backup Manuale

Entrare nella cartella del gestionale:

```bash
cd ~/gestionale-b3d
```

Rendere eseguibile lo script, se non lo e gia:

```bash
chmod +x scripts/bmax_copy_latest_backup.sh
```

Creare un backup:

```bash
scripts/bmax_backup.sh
```

Controllare che esista:

```bash
ls -lh backups/bmax
```

## Copiare L'ultimo Backup Fuori Dal BMAX

Esempio con destinazione reale BMAX `/mnt/backup/b3d_backups`:

```bash
EXTERNAL_BACKUP_DIR=/mnt/backup/b3d_backups scripts/bmax_copy_latest_backup.sh
```

Il comando:

- trova l'ultimo archivio `b3dlab_bmax_*.tar.gz`;
- lo copia nella destinazione esterna;
- calcola il checksum dell'origine e della copia;
- conferma se la copia e identica.

Messaggio finale atteso:

```text
Copia completata e verificata:
```

## Se La Destinazione Non Esiste

Se compare:

```text
Errore: destinazione esterna non trovata
```

controllare che il secondo disco interno, il disco USB o il NAS siano collegati e montati:

```bash
lsblk
lsblk -f
df -h
```

Non copiare backup in cartelle casuali se non si e sicuri che siano davvero fuori dal disco principale.

## Frequenza Consigliata

Prima versione:

- copia manuale dopo ogni prova importante;
- copia almeno settimanale se il gestionale contiene dati reali;
- prova periodica di ripristino da un backup copiato fuori dal BMAX.

Automatizzare la copia esterna con cron resta possibile, ma va fatto solo dopo aver scelto una destinazione stabile.
