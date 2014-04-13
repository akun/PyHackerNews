#!/usr/bin/env python


from urlparse import urlparse

from django.core.paginator import EmptyPage, InvalidPage, Paginator


def format_post(request, post):
    post.voted = False
    is_authenticated = request.user.is_authenticated()
    if is_authenticated and post.vote_set.filter(user=request.user).count():
        post.voted = True
    if post.url:
        post.netloc = urlparse(post.url).netloc


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
