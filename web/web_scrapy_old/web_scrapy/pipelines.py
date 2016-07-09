# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import psycopg2
import sys
sys.path.append("/code/interviews")
sys.path.append("/code")
# from interviews.models import Post

class Pipeline1(object):
    def __init__(self):
        pass
        # db_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # self.db = sqlite3.connect(db_path + "/db.sqlite3")
        # self.conn = psycopg2.connect("dbname = test user = postgres")

    def process_item(self, item, spider):
        # print "*****************process items****************"

        # print item['title']
        # print item['link']
        # print item['time']
        # print item['source']
        # print item['desc']
        cu = self.conn.cursor()
        cu.execute("insert into interviews_items values("
                   "'" + item['title'] + "', '" +
                   item['link'] + "', '" +
                   item['time'] + "', '" +
                   item['source'] + "', '" +
                   item['desc'] + "', '" +
                   item['tag'] +
                   "')")
        self.conn.commit()
        cu.close()
        return item

print sys.path
