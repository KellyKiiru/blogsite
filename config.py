import os
from distutils.debug import DEBUG
from doctest import FAIL_FAST
import os
from pickle import FALSE

class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://twacmvcbadjiqd:7c27ecbac0490fb6e9fbb9c86f74a2c627d1dad838cdf5a1f19492af71896558@ec2-3-231-82-226.compute-1.amazonaws.com:5432/df0rlua77c4bb1'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=465
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    

class ProdConfig(Config):
    
    DEBUG=False

class DevConfig(Config):
    
    DEBUG=True

config_options={
    'production':ProdConfig,
    'development':DevConfig
}