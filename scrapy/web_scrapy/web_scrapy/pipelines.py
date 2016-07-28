# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from settings import TAGS
import psycopg2


class PutIntoDB(object):
    def __init__(self):
        self.conn = psycopg2.connect(database="postgres", user="postgres", host="db", port="5432")
        self.query_cu = self.conn.cursor()

    def process_item(self, item, spider):
        if self.check_duplication(item):
            self.add_tags(item)
            self.put_into_db(item)

        return item

    def check_duplication(self, item):
        '''

        :param item:
        :return Boolean, true if no duplication in db:
        '''
        self.query_cu.execute('SELECT * FROM interviews_post WHERE link = %s'
                              , (item["link"],))
        rst = self.query_cu.fetchall()
        if not rst:
            return True
        else:
            return False

    def add_tags(self, item):
        '''

        :param item:
        :return:
        '''
        tags = {}
        for (key, values) in TAGS.items():
            count_title = 0
            count_desc = 0
            for v in values:
                count_title += item['title'].lower().count(v)
                count_desc += item['desc'].lower().count(v)
            score = count_title * 10 + count_desc * 2
            if score > 0:
                tags[key] = score
        tags_sorted = sorted(tags.iteritems(), key=lambda d: d[1], reverse=True)
        # print tags
        tag_str = ""
        for tag_tuple in tags_sorted:
            tag_str += tag_tuple[0] + " "

        item['tag'] = tag_str


    def put_into_db(self, item):
        '''

        :param item:
        :return:
        '''
        cu = self.conn.cursor()

        cu.execute("INSERT INTO interviews_post (title, link, create_time, source, description, tag, source_link)"
                   " VALUES (%s, %s, %s, %s, %s, %s, %s);", (
            item['title'],
            item['link'],
            "'" + item['create_time'] + "'",
            item['source'],
            item['desc'],
            item['tag'],
            item['source_link']
        ))

        self.conn.commit()
        cu.close()
