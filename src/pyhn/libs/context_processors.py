#!/usr/bin/env python


from django.conf import settings


def pyhn_info(request):
    return {
        'PYHN_TITLE': settings.PYHN_TITLE,
        'PYHN_COPYRIGHT': settings.PYHN_COPYRIGHT,
    }