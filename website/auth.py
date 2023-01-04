## Contains all routes dealing with the authentication functionality of the website
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash # hash function has no inverse so db 
                                                                          # doesn't store the password but can detect the correct 
from . import db # The one created in the __init__.py
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"]) # Allow  this route to do both GET & PUT (default is just GET)
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Login Successful!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password. Please try again!", category="error")
        else:
            flash("User does not exist. Please try again!")
    return render_template("login.html", user=current_user) 
    
    

@auth.route("/logout")
@login_required # Decorator makes sure the route is inaccessible unless user is logged in
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash("This email already has an account!", category="error")
        elif len(email) < 4:
            flash("Email must be at least 4 characters.", category="error") # Method that flashes a message to the user
        elif len(firstName) < 2:
            flash("First name must be greater than 1 character.", category="error")
        elif len(password1) < 8:
            flash("Password length must be at least 8 characters.", category="error")
        elif password1 != password2:
            flash("Passwords don't match.", category="error")
        else:
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            
            flash("Account created!", category="success")
            return redirect(url_for("views.home")) # Finding the route "home" mapped to Blueprint "views"
    return render_template("sign_up.html", user = current_user)