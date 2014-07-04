#!/usr/bin/env python
# coding=utf-8

##############
# Production #
##############
#from pyhn.settings.prod import *  # pylint: disable=W0401,W0614


#ALLOWED_HOSTS = ['.example.com']
#DATABASES = {
#   'default': {
#       'ENGINE': 'django.db.backends.mysql',
#       'NAME': '',
#       'USER': '',
#       'PASSWORD': '',
#   }
#}

# Google Analytics
# eg: PYHN_GOOGLE_ANALYTICS_UA = 'UA-99999999-9'
#PYHN_GOOGLE_ANALYTICS_UA = ''

# Bootstrap Theme
# eg: PYHN_THEME = 'united'
# more: http://bootswatch.com/
# NOTICE: theme name is `Lower Case`
#PYHN_THEME = ''

###############
# Development #
###############
#from pyhn.settings.dev import *  # pylint: disable=W0401,W0614


##########
# Common #
##########
#SECRET_KEY = ''

# GitHub
#SOCIAL_AUTH_GITHUB_KEY = ''
#SOCIAL_AUTH_GITHUB_SECRET = ''

# Sina Weibo
#SOCIAL_AUTH_WEIBO_KEY = ''
#SOCIAL_AUTH_WEIBO_SECRET = ''

# Site Title
# eg: PYHN_TITLE = "akun's News"
#PYHN_TITLE = ''

# Copyright
# eg: PYHN_COPYRIGHT = '&copy; 2014, <a href="https://github.com/akun">akun</a>'
#PYHN_COPYRIGHT = ''

# new register user can submit news
# if need limit new register user for submitting news, we can set as `False`
#
# * True - no limit
# * False - new register user can not submit news(make one user can
#           submit news, you need add `can_submit` permission on this user)
#PYHN_NEW_USER_CAN_SUBMIT = True
