#!/usr/bin/env python


import json

from urlparse import urlparse
import hashlib
import urllib

from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from news.forms import CommentForm
from news.models import Comment, Post


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


@require_POST
def vote(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.vote_set.filter(user=request.user).count():
        ret = {'code': 100, 'msg': 'has voted', 'result': {'id': post_id}}
    else:
        post.vote(request.user)
        ret = {'code': 0, 'msg': 'success', 'result': {'id': post_id}}
    return HttpResponse(json.dumps(ret, ensure_ascii=False))


@require_http_methods(['GET', 'POST'])
def comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'GET':
        format_post(request, post)
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(request.user, post)

    comments = Comment.objects.filter(parent=None)
    return render(request, 'news/comment.html', {
        'post': post,
        'show_index': False,
        'comments': comments,
    })


def format_post(request, post):
    post.voted = False
    is_authenticated = request.user.is_authenticated()
    if is_authenticated and post.vote_set.filter(user=request.user).count():
        post.voted = True
    if post.url:
        post.netloc = urlparse(post.url).netloc
        post.gravatar_url = get_gravatar_url(post.user.email)


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
