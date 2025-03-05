
from flask import Flask
from app.extensions import db,migrate
from app.extensions import db  # If running from project root

# Application factory function
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load configuration

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register models (not needed unless imported elsewhere)
    from app.models.author_model import Author
    from app.models.book_model import Book
    from app.models.company_model import Company

    # Index route
    @app.route('/')
    def index():
        return "Hello"

    return app

