#from django.test import TestCase

# Create your tests here.

# list = [1,2,3,4,5,6]
# for i in list:
#     list2 = []
# print list2
import requests
from lxml import etree

r = requests.get("http://proxy.goubanjia.com/free/gngn/index.shtml")
page = etree.HTML(r.content)
ips = page.xpath("//td[@class='ip']")
# help(ips[0])
for ip in ips:
    ipstr = ""
    for child in ip.getchildren():
        style = child.get(key='style')
        if child.text and not (style and style.find("none") != -1):
            ipstr += child.text

    print (ipstr+":" +ip.getnext().text)

# trs = etree.HTML(r.content).xpath("//table[@class='table']/tbody/tr")
# help(trs[0])
# for tr in trs:
#     ip = tr.xpath("td[position() < 3]")
#     print (tds[0], tds[1].text)

# print(page.xpath("//td[@class='ip']"))
# print(page.xpath("//td[@class='port']"))
