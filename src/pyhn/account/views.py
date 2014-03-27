#!/usr/bin/env python


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_GET


from pyhn.account.forms import AccountForm


@login_required
def index(request):

    form = AccountForm()
    return render(request, 'account/index.html', {'form': form})

@require_GET
def login(request):

    return render(request, 'account/login.html', {})
