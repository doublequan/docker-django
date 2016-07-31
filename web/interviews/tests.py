#from django.test import TestCase

# Create your tests here.

# list = [1,2,3,4,5,6]
# for i in list:
#     list2 = []
# print list2
import requests
from lxml import etree
import re

# req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#     'Accept':'text/html;q=0.9,*/*;q=0.8',
#     'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#     'Accept-Encoding':'gzip',
#     'Connection':'close',
#     'Referer':None,
# }
# r = requests.get("http://www.xicidaili.com/", headers=req_header)
# content = r.content
# trs = etree.HTML(content).xpath("//tr[@class='odd']")
# # help(trs[0])
# ips = []
# for tr in trs[:10]:
#     # print tr.xpath("td[2]")[0].text
#     ips += [tr.xpath("td[2]")[0].text + ":" + tr.xpath("td[3]")[0].text]
#     next = tr.getnext()
#     ips += [next.xpath("td[2]")[0].text + ":" + next.xpath("td[3]")[0].text]

# print ips

# content = '''
# {"i":"104.28.2.193","p":"80","c": {"f":"us","n": "United States"},"s":"0","tp":"HTTP","a":"Low","t":"700"},
# {"i":"108.162.196.76","p":"80","c": {"f":"us","n": "United States"},"s":"0","tp":"HTTP","a":"Low","t":"700"},
# {"i":"108.162.206.233","p":"80","c": {"f":"us","n": "United States"},"s":"0","tp":"HTTP","a":"Low","t":"700"},
# {"i":"104.28.9.2","p":"80","c": {"f":"us","n": "United States"},"s":"0","tp":"HTTP","a":"Low","t":"700"},
# {"i":"104.28.9.19","p":"80","c": {"f":"us","n": "United States"},"s":"0","tp":"HTTP","a":"Low","t":"700"},
# {"i":"104.28.9.18","p":"80","c": {"f":"us","n": "United States"},"s":"0","tp":"HTTP","a":"Low","t":"700"},
# {"i":"104.31.86.161","p":"80","c": {"f":"us","n": "United States"},"s":"0","tp":"HTTP","a":"Low","t":"700"},
# {"i":"104.28.10.101","p":"80","c": {"f":"us","n": "United States"},"s":"0","tp":"HTTP","a":"Low","t":"700"},
# {"i":"104.28.10.182","p":"80","c": {"f":"us","n": "United States"},"s":"0","tp":"HTTP","a":"Low","t":"700"},
# {"i":"104.28.1.5","p":"80","c": {"f":"us","n": "United States"},"s":"0","tp":"HTTP","a":"Low","t":"700"},
# '''

# m = re.findall(r'i', "dadsais")
# ip_list = re.findall(r'(?<="i":").*(?=","p":)', content)
# port_list = re.findall(r'(?<="p":").*(?=","c")', content)
#
# print len(ip_list), len(port_list)
# print ip_list
# print port_list

# help(ips[0])
# for ip in ips:
#     ipstr = ""
#     for child in ip.getchildren():
#         style = child.get(key='style')
#         if child.text and not (style and style.find("none") != -1):
#             ipstr += child.text
#
#     print (ipstr+":" +ip.getnext().text)


print range(1, 10)