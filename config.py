import os
class Config:
    WTF_CSRF_SECRET_KEY="qwerty12345"
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SECRET_KEY='qwerty12345'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blogsite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    pass

class DevConfig(Config):
    
    DEBUG=True

config_options={
    'production':ProdConfig,
    'development':DevConfig
}