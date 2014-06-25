#!/usr/bin/env python


import json

from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST, require_http_methods

from pyhn.news.forms import PostForm
from pyhn.news.models import Post


@login_required
@permission_required('news.can_submit')
@require_http_methods(['GET', 'POST'])
def submit(request):

    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'news/submit.html', {'form': form})


@login_required
@require_POST
def remove(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    ret = {'code': 0, 'msg': 'success', 'result': {'id': post_id}}
    return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type='application/json')
