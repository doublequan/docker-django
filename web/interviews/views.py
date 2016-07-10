# coding: utf-8

from django.shortcuts import render, get_object_or_404

from models import Post

# Create your views here.



def index(request):
    boards = ["Facebook", "LinkedIn", "Amazon", "Google", "Uber", "Airbnb"]
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
    content = {
        "total_num": 0,
        "boards": boards,
        "example": example
    }
    return render(request, 'interviews/index.html', content)

def newest(request):
    # items = Post.objects.order_by("create_time")[:10]
    items = Post.objects.all()[:10]

    print type(items), len(items)

    # print items[1]['create_time']

#     items = [{
#         "title": "有近期pure storage onsite的吗，求联系一起讨论，毕业前找到工作的最后希望之一！",
#         "link": "http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=154315&extra=page%3D2%26filter%3Dsortid%26sortid%3D192%26sortid%3D192",
#         "time": "2016-6-28 07:11:25",
#         "source": "1point3acres",
#         "source_link": "http://www.1point3acres.com/bbs/forum-28-1.html",
#         "desc": " 如题，求近期一起有去pure storage onsite的同学吗？求一起讨论学习，加qq552017575。有前辈面过的可以在此帖下留下面筋题目，小弟不甚感激。\
# 渣渣如我一直跪到现在，也面了很多公司了，一直跪，希望早日找到工作，然后把面过的所有面试都发出造福地里，天天都在攒人品，求offer！",
#     }] * 10
    content = {
        "items": items,
        "test": "testMsg",
    }
    return render(request, 'interviews/newest.html', content)


