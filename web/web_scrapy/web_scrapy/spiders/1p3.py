# coding: utf-8

import scrapy
import sys
import os
import re
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentdir)
from items import postItem

class oneP3Spider(scrapy.Spider):
    name = "1p3"
    allowed_domains = ["1point3acres.com"]
    start_urls = [
        "http://www.1point3acres.com/bbs/forum-28-1.html",
        # "http://www.1point3acres.com/bbs/forum-28-2.html",
        # "http://www.1point3acres.com/bbs/forum-28-3.html",
        # "http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=187005&extra=page%3D1%26filter%3Dsortid%26sortid%3D192%26sortid%3D192",
    ]

    def parse(self, response):
        '''
        parse the list page of 1p3.com, yield separate pages for late parse
        :param response:
        :return:
        '''
        self.logger.info("***Parsing List Page***")
        table = response.xpath("//table[@id = 'threadlisttableid']")
        #tbody_list = response.xpath("//table[@id = 'threadlisttableid']//tbody")
        a_list = response.xpath("//table[@id = 'threadlisttableid']//a[@class = 's xst']/@href").extract()
        # print len(a_list)

        for a in a_list:
            a_href = a.encode("utf-8")
            if self.is_new(a_href):

                # print "Yielding New Request :" + a_href
                yield scrapy.Request(a_href, callback=self.parse_page)

    def parse_page(self, response):
        self.logger.info("***Parsing Post Page***")

        postlist = response.xpath('//div[@id = \'postlist\']')
        title = postlist.xpath('//span[@id = \'thread_subject\']/text()').extract()[0].encode('utf-8')
        title = re.sub(r"'", "", title)

        link = response.url

        first_floor = postlist.xpath('div[1]/table/tr/td[@class = \'plc\']')
        time_list = first_floor.xpath('//div[@class = \'authi\']/em/span/@title').extract()
        if len(time_list) != 0:
            time = time_list[0].encode('utf-8')
        else:
            time = first_floor.xpath("//div[@class = 'authi']/em/text()").extract()[0].encode('utf-8')
            time = re.search(r"[0-9]{4}-[0-9]{1,2}-[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}", time).group(0)

        desc_unprocess = first_floor.xpath("//td[@class='t_f']").extract()[0].encode('utf-8')

        desc = self.process_desc_from1p3(desc_unprocess)

        item = postItem()
        item['title'] = title
        item['link'] = link
        item['create_time'] = time
        item['source'] = "1point3acres"
        item['source_link'] = "http://www.1point3acres.com/bbs/forum-28-1.html"
        item['desc'] = desc
        item['tag'] = ""
        yield item


    def is_new(self, url):
        return True

    def process_desc_from1p3(self, desc_un):
        desc = re.sub(r"(<.*?>)|(\n)", "", desc_un)
        pattern =  r"(注册一亩三分地论坛，查看更多干货！您需要 登录 才可以下载或查看，没有帐号？获取更多干货,去instant注册!)|" \
                   r"(. 涓�浜�-涓夊垎-鍦帮紝鐙鍙戝竷)|" \
                   r"(.鐣欏璁哄潧-涓�浜�-涓夊垎鍦�)|" \
                   r"(. Waral 鍗氬鏈夋洿澶氭枃绔�,)|" \
                   r"(. 鐣欏鐢宠璁哄潧-涓�浜╀笁鍒嗗湴)|" \
                   r"( 鏉ユ簮涓�浜�.涓夊垎鍦拌鍧�.)|" \
                   r"(.鏈枃鍘熷垱鑷�1point3acres璁哄潧)|" \
                   r"(. 1point 3acres 璁哄潧)|" \
                   r"(. 鍥磋鎴戜滑@1point 3 acres)|" \
                   r"(.1point3acres缃�)|" \
                   r"(. From 1point 3acres bbs)|" \
                   r"(. 1point3acres.com/bbs)|" \
                   r"(. more info on 1point3acres.com)|" \
                   r"(. 鐗涗汉浜戦泦,涓�浜╀笁鍒嗗湴)|" \
                   r"(. visit 1point3acres.com for more.)" \
                   r"|(')"
        desc = re.sub(pattern, "", desc)
        return desc