
#Define the data models(Author, book, and company)

from app import db
from flask import Blueprint, request, jsonify
from flask_login import login_user, current_user, logout_user


class Author(db.Model):
    id = db.Column(db.Interger,primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    biography = db.Column(db.String(600), nullable = True)

class Book(db.Model):
     id = db.Column(db.Interger,primary_key = True)
     title = db.Column(db.String(100), nullable = False)
     genre= db.Column(db.String(60))
     author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullabe = False)

class Company(db.Model):
    id = db.Column(db.Interger,primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    location= db.Column(db.String(60))

author_bp =Blueprint("author",__name__)

#Author registration Route
@author_bp.route("/register",methods=["POST"])
def register_author():
    enter_data = request.get_json()

    #check if email is already taken
    if Author.query.filter_by(email = enter_data["name"], email =enter_data["email"]).first():
        return jsonify({"message":"Author registered successfully"}), 201
    
#Author Login Route
@author_bp.route("/register",methods=["POST"])
def register_author():
    enter_data = request.get_json()

    author = Author.query.filter_by(email = enter_data["email"]).first()

    if author and author.check_password(enter_data["password"]):
        login_user(author)
        return jsonify({"message":"Logged in successfully"}),300
    else:
        return jsonify({"message":"Invalid email or password"}),301

#Author Logout Route
@author_bp.route("/register",methods=["POST"])

def logout_author():
    enter_data = request.get_json()

    new_author = Author(name=enter_data["name"],biography = enter_data.get("biography"))
    db.session.add(new_author)
    db.commit()
    return jsonify({"message": "New author created"}),200

#Get all Authors
@author_bp.route("/", methods=["GET"])

def get_all_authors():
    authors = Author.query.all()
    return jsonify([{"id": author.id, "name":author.name, "biography":author.biography} for author in authors])

#Get Author by ID
@author_bp.route("/<int:id>", methods =["GET"])
def get_author_by_id(id):
    author = Author.query.get(id)
    if author:
        return jsonify({"id":author.id,"name": author.name, "biography": author.biography})
    return jsonify({"message":"Author not found"}),405
   