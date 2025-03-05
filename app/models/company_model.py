from app.extensions import db,migrate
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Company(db.Model):
    
    __tablename__="company"
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(20),nullable = False)
    last_name = db.Column(db.String(50),nullable =False)
    email = db.Column(db.String(50),nullable = False)
    password = db.Column (db.Text(),nullable= False)
    image =db.Column(db.String(50),nullable =False )
    Age =db.Column(db.Integer,nullable= False)
    nationality =db.Column(db.Integer,nullable= False)
    bio =db.Column(db.String (50), nullable= False)
    created_at= db.Column(db.DateTime, default = datetime.now())
    updated_at=db.Column(db.DateTime, onupdate = datetime.now())
    contact=db.Column(db.String (50),nullable =False,unique= True)