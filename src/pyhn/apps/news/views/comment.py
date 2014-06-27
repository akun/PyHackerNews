#!/usr/bin/env python


import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST, require_http_methods

from pyhn.apps.news.forms import CommentForm, ReplyForm
from pyhn.apps.news.models import Comment, Post
from pyhn.apps.news.views.common import format_post


@require_http_methods(['GET', 'POST'])
def comment_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    reply_form = ReplyForm()

    if request.method == 'GET':
        format_post(request, post)
        comment_form = CommentForm()
    else:
        if not request.user.is_authenticated():
            path = request.get_full_path()
            return redirect_to_login(path)

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save(request.user, post)
            return HttpResponseRedirect(reverse('news:comment', kwargs={
                'post_id': post_id
            }))

    comments = Comment.objects.filter(post=post, parent=None)

    return render(request, 'news/comment.html', {
        'comment_form': comment_form,
        'reply_form': reply_form,
        'post': post,
        'show_index': False,
        'comments': comments,
    })


@require_POST
def reply_comment(request, comment_id):

    comment = get_object_or_404(Comment, id=comment_id)
    ret = {'code': 0, 'msg': 'success', 'result': {'id': comment.id}}
    if request.user.is_authenticated():
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save(request.user, comment)
        else:
            ret['code'] = 101
            ret['msg'] = 'form is invalid'
            ret['result']['errors'] = dict(form.errors)
    else:
        ret['code'] = 100
        ret['msg'] = 'need login'

    return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type='application/json')


@login_required
@require_POST
def remove(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    ret = {'code': 0, 'msg': 'success', 'result': {'id': comment_id}}
    return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type='application/json')
