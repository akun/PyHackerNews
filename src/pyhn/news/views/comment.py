#!/usr/bin/env python


from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from pyhn.news.forms import CommentForm
from pyhn.news.models import Comment, Post
from pyhn.news.views.common import format_post


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
            return HttpResponseRedirect(reverse('news:comment', kwargs={
                'post_id': post_id
            }))

    comments = Comment.objects.filter(parent=None)

    return render(request, 'news/comment.html', {
        'form': form,
        'post': post,
        'show_index': False,
        'comments': comments,
    })
