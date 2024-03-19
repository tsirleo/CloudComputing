#!/bin/sh

set -e

. /venv/bin/activate

uvicorn src.api.app:app --forwarded-allow-ips='*' --host 0.0.0.0 --port 12345