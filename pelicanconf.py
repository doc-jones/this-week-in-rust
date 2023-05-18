#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

# Adjust `TESTING_LOCALLY` if testing search functionality locally.
TESTING_LOCALLY = False
USE_EMAIL_THEME = True if os.environ.get('USE_EMAIL_THEME') == '1' else False

AUTHOR = u'TWiG Contributors'
SITENAME = u"This Week in GraphQL"
SITEURL = 'https://this-week-in-graphql.org' if not TESTING_LOCALLY else 'http://localhost:8000'

SOURCE_URL = 'https://github.com/doc-jones/twig'

if USE_EMAIL_THEME:
    THEME = 'themes/newsletter'
else:
    THEME = 'themes/rusted'

THEME_STATIC_DIR = THEME + '/static'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'atom.xml'
FEED_ALL_RSS = 'rss.xml'
FEED_MAX_ITEMS = 4
CATEGORY_FEED_ATOM = 'categories/{slug}/atom.xml'
CATEGORY_FEED_RSS = 'categories/{slug}/rss.xml'
RSS_FEED_SUMMARY_ONLY = False

DEFAULT_PAGINATION = 10

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

ARCHIVES_SAVE_AS = 'blog/archives/index.html'

CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'

# TODO: REPLACEME
LOGO_32_URL = "https://this-week-in-rust.org/images/logo32.png"
FAVICON_32_URL = "https://www.rust-lang.org/static/images/favicon-32x32.png"
FAVICON_SVG_URL = "https://www.rust-lang.org/static/images/favicon.svg"
SAFARI_PINNED_TAB_URL = "https://www.rust-lang.org/static/images/safari-pinned-tab.svg"
FORM_SUBSCRIBE_URL = "//this-week-in-rust.us11.list-manage.com/subscribe/post?u=fd84c1c757e02889a9b08d289&amp;id=0ed8b72485"
TWITTER_USERNAME = "ThisWeekInRust"
PRIVACY_POLICY_URL = "https://this-week-in-graphql.org/pages/privacy-policy.html"

LANDING_PAGE_ABOUT = {
        "title": "Cataloging the GraphQL community's awesomeness",
        "details": """
A weekly newsletter about GraphQL and the GraphQL community, with bonus content
scattered about.
"""
}

PLUGIN_PATHS = ["plugins"]

# Don't add next/previous buttons search functionality for email.
if USE_EMAIL_THEME:
    PLUGINS = ['webassets']
else:
    PLUGINS = ['webassets', 'neighbors', 'search']
    SEARCH_HTML_SELECTOR = "article"

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'anchorlink': True,
        },
    },
    'output_format': 'html5',
}
