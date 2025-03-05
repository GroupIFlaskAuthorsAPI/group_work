from flask import request, jsonify, Blueprint
from app.models import db, Book, Author

book_bp = Blueprint('book', __name__)

#Create a new book
@book_bp.route('/', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    genre = data.get('genre')
    author_id = data.get('author_id')

    author = Author.query.get(author_id)
    if not author:
        return jsonify({"message": "Author not found."}), 404
    

    new_book = Book(title=title, genre=genre, author_id=author_id)
    db.session.add(new_book)
    db.session.commit()

    return jsonify({"message": "Book created successfully"}), 200

# Get a single book
@book_bp.route('/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    return jsonify({"title": book.title, "genre": book.genre}), 200

# Update a book
@book_bp.route('/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get(id)
    if not book:
        return jsonify({"message": "Book not found."}), 404
    
    book.title = data.get('title', book.title)
    book.genre = data.get('genre', book.genre)
    db.session.commit()

    return jsonify({"message": "Book updated successfully"}), 200

# Delete a book
@book_bp.route('/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    
    db.session.delete(book)
    db.session.commit()

    return jsonify ({"message": "Book deleted successfully"}), 200