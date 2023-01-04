## Used to store database models
from . import db # Import the db object from this current package
from flask_login import UserMixin # Useful parent class for our custom user class
from sqlalchemy.sql import func #func retrieves current date and time

class Note(db.Model):    
    id = db.Column(db.Integer, primary_key= True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id")) # Sets a relationship between the Note and User classes. 
                                                              # Undercase cause SQL would have user as undercase
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key= True) # db.Column takes a primary key as a unique identifier
    email = db.Column(db.String(150), unique = True) # db.String needs a max size, unique means no dups
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    notes = db.relationship("Note") # Sets a relationship where the note id created by the user is stored in this notes field