from flask import request, jsonify, Blueprint
from app.models import db, Company

company_bp = Blueprint('company', __name__)

# Create a new company
@company_bp.route('/', methods=['POST'])
def create_company():
    data = request.get_json()
    name = data.get('name')
    address = data.get('address')

    if not name or not address:
        return jsonify({"message": "Missing required fields (name, address)"}), 400

    new_company = Company(name=name, address=address)
    db.session.add(new_company)
    db.session.commit()

    return jsonify({"message": "Company created successfully!"}), 201

# Get all companies
@company_bp.route('/', methods=['GET'])
def get_companies():
    companies = Company.query.all()
    # Returning structured response with id, name, and address
    return jsonify([{"id": company.id, "name": company.name, "address": company.address} for company in companies]), 200

# Get a single company
@company_bp.route('/<int:id>', methods=['GET'])
def get_company(id):
    company = Company.query.get(id)
    if not company:
        return jsonify({"message": "Company not found"}), 404
    return jsonify({"id": company.id, "name": company.name, "address": company.address})

# Update a company
@company_bp.route('/<int:id>', methods=['PUT'])
def update_company(id):
    data = request.get_json()
    company = Company.query.get(id)
    if not company:
        return jsonify({"message": "Company not found."}), 404
    
    company.name = data.get('name', company.name)
    company.address = data.get('address', company.address)
    db.session.commit()

    return jsonify({"message": "Company updated successfully!"}), 200

# Delete a company
@company_bp.route('/<int:id>', methods=['DELETE'])
def delete_company(id):
    company = Company.query.get(id)
    if not company:
        return jsonify({"message": "Company not found."}), 404
    
    db.session.delete(company)
    db.session.commit()

    return jsonify({"message": "Company deleted successfully!"}), 200
