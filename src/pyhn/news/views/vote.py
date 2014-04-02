#!/usr/bin/env python


import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from pyhn.news.models import Post


@require_POST
def vote(request, post_id):
    if not request.user.is_authenticated():
        ret = {'code': 100, 'msg': 'need login', 'result': {'id': post_id}}
    else:
        post = get_object_or_404(Post, id=post_id)
        if post.vote_set.filter(user=request.user).count():
            ret = {'code': 101, 'msg': 'has voted', 'result': {'id': post_id}}
        else:
            post.vote(request.user)
            ret = {'code': 0, 'msg': 'success', 'result': {'id': post_id}}
    return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type='application/json')
