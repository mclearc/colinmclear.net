#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colin McLear'
SITENAME = u'Colin McLear'
# SITEURL = 'http://colinmclear.net'
SITEURL = ''
LOAD_CONTENT_CACHE = False
GOOGLE_ANALYTICS = 'UA-30497236-1'
# INDEX_SAVE_AS = 'blog_index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

# # Default articles as drafts. To publish add Status: published in header
# DEFAULT_METADATA = {
#     'status': 'draft',
# }

DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'
STATIC_PATHS = ['images', 'pdfs', 'themes', 'extra/CNAME', 'extra/custom.css', 'blog', 'pages/phil101', 'pages/phil232', 'pages/phil871', 'pages/phil971']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/custom.css': {'path': 'static/custom.css'}}
# ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}'
CUSTOM_CSS = 'static/custom.css'

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# THEME='/Users/Roambot/Dropbox/Personal/Hacks/colinmclear.net-pelican/pelican-themes/pelican-bootstrap3'

THEME='/Users/Roambot/Dropbox/Personal/Hacks/colinmclear.net-pelican/pelican-bootstrap3'
BOOTSTRAP_THEME='simplex'
# BOOTSTRAP_THEME='cosmo'
# Change navbar color
BOOTSTRAP_NAVBAR_INVERSE = True
HIDE_SIDEBAR = False
BOOTSTRAP_FLUID = False
CC_LICENSE = "CC-BY-NC-SA"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
PYGMENTS_STYLE = 'vim'
FAVICON = 'images/favicon.ico'


# Tags

TAG_CLOUD = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'

# Blogroll
LINKS = (('PHIL 232', 'http://colinmclear.net/phil-232-early-modern-philosophy/'),
        ('PHIL 971', 'http://colinmclear.net/phil-971-introspection-self-knowledge/'),
        ('Blackboard', 'https://my.unl.edu/webapps/portal/frameset.jsp'),
        ('UNL Philosophy', 'http://www.unl.edu/philosophy/'))

# Social widget
SOCIAL = (('academia.edu', 'https://un-lincoln.academia.edu/ColinMcLear',
    'book'),
          ('twitter', 'http://twitter.com/mclearc'),
          ('github', 'https://github.com/mclearc'),
          ('facebook', 'https://www.facebook.com/?_rdr=p'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True



# Plugins
PLUGIN_PATHS = ['/Users/Roambot/Dropbox/Personal/Hacks/pelican-plugins']
PLUGINS = ['pandoc_reader', 'pelican-md-yaml', 'tipue_search', 'tag_cloud', 'neighbors']

PANDOC_ARGS = [
  '--mathjax',
  '--smart',
  '--toc',
  '--toc-depth=1',
]

PANDOC_EXTENSIONS = [
  '-hard_line_breaks',
  '+citations'
]

# Turn on Typogrify
TYPOGRIFY = True



