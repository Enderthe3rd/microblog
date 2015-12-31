# -*- coding: utf8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True
WHOOSH_BASE = os.path.join(basedir, 'search.db')

# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5

# email server
MAIL_SERVER = 'smtp.mail.yahoo.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = 'michaelkatcher'
MAIL_PASSWORD = 'habitat'

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

# administrator list
ADMINS = ['michaelkatcher@yahoo.com']

# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = 'enderthe3rd_microblog' # enter your MS translator app id here
MS_TRANSLATOR_CLIENT_SECRET = 'j3Krs8rh9g/zW1gEzTGkoGcZIfMx4WTxThZti54DSkI=' # enter your MS translator app secret here