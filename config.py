import os
class Config:
    WTF_CSRF_SECRET_KEY=os.environ.get("WTF_CSRF_SECRET_KEY")
    SECRET_KEY=os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')

class DevConfig(Config):
    
    DEBUG=True

config_options={
    'production':ProdConfig,
    'development':DevConfig
}