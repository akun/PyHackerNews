#!/usr/bin/env python


from pyhn.settings.common import *  # pylint: disable=W0401,W0614


SECRET_KEY = 'just4test'
INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS.append('django_nose')
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
