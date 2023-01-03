## Used to store the main URL endpoints/standard routes for the functional website nav.
from flask import Blueprint, render_template # Blueprint means file stores a bunch of routes/URLs for organization

views = Blueprint("views", __name__)

## Effects: Function will run whenever navigating to root
@views.route("/") # <- this is a decorator
def home():
    return render_template("home.html") # Renders the html in the path
