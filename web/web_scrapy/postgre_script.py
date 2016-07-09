# from twisted.internet import reactor
# from scrapy.crawler import CrawlerRunner, CrawlerProcess
# from scrapy.utils.log import configure_logging


import sys
sys.path.append("/code/")

import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_django.settings')

from django.conf import settings  # noqa

from web.interviews.models import Post


# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_django.settings")

# from django.apps import apps
#
# post = apps.get_models("interviews.Post")
# print post


# import models
# from interviews.models import Post

print "haha"

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