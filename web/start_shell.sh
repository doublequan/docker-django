#!/bin/sh

echo "**** start_shell.sh ****"
apachectl start
python manage.py runserver --insecure 0.0.0.0:8000
