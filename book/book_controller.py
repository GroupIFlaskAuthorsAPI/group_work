
from flask import Blueprint, request, jsonify # Define the blueprint for book
from app import db
from models import Book

book_controller = Blueprint('book', __name__)

# Create book
@book_controller.route('/', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book =Book(name=data['name'], title=data.get('title'), price=data.get("price"))
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'book created'}), 201

# Get all books
@book_controller.route('/', methods=['GET'])
def get_all_books():
    book =book.query.all()
    return jsonify([{'id': book.id, 'name': book.name, 'title': book,"title":book.price}for book in book])

# Get Book by ID
@book_controller.route('/<int:id>', methods=['GET'])
def get_book_by_id(id):
    book =book.query.get(id)
    if book:
        return jsonify({'id': book.id, 'name': book.name, 'title': book.title, "price":book.price })
    return jsonify({'message': 'Book not found'}), 405

# Update Book
@book_controller.route('/<int:id>', methods=['PUT'])
def update_book(id):
    book = book_controller.query.get(id)
    if book:
        data = request.get_json()
        book.name = data['name']
        book.title.get('title')
        book.price.get('price')
        db.session.commit()
        return jsonify({'message': 'Book updated'})
    return jsonify({'message': 'Book not found'}), 405

# Delete Book
@book_controller.route('/<int:id>', methods=['DELETE'])
def delete_book(id):
    book =book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted'})
    return jsonify({'message': 'Book not found'}), 405
