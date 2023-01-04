## Used to store the main URL endpoints/standard routes for the functional website nav.
from flask import Blueprint, render_template, request, flash, jsonify # Blueprint means file stores a bunch of routes/URLs for organization
from flask_login import login_required, current_user
from . import db
from .models import Note
import json

views = Blueprint("views", __name__)

## Effects: Function will run whenever navigating to root
@views.route("/", methods=["GET", "POST"]) # <- this is a decorator
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")
        
        if len(note) < 1:
            flash("The minimum note length is 2 characters", category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Your note has been added successfully!", category="sucess")
    return render_template("home.html", user=current_user)

@views.route("/delete-note", methods=["POST"])
def delete_note():
    data = json.loads(request.data)
    noteId = data["noteId"]
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
            
