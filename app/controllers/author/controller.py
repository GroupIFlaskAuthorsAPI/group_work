from flask import request, jsonify, Blueprint
from app.models import db, Author
from werkzeug.security import generate_password_hash, check_password_hash

# Define the Blueprint with the '/authors' URL prefix
author_bp = Blueprint('author', __name__, url_prefix='/authors')

# Author Registration
@author_bp.route('/register', methods=['POST'])
def register_author():
    data = request.get_json()
    
    # Check if all required fields are provided
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Validations for the incoming request 
    if not name or not email or not password:
        return jsonify({"message": "Missing required fields (name, email, password)"}), 400

    if Author.query.filter_by(email=email).first():
        return jsonify({"message": "Author with this email already exists."}), 400
    
    # Hash the password
    hashed_password = generate_password_hash(password, method='sha256')
    new_author = Author(name=name, email=email, password=hashed_password)
    
    try:
        db.session.add(new_author)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error saving to the database", "error": str(e)}), 500

    return jsonify({"message": "Author registration successful!"}), 201

# Author Login
@author_bp.route('/login', methods=['POST'])
def login_author():
    data = request.get_json()
    
    # Check if all required fields are provided
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Missing required fields (email, password)"}), 400

    author = Author.query.filter_by(email=email).first()
    if author and check_password_hash(author.password, password):
        return jsonify({"message": "Login successful!"}), 200

    return jsonify({"message": "Invalid email or password"}), 401
