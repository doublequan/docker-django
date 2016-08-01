# coding: utf-8
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from models import Post
import chardet
import random
import re

from django.utils.http import urlunquote, urlquote

# Create your views here.

tips = ("搜索关键词，例如：Google",
        "空格隔开关键词,例如:Amazon onsite",
        )

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

    # boards = [("Facebook", example),
    #           ("LinkedIn", example),
    #           ("Amazon", example),
    #           ("Google", example),
    #           ("Uber", example),
    #           ("Airbnb", example)]

    content = {
        "total_num": len(all_posts),
        "content_newest": content_newest,
        "boards": boards,
        "tips": random.choice(tips)
    }
    return render(request, 'interviews/index.html', content)


def search(request):

    if request.GET.get('pn'):
        current_page_id = request.GET.get('pn')
    else:
        current_page_id = 1
    current_page_id = int(current_page_id)


    # items = Post.objects.order_by("create_time")[:10]
    result_num_each_page = 10

    # print chardet.detect(request.GET.get('wd'))
    keyword = ""
    if request.GET.get('wd') and request.GET.get('wd').encode('utf-8') != "":
        keyword = request.GET.get('wd').encode('utf-8')
        # wds = keyword.split(" ")
        # wds = filter(None, wds)
        # print wds
        # Sorting Algorithm

        # End of Sorting

        args = (Q(title__icontains=keyword) |
                Q(description__icontains=keyword) |
                Q(tag__icontains=keyword),)
        all_posts = Post.objects.filter(*args)
    else:
        all_posts = Post.objects.all()
    # print chardet.detect(request.GET.get('wd').encode('utf-8'))

    result_num = len(all_posts)
    total_page_num = result_num / result_num_each_page + 1

    if current_page_id > total_page_num or current_page_id <= 0:
        raise Http404("No Such Page!")

    prev_page = False
    next_page = False
    if current_page_id > 1:
        url = "/search?pn=%d&wd=%s" % (current_page_id - 1, urlquote(keyword))
        prev_page = url
    if current_page_id < total_page_num:
        url = "/search?pn=%d&wd=%s" % (current_page_id + 1, urlquote(keyword))
        next_page = url

    pages = []
    if total_page_num <= 10:
        for i in range(1, total_page_num + 1):
            url = "/search?pn=%d&wd=%s" % (i, urlquote(keyword))
            pages += [(i, url)]
            # print url
    else:
        start_page = max(1, current_page_id - 4)
        end_page = min(total_page_num, current_page_id + 5)
        if end_page - start_page + 1 < 10:
            if end_page == total_page_num:
                start_page = end_page - 9

        for i in range(start_page, start_page + 10):
            url = "/search?pn=%d&wd=%s" % (i, urlquote(keyword))
            pages += [(i, url)]

    start_id = (current_page_id - 1) * result_num_each_page
    end_id = start_id + result_num_each_page
    item_list = all_posts.order_by('-create_time')[start_id : end_id]
    items = []
    for item in item_list:
        tags = [n for n in item.tag.split(' ') if n.strip()]
        items += [[item, tags]]

    # print items
    content = {
        "items": items,
        "result_num": result_num,
        "pages": pages,
        "page_num": total_page_num,
        "current_page_num": current_page_id,
        "prev_page": prev_page,
        "next_page": next_page,
        "search_keyword": keyword,
        "tips": random.choice(tips),
    }

    return render(request, 'interviews/search.html', content)


