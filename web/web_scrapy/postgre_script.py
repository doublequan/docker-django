from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.utils.log import configure_logging


# import sys
# sys.path.append("/code/interviews/")

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_django.settings")

import psycopg2


conn = psycopg2.connect(database="postgres", user="postgres", host="db", port="5432")
cur = conn.cursor()
cur.execute("CREATE TABLE testFuck(id serial PRIMARY KEY, num integer,data varchar);")
conn.commit()

# import models
# from interviews.models import Post

# from 1p3 import oneP3Spider

# configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
# runner = CrawlerRunner()
#
# d = runner.crawl(OneP3acresSpider)
# d.addBoth(lambda _: reactor.stop())
# reactor.run() # the script will block here until the crawling is finished

# process = CrawlerProcess()
# process.crawl(OneP3Spider)
# # process.crawl(OneP3acresSpider)
# process.start() # the script will block here until all crawling jobs are finished