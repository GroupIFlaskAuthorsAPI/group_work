from flask import Blueprint, request, jsonify
from app import db
from models import Company

company_controller= Blueprint('company', __name__)

# Create Company
@company_controller.route('/', methods=['POST'])
def create_company():
    data = request.get_json()
    new_company = Company(name=data['name'], location=data.get('location'))
    db.session.add(new_company)
    db.session.commit()
    return jsonify({'message': 'Company created'}), 201

# Get all Companies
@company_controller.route('/', methods=['GET'])
def get_all_companies():
    companies = Company.query.all()
    return jsonify([{'id': company.id, 'name': company.name, 'location': company.location} for company in companies])

# Get Company by ID
@company_controller.route('/<int:id>', methods=['GET'])
def get_company_by_id(id):
    company = Company.query.get(id)
    if company:
        return jsonify({'id': company.id, 'name': company.name, 'location': company.location})
    return jsonify({'message': 'Company not found'}), 405

# Update Company
@company_controller.route('/<int:id>', methods=['PUT'])
def update_company(id):
    company = Company.query.get(id)
    if company:
        data = request.get_json()
        company.name = data['name']
        company.location = data.get('location')
        db.session.commit()
        return jsonify({'message': 'Company updated'})
    return jsonify({'message': 'Company not found'}), 405

# Delete Company
@company_controller.route('/<int:id>', methods=['DELETE'])
def delete_company(id):
    company = Company.query.get(id)
    if company:
        db.session.delete(company)
        db.session.commit()
        return jsonify({'message': 'Company deleted'})
    return jsonify({'message': 'Company not found'}), 405
