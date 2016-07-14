# coding: utf-8
import psycopg2
import sys

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

# All the contents will be in lowercase
TAGS = {
    # Companies
    'Google': ('google', 'googl', 'g家', '谷歌'),
    'Amazon': ('amazon', 'a家', '亚麻', '亚马逊', '亚玛逊'),
    'LinkedIn': ('linkedin', 'linkin', 'l家', '领英'),
    'Facebook': ('fb', 'facebook', '脸书'),
    'Microsoft': ('microsoft', 'm家', '微软'),
    'Airbnb': ('airbnb',),
    'Uber': ('uber', '优步'),

    # Other Keywords
    'Onsite': ('onsite',),
    'Resume': ('resume', '简历'),
    'OA': ('oa', '在线测试'),
    'Intern': ('intern', 'internship', '实习'),
}

query_cu.execute('SELECT link, title, description FROM interviews_post')
tuple_list = query_cu.fetchall()

for tu in tuple_list:
    tags = {}
    for (key, values) in TAGS.items():
        count_title = 0
        count_desc = 0
        for v in values:
            count_title += tu[1].count(v)
            count_desc += tu[2].count(v)
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
