set -e

mkdir -p /src/logs

cd /src

export DJANGO_SETTINGS_MODULE=config.settings

exec gunicorn config.wsgi:application \
    --name config \
    --reload \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --log-level=debug
    "$@"