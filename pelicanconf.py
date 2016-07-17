#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colin McLear'
SITENAME = u'Colin McLear'
SITEURL = u'http://colinmclear.net'
# # Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
# CACHE_CONTENT = True
# CACHE_PATH = '/Users/Roambot/Dropbox/Personal/bin/pelican-web/cache'
# AUTORELOAD_IGNORE_CACHE = True
# LOAD_CONTENT_CACHE = True
# CHECK_MODIFIED_METHOD = 'mtime'
# INDEX_SAVE_AS = 'blog_index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

# # Default articles as drafts. To publish add Status: published in header
# DEFAULT_METADATA = {
#     'status': 'draft',
# }

READERS = {'html': None}
DELETE_OUTPUT_DIRECTORY = True
# PATH = 'content'
PATH = 'content'
STATIC_PATHS = ['images', 'pdfs', 'pdfs/phil871/phil871kant', 'themes', 'extra/McLearCV.html', 'extra/McLearCV.pdf', 'extra/CNAME', 'extra/custom.css', 'blog', 'pages/phil101', 'pages/phil232', 'pages/phil871', 'pages/phil971']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/custom.css': {'path': 'static/custom.css'}, 'extra/style.css': {'path': 'static/style.css'}}
# ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}'
CUSTOM_CSS = 'static/custom.css'

DIRECT_TEMPLATES = ('index', 'tags', 'authors', 'archives', 'search')

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# THEME='/Users/Roambot/Dropbox/Personal/Hacks/colinmclear.net-pelican/pelican-themes/pelican-bootstrap3'

THEME='/Users/Roambot/projects/website/pelican-bootstrap3'
BOOTSTRAP_THEME='simplex'
# Change navbar color
BOOTSTRAP_NAVBAR_INVERSE = True
HIDE_SIDEBAR = False
BOOTSTRAP_FLUID = False
CC_LICENSE = "CC-BY-NC-SA"

# Turn on Typogrify
TYPOGRIFY = True

# Plugins
PLUGIN_PATHS = ['/Users/Roambot/bin/pelican-plugins']
PLUGINS = ['pandoc_reader', 'assets', 'tipue_search', 'tag_cloud', 'neighbors']
PANDOC_ARGS = [
    '--filter=/Users/Roambot/bin/pandoc-citeproc',
    '--base-header-level=2',
    # '--standalone',
    # '--smart',
    '--bibliography=/Users/Roambot/Dropbox/Work/Master.bib',
    '--mathjax',
    '--toc',
    '--toc-depth=5',
  ]


# Blogroll
LINKS = (('PHIL 101', 'http://phil101.colinmclear.net'),
        ('PHIL 871', 'http://phil871.colinmclear.net/'),
        ('Blackboard', 'https://my.unl.edu/webapps/portal/frameset.jsp'),
        ('UNL Philosophy', 'http://www.unl.edu/philosophy/'))

# Social widget
SOCIAL = (
          ('philpapers', 'http://philpapers.org/profile/740', 'file-text'),
          ('github', 'https://github.com/mclearc'),
          ('twitter', 'http://twitter.com/mclearc'),
          ('academia.edu', 'https://un-lincoln.academia.edu/ColinMcLear', 'book'),
          ('facebook', 'https://www.facebook.com/?_rdr=p'),
          )

DEFAULT_PAGINATION = 10

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





