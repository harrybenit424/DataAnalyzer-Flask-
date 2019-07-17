import tempfile
db_file = tempfile.NamedTemporaryFile()

import os


class Config(object):
    SECRET_KEY = os.urandom(32)


class ProdConfig(Config):
    ENV = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

    CACHE_TYPE = 'simple'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

    CACHE_TYPE = 'null'
    ASSETS_DEBUG = True


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_file.name
    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False
