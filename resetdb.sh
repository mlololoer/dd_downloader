#!/usr/bin/env bash
rm ./db.sqlite3
rm ./dd_downloader/migrations/000*
python3 ./manage.py makemigrations dd_downloader
python3 ./manage.py migrate
