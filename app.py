from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from auth.author_controller import author_controller
from book.book_controller import book_controller
from company.company_controller import company_controller


app = Flask(__name__)
app.config["SQLACHEMY_DATABASE_URI"]= "sqlite:///authors_books_company.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view ="author.login" #redirect to login if not authenticated.

# Register Blueprints for controllers
app.register_blueprint(author_controller, url_prefix='/author')
app.register_blueprint(book_controller, url_prefix='/book')
app.register_blueprint(company_controller, url_prefix='/company')

if __name__ == '__main__':
    db.create_all()  # Create tables if they don't exist
    app.run(debug=True)



