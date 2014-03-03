#!/usr/bin/env python


from urlparse import urlparse
import hashlib
import urllib

from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.shortcuts import render

from news.models import Post


def index(request, cur_page_num=1):
    cur_page_num = int(cur_page_num)
    num_per_page = 30
    posts = Post.objects.all()
    paged_object = get_paged_object(posts, cur_page_num, num_per_page)
    for post in paged_object.object_list:
        if post.url:
            post.netloc = urlparse(post.url).netloc
            post.gravatar_url = get_gravatar_url(post.user.email)
    return render(request, 'news/index.html', {
        'paged_object': paged_object,
        'start_index': num_per_page * (cur_page_num - 1),
    })


def get_gravatar_url(email):
    size = 16
    default = 'http://www.gravatar.com/avatar/00000000000000000000000000000000?s=%d' % size

    gravatar_url = 'http://s.gravatar.com/avatar/' + hashlib.md5(email.lower()).hexdigest() + '?'
    gravatar_url += urllib.urlencode({'d': default, 's': str(size)})
    return gravatar_url


def get_paged_object(source_items, cur_page_num, num_per_page):
    paginator = Paginator(source_items, num_per_page)
    try:
        page = int(cur_page_num)
    except ValueError:
        page = 1

    try:
        paged_object = paginator.page(page)
    except (EmptyPage, InvalidPage):
        paged_object = paginator.page(paginator.num_pages)

    return paged_object
