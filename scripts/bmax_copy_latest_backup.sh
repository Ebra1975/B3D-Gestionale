#!/usr/bin/env sh
set -eu

# Copia l'ultimo backup BMAX verso una destinazione esterna, ad esempio disco USB o NAS.
# Va eseguito dalla cartella del progetto, dove si trova docker-compose.yml.

PROJECT_DIR=${PROJECT_DIR:-$(pwd)}
BACKUP_DIR=${BACKUP_DIR:-"$PROJECT_DIR/backups/bmax"}
EXTERNAL_BACKUP_DIR=${EXTERNAL_BACKUP_DIR:-}

cd "$PROJECT_DIR"

if [ ! -f docker-compose.yml ]; then
  echo "Errore: eseguire lo script dalla cartella del progetto."
  exit 1
fi

if [ -z "$EXTERNAL_BACKUP_DIR" ]; then
  echo "Errore: indicare la destinazione esterna."
  echo "Esempio:"
  echo "EXTERNAL_BACKUP_DIR=/mnt/b3d-backup scripts/bmax_copy_latest_backup.sh"
  exit 1
fi

if [ ! -d "$BACKUP_DIR" ]; then
  echo "Errore: cartella backup non trovata: $BACKUP_DIR"
  exit 1
fi

if [ ! -d "$EXTERNAL_BACKUP_DIR" ]; then
  echo "Errore: destinazione esterna non trovata: $EXTERNAL_BACKUP_DIR"
  echo "Controllare che disco USB o NAS siano montati."
  exit 1
fi

LATEST_BACKUP=$(find "$BACKUP_DIR" -maxdepth 1 -name "b3dlab_bmax_*.tar.gz" -type f -printf "%T@ %p\n" | sort -nr | awk 'NR==1 {print $2}')

if [ -z "$LATEST_BACKUP" ]; then
  echo "Errore: nessun backup trovato in $BACKUP_DIR"
  echo "Creare prima un backup con:"
  echo "scripts/bmax_backup.sh"
  exit 1
fi

DESTINATION="$EXTERNAL_BACKUP_DIR/$(basename "$LATEST_BACKUP")"

echo "Ultimo backup trovato:"
echo "$LATEST_BACKUP"
echo "Copio verso:"
echo "$DESTINATION"

cp "$LATEST_BACKUP" "$DESTINATION"

SOURCE_HASH=$(sha256sum "$LATEST_BACKUP" | awk '{print $1}')
DESTINATION_HASH=$(sha256sum "$DESTINATION" | awk '{print $1}')

if [ "$SOURCE_HASH" != "$DESTINATION_HASH" ]; then
  echo "Errore: checksum diverso dopo la copia."
  echo "Origine:      $SOURCE_HASH"
  echo "Destinazione: $DESTINATION_HASH"
  exit 1
fi

echo "Copia completata e verificata:"
echo "$DESTINATION"
