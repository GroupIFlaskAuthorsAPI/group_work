from flask import request, jsonify, Blueprint
from app.models import db, Author
from passlib.hash import sha256_crypt

author_bp = Blueprint('author', __name__, url_prefix='/authors')

# Register Author Endpoint
@author_bp.route('/register', methods=['POST'])
def register_author():
    try:
        data = request.get_json()

        if not data or not isinstance(data, dict):
            return jsonify({"message": "Invalid request format. Expected JSON"}), 400

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            return jsonify({"message": "Missing required fields (name, email, password)"}), 400

        if Author.query.filter_by(email=email).first():
            return jsonify({"message": "Author with this email already exists."}), 400

        hashed_password = sha256_crypt.hash(str(password))  # Convert password to string
        new_author = Author(name=name, email=email, password=hashed_password)

        db.session.add(new_author)
        db.session.commit()

        return jsonify({"message": "Author registration successful!"}), 201

    except Exception as e:
        db.session.rollback()
        print(f"Error in registration: {str(e)}")
        return jsonify({"message": "Internal Server Error", "error": str(e)}), 500


# Login Author Endpoint
@author_bp.route('/login', methods=['POST'])
def login_author():
    try:
        data = request.get_json()

        if not data or not isinstance(data, dict):
            return jsonify({"message": "Invalid request format. Expected JSON"}), 400

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"message": "Missing required fields (email, password)"}), 400

        author = Author.query.filter_by(email=email).first()

        # Correct indentation for the 'if' statement
        if author and sha256_crypt.verify(str(password), author.password):  # Ensure password is a string
            return jsonify({"message": "Login successful!"}), 200

        return jsonify({"message": "Invalid email or password"}), 401

    except Exception as e:
        print(f"Error in login: {str(e)}")
        return jsonify({"message": "Internal Server Error", "error": str(e)}), 500
