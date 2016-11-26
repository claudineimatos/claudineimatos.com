#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Claudinei Matos'
SITENAME = u'claudineimatos.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/claudineimatos7'),
          ('linkedin', 'http://www.linkedin.com/in/claudineimatos'),
          ('github', 'http://github.com/claudineimatos'),
          ('google', 'http://plus.google.com/+ClaudineiMatos'))

DISPLAY_TAGS_INLINE = True

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]

TAG_CLOUD_STEPS = 4
TAG_CLOUD_BADGE = True	
TAG_CLOUD_SORTING = 'size'	

PYGMENTS_STYLE = 'emacs'

ABOUT_ME = 'Hi, my name is Claudinei and I\'m an I.T. passionate guy'
SHOW_ARTICLE_AUTHOR = False


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = os.path.join(os.environ.get('HOME'), "workspace/claudineimatos.com/pelican-themes/bootstrap2/")
