from flask import Flask
from app.extensions import db, migrate
from app.controller.auth.controller import auth_bp
from app.controller.books.controller import books_bp
from app.controller.company.controller import company_bp
from flask_jwt_extended import JWTManager

def create_app(config_object='app.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(books_bp, url_prefix='/books')
    app.register_blueprint(company_bp, url_prefix='/company')

    return app
