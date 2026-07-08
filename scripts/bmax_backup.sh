#!/usr/bin/env sh
set -eu

# Backup automatico per il BMAX Linux Server.
# Va eseguito dalla cartella del progetto, dove si trova docker-compose.yml.

PROJECT_DIR=${PROJECT_DIR:-$(pwd)}
BACKUP_DIR=${BACKUP_DIR:-"$PROJECT_DIR/backups/bmax"}
RETENTION_DAYS=${RETENTION_DAYS:-30}
MIN_FREE_MB=${MIN_FREE_MB:-1024}

cd "$PROJECT_DIR"

if [ ! -f docker-compose.yml ]; then
  echo "Errore: eseguire lo script dalla cartella del progetto."
  exit 1
fi

if [ -f .env ]; then
  set -a
  # shellcheck disable=SC1091
  . ./.env
  set +a
fi

POSTGRES_DB=${POSTGRES_DB:-b3dlab}
POSTGRES_USER=${POSTGRES_USER:-b3dlab}
COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME:-gestionale-b3d}
MEDIA_VOLUME=${MEDIA_VOLUME:-"${COMPOSE_PROJECT_NAME}_media_data"}

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
WORK_DIR="$BACKUP_DIR/work_$TIMESTAMP"
ARCHIVE_PATH="$BACKUP_DIR/b3dlab_bmax_$TIMESTAMP.tar.gz"

mkdir -p "$WORK_DIR"

FREE_MB=$(df -Pm "$BACKUP_DIR" | awk 'NR==2 {print $4}')
if [ "$FREE_MB" -lt "$MIN_FREE_MB" ]; then
  echo "Errore: spazio libero insufficiente in $BACKUP_DIR (${FREE_MB} MB disponibili)."
  echo "Soglia minima richiesta: ${MIN_FREE_MB} MB."
  rm -rf "$WORK_DIR"
  exit 1
fi

echo "Creo backup database PostgreSQL..."
docker compose exec -T db pg_dump -U "$POSTGRES_USER" "$POSTGRES_DB" > "$WORK_DIR/database.sql"

echo "Creo backup file media..."
docker run --rm \
  -v "$MEDIA_VOLUME:/media_data:ro" \
  -v "$WORK_DIR:/backup" \
  alpine tar -czf /backup/media.tar.gz -C /media_data .

if [ -f .env ]; then
  cp .env "$WORK_DIR/env.txt"
  chmod 600 "$WORK_DIR/env.txt"
else
  echo "Attenzione: file .env non trovato." > "$WORK_DIR/env_mancante.txt"
fi

cat > "$WORK_DIR/manifest.txt" <<EOF
Backup gestionale B3D Lab BMAX
Creato: $TIMESTAMP
Progetto Docker Compose: $COMPOSE_PROJECT_NAME
Database: $POSTGRES_DB
Utente database: $POSTGRES_USER
Volume media: $MEDIA_VOLUME
EOF

(
  cd "$WORK_DIR"
  sha256sum database.sql media.tar.gz manifest.txt $(find . -maxdepth 1 -name 'env*.txt' -printf '%f\n') > checksums.sha256
)

tar -czf "$ARCHIVE_PATH" -C "$WORK_DIR" .
rm -rf "$WORK_DIR"

if [ "$RETENTION_DAYS" -gt 0 ]; then
  find "$BACKUP_DIR" -maxdepth 1 -name "b3dlab_bmax_*.tar.gz" -type f -mtime +"$RETENTION_DAYS" -delete
fi

echo "Backup creato:"
echo "$ARCHIVE_PATH"
