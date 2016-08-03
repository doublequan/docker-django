#!/bin/sh

echo "**** start_shell.sh ****"

echo "*** start apache server ***"
apachectl -k restart

echo "*** start cron task ***"
cron

echo "*** start django server ***"
python manage.py runserver --insecure 0.0.0.0:8000
