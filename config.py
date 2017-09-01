import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
        Settging up default environment configurations
    """
    SECRET_KEY = 'check_point_rules'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    """
    Setting up environment variables

    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.db')


class Testing(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.db')


configset = {
    "development": Development,
    "Testing": Testing,
    "default": Development
}

expiry_time = 40000
