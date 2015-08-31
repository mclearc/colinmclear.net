#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colin McLear'
SITENAME = u'Colin McLear'
SITEURL = u'http://colinmclear.net'
# SITEURL = ''
LOAD_CONTENT_CACHE = False
GOOGLE_ANALYTICS = 'UA-30497236-1'
# INDEX_SAVE_AS = 'blog_index.html'
DISQUS_SITENAME = 'colinmclear'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

# # Default articles as drafts. To publish add Status: published in header
# DEFAULT_METADATA = {
#     'status': 'draft',
# }



READERS = {'html': None} 
DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'
STATIC_PATHS = ['images', 'pdfs', 'pdfs/phil871/phil871kant', 'themes', 'extra/McLearCV.html', 'extra/CNAME', 'extra/custom.css', 'blog', 'pages/phil101', 'pages/phil232', 'pages/phil871', 'pages/phil971']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/custom.css': {'path': 'static/custom.css'}}
# ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}'
CUSTOM_CSS = 'static/custom.css'

DIRECT_TEMPLATES = ('index', 'tags', 'authors', 'archives', 'search')

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# THEME='/Users/Roambot/Dropbox/Personal/Hacks/colinmclear.net-pelican/pelican-themes/pelican-bootstrap3'

THEME='/Users/Roambot/Dropbox/Personal/Hacks/colinmclear.net-pelican/pelican-bootstrap3'
BOOTSTRAP_THEME='simplex'
# Change navbar color
BOOTSTRAP_NAVBAR_INVERSE = True
HIDE_SIDEBAR = False
BOOTSTRAP_FLUID = False
CC_LICENSE = "CC-BY-NC-SA"

# Turn on Typogrify
TYPOGRIFY = True

# Plugins
PLUGIN_PATHS = ['/Users/Roambot/Dropbox/Personal/Hacks/pelican-plugins']
PLUGINS = ['pandoc_reader', 'assets', 'tipue_search', 'tag_cloud', 'neighbors'] 

PANDOC_ARGS = [
  '--smart',
  '--filter=pandoc-citeproc',
  '--base-header-level=2'
  ]

PANDOC_EXTENSIONS = [
  '+citations',
  '+yaml_metadata_block'
]

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
DISPLAY_TAGS_ON_SIDEBAR= True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'





