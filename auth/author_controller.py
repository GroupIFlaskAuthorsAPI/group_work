# auth/author_controller.py

from flask import Blueprint

# Define the blueprint
author_bp = Blueprint('author', __name__)

# Example route
@author_bp.route('/')
def index():
    return "Author page"

