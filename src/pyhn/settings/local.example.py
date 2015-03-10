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
#       'NAME': 'pyhn_production',
#       'USER': 'pyhn',
#       'PASSWORD': 'your password',
#   }
#}

###############
# Development #
###############
#from pyhn.settings.dev import *  # pylint: disable=W0401,W0614


##########
# Common #
##########
# see also:
# * https://docs.djangoproject.com/en/1.7/ref/settings/#secret-key
# * https://docs.djangoproject.com/en/1.7/topics/signing/
#
# Generate Django Secret Key: http://www.miniwebtool.com/django-secret-key-generator/
# !!!!required!!!!
#SECRET_KEY = ''

# Google Analytics
# eg: PYHN_GOOGLE_ANALYTICS_UA = 'UA-99999999-9'
#PYHN_GOOGLE_ANALYTICS_UA = ''

# Bootstrap Theme
# eg: PYHN_THEME = 'united'
# more: http://bootswatch.com/
# NOTICE: theme name is `Lower Case`
#PYHN_THEME = ''

# GitHub
# How to get URL:
#SOCIAL_AUTH_GITHUB_KEY = ''
#SOCIAL_AUTH_GITHUB_SECRET = ''

# Sina Weibo
# How to get URL:
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

# rss settings
# eg: PYHN_RSS_TITLE = 'Python Hacker News'
#PYHN_RSS_TITLE = ''

# eg: PYHN_RSS_DESCRIPTION = 'Update on Python Hacker News'
#PYHN_RSS_DESCRIPTION = ''

# eg: PYHN_RSS_SIZE = 10
#PYHN_RSS_SIZE = 10
