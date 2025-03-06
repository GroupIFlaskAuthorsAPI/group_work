from app import create_app, db
from app.models import Author, Book, Company  # Import your models to ensure tables are created

app = create_app()

# This ensures that tables are created before running the app
with app.app_context():
    db.create_all()  # This will create the tables if they don't already exist

if __name__ == '__main__':
    app.run(debug=True)
