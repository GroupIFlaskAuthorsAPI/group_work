from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models import db, Author  # Assuming you have an Author model

# Create the Blueprint
auth_bp = Blueprint('auth', __name__)

# Route for user registration
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validate input
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Missing required fields"}), 400

    # Hash the password
    hashed_password = generate_password_hash(data["password"])
    
    # Create a new author
    new_author = Author(username=data["username"], password=hashed_password)
    
    # Save to database
    db.session.add(new_author)
    db.session.commit()

    return jsonify({"message": "Author created successfully!"}), 201