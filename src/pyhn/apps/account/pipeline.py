#!/usr/bin/env python


from django.conf import settings
from django.contrib.auth.models import Permission

from social.pipeline.user import create_user as social_create_user

from pyhn.apps.account.models import Profile


def create_user(strategy, details, response, uid, user=None, *args, **kwargs):
    info = social_create_user(
        strategy, details, response, uid, user, *args, **kwargs
    )

    if info['is_new']:
        user = info['user']
        if settings.PYHN_NEW_USER_CAN_SUBMIT:
            permission = Permission.objects.get(codename='can_submit')
            user.user_permissions.add(permission)

        profile = Profile(user_ptr=user)
        profile.username = user.username
        profile.email = user.email
        profile.about = ''
        profile.save()

    return {'is_new': True, 'user': user}
