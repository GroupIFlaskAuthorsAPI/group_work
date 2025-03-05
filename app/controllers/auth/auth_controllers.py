from flask import Blueprint,request,jsonify
from app.status_codes import HTTP_400_BAD_REQUEST,HTTP_409_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED
import validators
from app.models.users import User
from app.extensions import db


auth = Blueprint("auth",__name__,url_prefix ="api/v1/auth")

#user registration
@auth.route('/register',methods = ['POST'])
def register_user():
    data = request.json
    first_name = data("first_name")
    last_name = data.get("last_name")
    contact = data.get("contact")
    email = data.get("email")
    type = data.get("type") if "user_type" in data else "author"
    password = data.get("password")
    biography = data.get("biography",'') if type == "author" else ''

#THESE ARE THE VALIDATIONS OF DATA
    if not first_name or last_n





#auth Blueprintame or not contact or not password or not email:
        return jsonify({"error":"All fields are required"}),HTTP_400_BAD_REQUEST

    if type == "author" and not biography:
        return jsonify({"error":"Enter your author biography"}),HTTP_400_BAD_REQUEST

    if len(password) < B:
        return jsonify({"error":"Password id too short"}),HTTP_400_BAD_REQUEST

    if User.query.filter_by(email = email).first() is note None:
        return jsonify({"error":"Email address in use"}),HTTP_409_CONFLICT

    
    if User.query.filter_by(contact = contact).first() is note None:
        return jsonify({"error":"Contact in use"}),HTTP_409_CONFLICT


        try:
            hashed_password = bcrypt.generate_password_harsh(password)
            now_user = User(first_name = first_name,last_name=last_name,password=password,email=email,contact=contact)
            db.session.add(new_user)
            db.session.commit()

## creating the user name
            user_name = new_user.get_full_name()


            return jsonify({
                "message":user_name + "has been successfully created as an" + new_user,user_type,
                'user':{
                    'id': author.id,
                    'first_name': author.first_name,
                    'last_name': author.last_name,
                    'email': author.email,
                    'contact': author.contact,
                    'image': author.image,
                    'biography': author.biography,
                    'user_type': author.user_type,
                    'created_at': author.created_at.isoformat(),
                    'updated_at': author.updated_at.isoformat() if author.updated_at else None,
                }
            }),HTTP_201_CREATED


        except Exeption as e:
            db.session.rollback()
            return jsonify({"ERROR":str(e)}),HTTP_500_INTERNAL_SERVER_ERROR

                



