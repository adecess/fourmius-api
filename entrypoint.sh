#!/bin/sh

set -e

/.venv/bin/alembic upgrade head && echo "Migrations complete" && /.venv/bin/fastapi devw src/main.py --port 8000 --host 0.0.0.0 --reload