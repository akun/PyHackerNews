PyHackerNews
============

.. image:: https://travis-ci.org/akun/PyHackerNews.svg?branch=master
   :target: https://travis-ci.org/akun/PyHackerNews
   :alt: Build Status

.. image:: https://landscape.io/github/akun/PyHackerNews/master/landscape.png
   :target: https://landscape.io/github/akun/PyHackerNews/master
   :alt: Code Health

.. image:: https://coveralls.io/repos/akun/PyHackerNews/badge.png?branch=master
   :target: https://coveralls.io/r/akun/PyHackerNews?branch=master
   :alt: Coverage Status

Hacker News written in Python

Install
-------

Features
--------

* [o] show news list

  + [o] show news list, order by score, with paginator
  + [o] show news list, order by post time
  + [o] show news info: title, domain, point, reporter, since when, comment count
  + [o] vote for news. **login required**
  + [ ] remove news you post. **login required**

* [o] submit news

  + [o] submit news with title and URL/Content. **login required**

    - [o] URL for news
    - [o] leave URL blank to submit a question for discussion

* [o] comment

  + [o] show comment list order by score, with indent
  + [o] show comment info: comment words, point, who comment, since when
  + [ ] copy comment link
  + [o] add comment abount news. **login required**
  + [o] reply the comment. **login required**
  + [ ] vote for comment. **login required**
  + [ ] remove the comment you add or reply. **login required**

* [o] Auth/Account

  + [o] login with social site's oauth
  + [o] show social site's oauth list
  + [ ] edit personal account info: nickname for show(empty will show social site's username), email(for gravatar). **login required**
  + [ ] show someone account info: username for show, score, about

* [o] Hacker News Score System(auto)

  + [o] news score
  + [ ] comment score
  + [ ] user score
  + [ ] calculate score in background

License
-------
