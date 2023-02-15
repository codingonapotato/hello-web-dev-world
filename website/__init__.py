## Makes the website folder a Python package that can be imported to run contents automatically
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

## Effects: initializes a Flask object using the name of the currently running module
def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config["SECRET_KEY"] = "Zipper Man" # Encryption key to protect website session cookies & data
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/") # url prefix = how to access blueprint in url
    app.register_blueprint(auth, url_prefix="/") # / indicates no prefix (sorta)
    
    from .models import User, Note # Ensures all necessary classes in this file are loaded
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # Searches for primary key by default
    
    return app

def create_database(app):
    if not path.exists(f"website/{DB_NAME}"): #checking to see if the database already exists in the website package
        with app.app_context(): # specifies to SQLAlchemy which app the database is for
            db.create_all()
        print("New database created!")