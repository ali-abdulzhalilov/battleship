import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'no_key_set'

class TestConfig(Config):
    TESTING = True
    SECRET_KEY = 'test_key'

app_config = {
    'development': TestConfig,
    'testing': TestConfig,
    'production': Config
}
