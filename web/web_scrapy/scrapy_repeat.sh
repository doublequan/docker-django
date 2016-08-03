#!/bin/sh
export PATH=$PATH:/usr/local/bin

echo "**** scrapy_repeat.sh ****"

time=$(date "+%Y-%m-%d %H:%M")

echo "${time}: start run crawler 1p3" >> /code/logs/shell.log

# cd /code/web_scrapy
/usr/local/bin/scrapy crawl 1p3

time=$(date "+%Y-%m-%d %H:%M")
echo "${time}: finish crawling" >> /code/logs/shell.log

