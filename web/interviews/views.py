# coding: utf-8
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from models import Post
import chardet
# Create your views here.



def index(request):
    example = {
        "2016-Jun-07 新鲜OA题目 截",
        "国内30岁，想去美国硅谷工作或者申请CS PHD",
        "Google 6/2 Onsite [已跪]",
        "公司training不好，求助大家",
        "Google 6/14 二轮店面",
        "被一家ICC给拒了",
        "有人收到 Vancouver Interview Event 的吗",
        "M家onsite吐槽下",
        "FB phone要求bug free？",
    }

    boards = [("Facebook", example),
              ("LinkedIn", example),
              ("Amazon", example),
              ("Google", example),
              ("Uber", example),
              ("Airbnb", example)]

    content = {
        "total_num": 0,
        "boards": boards,
        "example": example
    }
    return render(request, 'interviews/index.html', content)


def search(request, current_page_num):
    # items = Post.objects.order_by("create_time")[:10]
    result_num_each_page = 10;

    # print chardet.detect(request.GET.get('wd'))
    # print request.GET.get('wd').encode('utf-8')
    # print chardet.detect(request.GET.get('wd').encode('utf-8'))

    all_posts = Post.objects.all()

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
    }

    return render(request, 'interviews/search.html', content)


