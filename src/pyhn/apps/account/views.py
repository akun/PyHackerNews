#!/usr/bin/env python


from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET

from pyhn.apps.account.forms import AccountForm
from pyhn.apps.account.models import Profile


@login_required
def index(request):

    if request.method == 'GET':
        try:
            about = request.user.profile.about
        except Profile.DoesNotExist:
            about = ''

        form = AccountForm(initial={
            'username': request.user.username,
            'email': request.user.email,
            'about': about,
        })
    else:
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('account:index'))
    return render(request, 'account/index.html', {'form': form})


@require_GET
def login(request):

    return render(request, 'account/login.html', {})


@require_GET
def user_profile(request, user_id):
    profile = get_object_or_404(Profile, id=user_id)
    return render(request, 'account/profile.html', {'profile': profile})
