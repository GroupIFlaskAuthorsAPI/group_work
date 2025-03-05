from app.extensions import db
from datetime import datetime

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(50), nullable=False)  # Fixed `db.sting` -> `db.String`
    age = db.Column(db.Integer, nullable=False)  # Fixed `db.integer` -> `db.Integer`
    nationality = db.Column(db.String(50), nullable=False)  # Changed `Integer` to `String`
    bio = db.Column(db.String(255), nullable=False)  # Increased length for more bio text
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)
    contact = db.Column(db.String(50), nullable=False, unique=True)  # Fixed `db.column`

    def __repr__(self):
        return f"<Author {self.first_name} {self.last_name}>"
