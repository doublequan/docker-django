# coding: utf-8
import os

from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from models import Post
import chardet
import random
import re

from django.utils.http import urlunquote, urlquote

# tips displayed in search placeholder
tips = ("搜索关键词，例如：Google",
        "空格隔开关键词,例如:Amazon onsite",
        )

# Tags for keyword transfer while searching
# All the contents will be in lowercase
TAGS = {
    # Companies
    'Google': ('google', 'googl', 'g家', '谷歌'),
    'Amazon': ('amazon', 'a家', '亚麻', '亚马逊', '亚玛逊'),
    'LinkedIn': ('linkedin', 'linkin', 'l家', '领英'),
    'Facebook': ('fb', 'facebook', '脸书', 'f家'),
    'Microsoft': ('microsoft', 'm家', '微软'),
    'Airbnb': ('airbnb',),
    'Uber': ('uber', '优步'),

    # Other Keywords
    'Onsite': ('onsite',),
    'Resume': ('resume', '简历'),
    'OA': ('oa', '在线测试'),
    'Intern': ('intern', 'internship', '实习'),
}

def index(request):
    all_posts = Post.objects.all()

    content_newest_models = all_posts.order_by("-create_time")[:10]
    content_newest = [(models, models.create_time.strftime("%b %d"))
                      for models in content_newest_models]


    board_names = ("Google",
                   "Amazon",
                   "Facebook",
                   "Linkedin",
                   "Uber",
                   "Microsoft",
                   # "Airbnb",
                   "Onsite",
                   "Intern")

    boards = []
    for board_name in board_names:
        args = (Q(tag__icontains=board_name),)
        board_content_models = all_posts.filter(*args).order_by("-create_time")[:10]
        board_content = [(models, models.create_time.strftime("%b %d")) for models in board_content_models]
        boards += [(board_name, board_content)]

    # print all_posts[0].create_time.strftime("%d %b")

    content = {
        "total_num": len(all_posts),
        "content_newest": content_newest,
        "boards": boards,
        "tips": random.choice(tips)
    }
    return render(request, 'interviews/index.html', content)


def search(request):

    # get the GET params from request
    if request.GET.get('pn'):
        current_page_id = request.GET.get('pn')
    else:
        current_page_id = 1
    current_page_id = int(current_page_id)

    # set the results you wanna to show on each page
    result_num_each_page = 10

    # get all required posts from db
    keyword = ""
    if request.GET.get('wd') and request.GET.get('wd').encode('utf-8') != "":
        keyword = request.GET.get('wd').encode('utf-8')
        wds = keyword.split(" ")
        wds = filter(None, wds)
        # transfer specific kw to tags
        for i in range(0, len(wds)):
            for (key, values) in TAGS.items():
                if wds[i] in values:
                    wds[i] = key
                    break

        print wds

        # search using multiple keywords
        args = ()
        for wd in wds:
            args += (Q(title__icontains=wd) |
                     Q(description__icontains=wd) |
                     Q(tag__icontains=wd),)

        all_posts = Post.objects.filter(*args)

        # Sorting Algorithm

        # End of Sorting
    else:
        all_posts = Post.objects.all()
    # print chardet.detect(request.GET.get('wd').encode('utf-8'))

    # get total nums of results and calculate total page nums
    result_num = len(all_posts)
    total_page_num = result_num / result_num_each_page + 1

    # if the required page id is invalid, return 404 page
    if current_page_id > total_page_num or current_page_id <= 0:
        raise Http404("No Such Page!")

    # deal with next_page, prev_page
    # False if need to be disabled, otherwise the target url
    prev_page = False
    next_page = False
    if current_page_id > 1:
        url = "/search?pn=%d&wd=%s" % (current_page_id - 1, urlquote(keyword))
        prev_page = url
    if current_page_id < total_page_num:
        url = "/search?pn=%d&wd=%s" % (current_page_id + 1, urlquote(keyword))
        next_page = url

    # deal with pages
    # False if no need to show page
    # otherwise make it a list of (id of page, url of page)
    pages = []
    if total_page_num == 1:
        pages = False
    elif total_page_num <= 5:
        for i in range(1, total_page_num + 1):
            url = "/search?pn=%d&wd=%s" % (i, urlquote(keyword))
            pages += [(i, url)]
            # print url
    else:
        start_page = max(1, current_page_id - 2)
        end_page = min(total_page_num, current_page_id + 2)
        if end_page - start_page + 1 < 5:
            if end_page == total_page_num:
                start_page = end_page - 4

        for i in range(start_page, start_page + 5):
            url = "/search?pn=%d&wd=%s" % (i, urlquote(keyword))
            pages += [(i, url)]

    # calculate the items we are going to show
    # put the items and their tags in the list [items]
    start_id = (current_page_id - 1) * result_num_each_page
    end_id = start_id + result_num_each_page
    item_list = all_posts.order_by('-create_time')[start_id : end_id]
    items = []
    for item in item_list:
        tags = [n for n in item.tag.split(' ') if n.strip()]
        items += [[item, tags]]

    # calculate the truely item start and end id
    start_id += 1
    end_id = start_id + len(item_list) - 1

    content = {
        "items": items,
        "result_num": result_num,
        "pages": pages,
        "page_num": total_page_num,
        "current_page_num": current_page_id,
        "prev_page": prev_page,
        "next_page": next_page,
        "item_start_id": start_id,
        "item_end_id": end_id,
        "search_keyword": keyword,
        "tips": random.choice(tips),
    }

    return render(request, 'interviews/search.html', content)


def log(request):
    # logFile = open('/code/web_scrapy/logs/scrapy.log', 'r')
    logFile = open('/code/web_scrapy/logs/shell.log', 'r')
    logFile.seek(-10000, os.SEEK_END)
    lines = logFile.readlines()[1:]
    # for row in lines[::-1]:

    content = {
        'lines': lines[::-1]
    }
    return render(request, 'interviews/log.html', content)
