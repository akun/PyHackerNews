#!/usr/bin/env python


from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from pyhn.news.forms import PostForm


@login_required
@require_http_methods(['GET', 'POST'])
def submit(request):

    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'news/submit.html', {'form': form})
