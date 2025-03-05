

from flask import Blueprint, request, jsonify
from app import db
from models import Author

author_controller= Blueprint("aubpthor",__name__)

# Create Author
@author_controller.route('/',methods=['POST'])
def create_author():
    data = request.get_json()
    new_author=Author(name=data["name"],biography=data.get("biograpy"))
    db.session.add(new_author)
    db.session.commit()
    return jsonify({'message': ' Author created'}),200

# Get all authors
@author_controller.route('/',methods=['GET'])
def get_all_author():
    authors= Author.query.all()
    return jsonify([{'id': author.id, 'name':author.name, 'biography':author.biography}for author in authors])

# Get Author by Id
@author_controller.route('/<int:id>', methods=['GET'])
def get_all_authors():
    author = Author.query.all(id)
    if author:
        return jsonify({'id': author.id, 'name':author.name,'biography':author.biography})
    return jsonify({'message': ' Author not found'}) , 200

# Update Author
@author_controller.route('/<int:id>', methods=['put'])
def update_author(id):
    author=Author.query.get(id)
    if author:
        data = request.get_json()
        author.name=data.get('name')
        author.biography =data.get('biography')
        db.session.commit()
        return jsonify({'message': " Author updated"})
    return jsonify({'message': ' Author not found'}),205

# Delete Author
@author_controller.route('/<int:id>', methods=['DELETE'])
def delete_author(id):
    author = Author.query.get(id)
    if author:
        db.session.delete(author)
        db.session.commit()
        return jsonify({'message': ' Author deleted'})
    return jsonify({'message': ' Author not found'}) ,700
