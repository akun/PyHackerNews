#!/usr/bin/env python


from django.shortcuts import render
from django.views.decorators.http import require_GET

from pyhn.news.models import Post
from pyhn.news.views.common import format_post, get_paged_object


@require_GET
def index(request, cur_page_num=1, order_by=None):
    cur_page_num = int(cur_page_num)
    num_per_page = 30

    posts = Post.objects.all()
    if order_by:
        posts = posts.order_by(order_by)
    paged_object = get_paged_object(posts, cur_page_num, num_per_page)
    for post in paged_object.object_list:
        format_post(request, post)

    return render(request, 'news/list.html', {
        'paged_object': paged_object,
        'start_index': num_per_page * (cur_page_num - 1),
        'show_index': True,
    })
