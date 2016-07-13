# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2


# class CheckDuplication(object):
#     def process_item(self, item, spider):
#         return item
#
#
# class AddTag(object):
#     def process_item(self, item, spider):
#
#         return item


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
        pass

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
