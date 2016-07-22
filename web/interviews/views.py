# coding: utf-8
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from models import Post
import chardet
import random
# Create your views here.



def index(request):
    all_posts = Post.objects.all()

    content_newest_models = all_posts.order_by("-create_time")[:10]
    content_newest = [(models, models.create_time.strftime("%b %d"))
                      for models in content_newest_models]


    board_names = ("Facebook",
                   "LinkedIn",
                   "Amazon",
                   "Google",
                   "Uber",
                   "Microsoft",
                   "Airbnb",
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

    tips = ("搜索关键词，例如：Google",
            "随机Tips1",
            "随机Tips2",)


    content = {
        "total_num": len(all_posts),
        "content_newest": content_newest,
        "boards": boards,
        "tips": random.choice(tips)
    }
    return render(request, 'interviews/index.html', content)


def search(request, current_page_num):
    # items = Post.objects.order_by("create_time")[:10]
    result_num_each_page = 10

    # print chardet.detect(request.GET.get('wd'))
    keyword = ""
    if request.GET.get('wd') and request.GET.get('wd').encode('utf-8') != "":
        keyword = request.GET.get('wd').encode('utf-8')
        print keyword

        args = (Q(title__icontains=keyword) |
                Q(description__icontains=keyword) |
                Q(tag__icontains=keyword),)
        all_posts = Post.objects.filter(*args)
    else:
        all_posts = Post.objects.all()
    # print chardet.detect(request.GET.get('wd').encode('utf-8'))

    result_num = len(all_posts)
    page_num = result_num / result_num_each_page + 1

    current_page_num = int(current_page_num)

    if current_page_num > page_num or current_page_num <= 0:
        raise Http404("No Such Page!")

    if page_num <= 10:
        pages = range(1, page_num + 1)
    else:
        start_page = max(1, current_page_num - 4)
        pages = range(start_page, start_page + 10)

    start_id = (current_page_num - 1) * result_num_each_page
    end_id = start_id + result_num_each_page
    item_list = all_posts.order_by('-create_time')[start_id : end_id]
    items = []
    for item in item_list:
        tags = [n for n in item.tag.split(' ') if n.strip()]
        items += [[item, tags]]

    print items
    content = {
        "items": items,
        "result_num": result_num,
        "pages": pages,
        "page_num": page_num,
        "current_page_num": current_page_num,
        "prev_page": current_page_num - 1,
        "next_page": current_page_num + 1,
        "search_keyword": keyword,
    }

    return render(request, 'interviews/search.html', content)


