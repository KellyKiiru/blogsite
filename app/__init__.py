from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_moment import Moment

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
##moment = Moment()

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
    #moment.init_app(app)
    
    #initialize logins
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"
    login_manager.login_message_category = "warning"
    
    return app