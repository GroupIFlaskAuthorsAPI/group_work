from flask import Flask  # ✅ Import Flask
from app.models import db
from app.controllers.blueprint import author_bp, book_bp, company_bp  # Importing blueprints
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    # Database URI and configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True  # Enable debug mode

    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints with their respective prefixes
    app.register_blueprint(author_bp, url_prefix='/authors')  # Add URL prefix for authors
    app.register_blueprint(book_bp, url_prefix='/books')      # Add URL prefix for books
    app.register_blueprint(company_bp, url_prefix='/companies')  # Add URL prefix for companies

    return app  # ✅ Ensure the function returns the app properly


