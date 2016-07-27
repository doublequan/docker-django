# coding: utf-8
from settings import TAGS
import psycopg2
import sys
import chardet


conn = psycopg2.connect(database="postgres", user="postgres", host="db", port="5432")
query_cu = conn.cursor()

CLEAN = False
CLEAN = True
if CLEAN:
    query_cu.execute('UPDATE interviews_post SET tag = %s', ('',))
    conn.commit()
    # query_cu.close()
    # conn.close()
    # sys.exit("Clean Completed")



query_cu.execute('SELECT link, title, description FROM interviews_post')
tuple_list = query_cu.fetchall()

for tu in tuple_list:
    tags = {}
    for (key, values) in TAGS.items():
        count_title = 0
        count_desc = 0
        for v in values:
            # if v == 'g家':
            #     print chardet.detect(tu[1].lower()), v, chardet.detect(v)
            #     print v.decode('utf-8'), tu[1].lower().count(v.decode('utf-8'))
            count_title += tu[1].lower().count(v)
            count_desc += tu[2].lower().count(v)
        score = count_title * 10 + count_desc * 2
        if score > 0:
            tags[key] = score
    tags_sorted = sorted(tags.iteritems(), key=lambda d: d[1], reverse=True)
    # print tags
    tag_str = ""
    for tag_tuple in tags_sorted:
        tag_str += tag_tuple[0] + " "

    query_cu.execute('UPDATE interviews_post SET tag = %s WHERE link = %s',
                     (tag_str, tu[0]))
    conn.commit()


query_cu.close()
conn.close()
