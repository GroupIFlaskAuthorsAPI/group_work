# app/__main__.py
from app import create_app

app = create_app()  # No need to unpack it since create_app already returns the app object
app.run(debug=True)  # Optional: Set debug=True for development
