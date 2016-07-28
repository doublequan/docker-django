from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.utils.log import configure_logging



import psycopg2


conn = psycopg2.connect(database="postgres", user="postgres", host="0.0.0.0", port="5432")
cu = conn.cursor()

# cu.execute("SELECT * FROM interviews_post where source = %s ", ("1p4",))
# print cu.fetchall()

# cu.execute("INSERT INTO interviews_post (title, link, create_time, source, description, tag)"
#      " VALUES (%s, %s, %s, %s, %s, %s);", (
#          "New Title",
#          "www.link.com",
#          "'" + "2016-07-09 09:40:58" + "'",
#          "source",
#          "Description",
#          "Tag1 Tag2",
#      ))
# conn.commit()

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