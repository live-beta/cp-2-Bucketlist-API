import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
        Contains default configuration utilised in environment setup
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'check_point_rules'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    """
    Setup wide development environment

    """
    DEBUG = True
    # configuration for postgres development
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql://bucketlist:bucketlist@localhost/bucketlist')
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.db')


class Testing(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or  \
        'sqlite:///' + os.path.join(basedir, 'data-test.db')

# class Production(Config):

#     DEBUG= True

#      SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'data-dev.db')


#      #app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql://bucketlist:bucketlist@localhost/bucketlist')




configset = {
    "development": Development,
    "Testing": Testing,
    "default": Development
}

expiry_time = 40000
