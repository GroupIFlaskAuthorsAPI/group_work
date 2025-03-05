
from flask import Blueprint

# Define the blueprints only once
author_bp = Blueprint('author', __name__, url_prefix='/authors')
book_bp = Blueprint('book', __name__, url_prefix='/books')
company_bp = Blueprint('company', __name__, url_prefix='/companies')

# Import the controller files which should define routes
from .author.controller import *
from .book.controller import *
from .company.controller import *
