#!/bin/sh
export PATH=$PATH:/usr/local/bin

echo "**** scrapy_all.sh ****"

time=$(date "+%Y-%m-%d %H:%M")

echo "${time}: *********** start run crawler 1p3_all *************" >> /logs/shell.log

# cd /code/web_scrapy
# ls >> /code/crontab.log
/usr/local/bin/scrapy crawl 1p3_all

time=$(date "+%Y-%m-%d %H:%M")
echo "${time}: *********** finish crawling 1p3_all *************" >> /logs/shell.log

