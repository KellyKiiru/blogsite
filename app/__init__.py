from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

bootstrap=Bootstrap()
db = SQLAlchemy()
csrf = CSRFProtect()

def create_app(config_name):
    app = Flask(__name__)
    
    ''''
    app configurations
    '''
    app.config.from_object(config_options[config_name])
    
    '''
    register blueprints
    '''
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #initialize bootstrap
    bootstrap.init_app(app)
    
    #initialize database
    db.init_app(app)
    
    csrf.init_app(app)   
    
    
    return app