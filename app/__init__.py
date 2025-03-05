from flask import flask
from app.extensions import db
from app.controllers.auth.controllers import auth


#creating a factory function
def create_app():

    #an app instance
    app = Flask(__name__)

    db.init_app(app)


    @app.route("/")
    def home():
        return "Author API project setup 1"




        return app
