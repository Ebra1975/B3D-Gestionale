#!/usr/bin/env sh
set -eu

# Prova di ripristino sicura per backup BMAX.
# Usa contenitori e volumi Docker temporanei, senza toccare il gestionale reale.

if [ "$#" -ne 1 ]; then
  echo "Uso: scripts/bmax_restore_test.sh backups/bmax/b3dlab_bmax_YYYYMMDD_HHMMSS.tar.gz"
  exit 1
fi

ARCHIVE_PATH=$1
if [ ! -f "$ARCHIVE_PATH" ]; then
  echo "Errore: archivio non trovato: $ARCHIVE_PATH"
  exit 1
fi

PROJECT_DIR=${PROJECT_DIR:-$(pwd)}
TEST_ID=$(date +"%Y%m%d_%H%M%S")
RESTORE_DIR="$PROJECT_DIR/backups/restore-test-$TEST_ID"
DB_CONTAINER="b3dlab_restore_db_$TEST_ID"
DB_VOLUME="b3dlab_restore_pg_$TEST_ID"
MEDIA_VOLUME="b3dlab_restore_media_$TEST_ID"

cleanup() {
  if [ "${KEEP_RESTORE_TEST:-0}" != "1" ]; then
    docker rm -f "$DB_CONTAINER" >/dev/null 2>&1 || true
    docker volume rm "$DB_VOLUME" "$MEDIA_VOLUME" >/dev/null 2>&1 || true
    rm -rf "$RESTORE_DIR"
  fi
}
trap cleanup EXIT

mkdir -p "$RESTORE_DIR"
tar -xzf "$ARCHIVE_PATH" -C "$RESTORE_DIR"

if [ ! -f "$RESTORE_DIR/database.sql" ] || [ ! -f "$RESTORE_DIR/media.tar.gz" ]; then
  echo "Errore: l'archivio non contiene database.sql e media.tar.gz."
  exit 1
fi

if [ -f "$RESTORE_DIR/checksums.sha256" ]; then
  (
    cd "$RESTORE_DIR"
    sha256sum -c checksums.sha256
  )
fi

BACKUP_POSTGRES_DB=$(awk -F': ' '/^Database:/ {print $2}' "$RESTORE_DIR/manifest.txt" 2>/dev/null || true)
BACKUP_POSTGRES_USER=$(awk -F': ' '/^Utente database:/ {print $2}' "$RESTORE_DIR/manifest.txt" 2>/dev/null || true)

POSTGRES_DB=${RESTORE_POSTGRES_DB:-${BACKUP_POSTGRES_DB:-b3dlab}}
POSTGRES_USER=${RESTORE_POSTGRES_USER:-${BACKUP_POSTGRES_USER:-b3dlab}}
POSTGRES_PASSWORD=b3dlab_restore_test

docker volume create "$DB_VOLUME" >/dev/null
docker volume create "$MEDIA_VOLUME" >/dev/null

docker run -d --name "$DB_CONTAINER" \
  -e POSTGRES_DB="$POSTGRES_DB" \
  -e POSTGRES_USER="$POSTGRES_USER" \
  -e POSTGRES_PASSWORD="$POSTGRES_PASSWORD" \
  -v "$DB_VOLUME:/var/lib/postgresql/data" \
  postgres:16-alpine >/dev/null

echo "Attendo avvio PostgreSQL di test..."
for _ in $(seq 1 30); do
  if docker exec "$DB_CONTAINER" pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB" >/dev/null 2>&1; then
    break
  fi
  sleep 1
done

docker exec "$DB_CONTAINER" pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB" >/dev/null

echo "Ripristino database in ambiente di test..."
docker exec -i "$DB_CONTAINER" psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" "$POSTGRES_DB" < "$RESTORE_DIR/database.sql" >/dev/null

echo "Ripristino media in volume di test..."
docker run --rm \
  -v "$MEDIA_VOLUME:/media_data" \
  -v "$RESTORE_DIR:/backup:ro" \
  alpine tar -xzf /backup/media.tar.gz -C /media_data

TABLE_COUNT=$(docker exec "$DB_CONTAINER" psql -U "$POSTGRES_USER" "$POSTGRES_DB" -tAc "select count(*) from information_schema.tables where table_schema = 'public';")
MEDIA_COUNT=$(docker run --rm -v "$MEDIA_VOLUME:/media_data:ro" alpine sh -c "find /media_data -type f | wc -l")

echo "Prova ripristino completata."
echo "Tabelle database ripristinate: $TABLE_COUNT"
echo "File media ripristinati: $MEDIA_COUNT"

if [ "${KEEP_RESTORE_TEST:-0}" = "1" ]; then
  echo "Ambiente di test mantenuto:"
  echo "Container DB: $DB_CONTAINER"
  echo "Volume DB: $DB_VOLUME"
  echo "Volume media: $MEDIA_VOLUME"
fi
