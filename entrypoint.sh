#!/bin/bash
APP_PORT=${PORT:-8000}
cd /app/
gunicorn --worker-tmp-dir /dev/shm coplate_project.wsgi:application --bind "0.0.0.0:${APP_PORT}"