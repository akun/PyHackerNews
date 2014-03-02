#!/usr/bin/env python


from urlparse import urlparse
import hashlib
import urllib

from django.shortcuts import render

from news.models import Post


def index(request):
    posts = Post.objects.all()
    for post in posts:
        if post.url:
            post.netloc = urlparse(post.url).netloc
            post.gravatar_url = get_gravatar_url(post.user.email)
    return render(request, 'news/index.html', {'posts': posts})


def get_gravatar_url(email):
    size = 16
    default = 'http://www.gravatar.com/avatar/00000000000000000000000000000000?s=%d' % size

    gravatar_url = 'http://s.gravatar.com/avatar/' + hashlib.md5(email.lower()).hexdigest() + '?'
    gravatar_url += urllib.urlencode({'d': default, 's': str(size)})
    return gravatar_url
