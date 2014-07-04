#!/usr/bin/env python


from django.conf import settings


def pyhn_info(request):
    return {
        'PYHN_TITLE': settings.PYHN_TITLE,
        'PYHN_COPYRIGHT': settings.PYHN_COPYRIGHT,
        'PYHN_NEW_USER_CAN_SUBMIT': settings.PYHN_NEW_USER_CAN_SUBMIT,
        'PYHN_GOOGLE_ANALYTICS_UA': settings.PYHN_GOOGLE_ANALYTICS_UA,
    }
