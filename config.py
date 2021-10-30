import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI="postgresql:///animal_shelter"
    SECRET_KEY="keep-me-a-secret-!"

class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


def env_config_classes():
    pass

env_config_classes.ProductionConfig = ProductionConfig
env_config_classes.DevelopmentConfig = DevelopmentConfig
