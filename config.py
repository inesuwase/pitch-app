import os

class Config:
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:ines@localhost/pitch_app'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY =('SECRET_KEY')
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'uwaseines7@gmail.com'
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:ines@localhost/pitch_app'
    pass

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:ines@localhost/pitch_test'

    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://user:ines@localhost/pitch_app'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}
