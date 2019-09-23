import os

class Config:
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:ines@localhost/pitch_app'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:ines@localhost/pitch_app'
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://user:ines@localhost/pitch_app'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

