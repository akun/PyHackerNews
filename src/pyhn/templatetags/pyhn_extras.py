#!/usr/bin/env python


import hashlib
import urllib

from django import template
register = template.Library()


@register.filter
def gravatar_url(email):
    size = 16
    default = 'http://www.gravatar.com/avatar/00000000000000000000000000000000?s=%d' % size

    gravatar_url = 'http://s.gravatar.com/avatar/' + hashlib.md5(email.lower()).hexdigest() + '?'
    gravatar_url += urllib.urlencode({'d': default, 's': str(size)})
    return gravatar_url
