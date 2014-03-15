#!/usr/bin/env python


import json

from urlparse import urlparse
import hashlib
import urllib

from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_POST

from news.models import Post


@require_GET
def index(request, cur_page_num=1):
    cur_page_num = int(cur_page_num)
    num_per_page = 30
    posts = Post.objects.all()
    paged_object = get_paged_object(posts, cur_page_num, num_per_page)
    for post in paged_object.object_list:
        if post.vote_set.filter(user=request.user).count():
            post.voted = True
        else:
            post.voted = False

        if post.url:
            post.netloc = urlparse(post.url).netloc
            post.gravatar_url = get_gravatar_url(post.user.email)

    return render(request, 'news/index.html', {
        'paged_object': paged_object,
        'start_index': num_per_page * (cur_page_num - 1),
    })

@require_POST
def vote(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.vote_set.filter(user=request.user).count():
        ret = {'code': 100, 'msg': 'has voted', 'result': {'id': post_id}}
    else:
        post.vote(request.user)
        ret = {'code': 0, 'msg': 'success', 'result': {'id': post_id}}
    return HttpResponse(json.dumps(ret, ensure_ascii=False))


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
