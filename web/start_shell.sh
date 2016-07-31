#!/bin/sh

echo "**** start_shell.sh ****"
apachectl -k restart
python manage.py runserver --insecure 0.0.0.0:8000
