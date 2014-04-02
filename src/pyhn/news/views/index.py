#!/usr/bin/env python


from django.shortcuts import render
from django.views.decorators.http import require_GET

from pyhn.news.models import Post
from pyhn.news.views.common import format_post, get_gravatar_url, get_paged_object


@require_GET
def index(request, cur_page_num=1):
    cur_page_num = int(cur_page_num)
    num_per_page = 30

    posts = Post.objects.all()
    paged_object = get_paged_object(posts, cur_page_num, num_per_page)
    for post in paged_object.object_list:
        format_post(request, post)

    gravatar_url = None
    if request.user.is_authenticated():
        email = request.user.email
        gravatar_url = get_gravatar_url(email)

    return render(request, 'news/list.html', {
        'paged_object': paged_object,
        'start_index': num_per_page * (cur_page_num - 1),
        'gravatar_url': gravatar_url,
        'show_index': True,
    })
