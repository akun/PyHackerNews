#!/usr/bin/env python


import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from pyhn.apps.news.models import Comment, Post


@require_POST
def post_vote(request, post_id):
    return do_vote(request, post_id, Post)


@require_POST
def comment_vote(request, comment_id):
    return do_vote(request, comment_id, Comment)


def do_vote(request, object_id, object_class):
    set_dict = {
            Post: 'vote_set',
            Comment: 'commentvote_set',
    }
    if not request.user.is_authenticated():
        ret = {'code': 100, 'msg': 'need login', 'result': {'id': object_id}}
    else:
        object_instance = get_object_or_404(object_class, id=object_id)
        if getattr(object_instance, set_dict[object_class]).filter(
            user=request.user
        ).count():
            ret = {
                'code': 101, 'msg': 'has voted', 'result': {'id': object_id}
            }
        else:
            object_instance.vote(request.user)
            ret = {'code': 0, 'msg': 'success', 'result': {'id': object_id}}
    return HttpResponse(
        json.dumps(ret, ensure_ascii=False), content_type='application/json'
    )
