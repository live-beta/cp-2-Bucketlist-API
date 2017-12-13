import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
        Contains default configuration utilised in environment setup
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'check_point_rules'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SSL_DISABLE = True

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
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 


class Testing(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or  \
        'sqlite:///' + os.path.join(basedir, 'data-test.db')

# class Production(Config):

#     DEBUG= True

#      SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'data-dev.db')


#      #app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql://bucketlist:bucketlist@localhost/bucketlist')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
     # SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]




class HerokuConfig(ProductionConfig): 

    # Configuration for heroku deployment

    @classmethod
    def init_app(cls  , app): 
        ProductionConfig.init_app(app)
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)
        SSL_DISABLE = bool(os.environ.get('SSL_DISABLE'))

    @classmethod
    def init_app(cls, app): # ...
        # handle proxy server headers
        from werkzeug.contrib.fixers import ProxyFix 
        app.wsgi_app = ProxyFix(app.wsgi_app)
        


configset = {
    "development": Development,
    "Testing": Testing,
    "Production": ProductionConfig,
    "default": Development
}

expiry_time = 40000
