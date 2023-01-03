## Makes the website folder a Python package that can be imported to run contents automatically
from flask import Flask

## Effects: initializes a Flask object using the name of the currently running module
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Zipper Man" # Encryption key to protect website session cookies & data
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/") # url prefix = how to access blueprint in url
    app.register_blueprint(auth, url_prefix="/") # / indicates no prefix (sorta)
    
    return app