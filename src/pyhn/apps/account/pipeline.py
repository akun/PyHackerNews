#!/usr/bin/env python


from social.pipeline.user import create_user as social_create_user

from pyhn.apps.account.models import Profile


def create_user(strategy, details, response, uid, user=None, *args, **kwargs):
    info = social_create_user(
        strategy, details, response, uid, user, *args, **kwargs
    )

    if info['is_new']:
        user = info['user']
        profile = Profile(user_ptr=user)
        profile.username = user.username
        profile.email = user.email
        profile.about = ''
        profile.save()

    return {'is_new': True, 'user': user}
