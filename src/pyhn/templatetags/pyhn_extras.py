#!/usr/bin/env python


import hashlib
import urllib

from django import template
register = template.Library()


@register.filter
def gravatar_url(email, size=16):
    default = 'http://www.gravatar.com/avatar/00000000000000000000000000000000?s=%d' % size

    return 'http://s.gravatar.com/avatar/%s?%s' % (
        hashlib.md5(email.lower()).hexdigest(),
        urllib.urlencode({'d': default, 's': str(size)})
    )
