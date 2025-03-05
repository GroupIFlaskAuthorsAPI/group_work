# app/__init__.py
from flask import Flask
from app.models import db
from app.controllers.blueprint import author_bp, book_bp, company_bp
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    # Database URI and configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Initialize Flask-Migrate
    migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(author_bp)
    app.register_blueprint(book_bp)
    app.register_blueprint(company_bp)

    return app



