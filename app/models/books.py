from app.extensions import db
from datetime import datetime

class Book(db.Model):
    __tablename__ = "books"
    id = db.column(db.Integer,primary_key = True)
    title = db.Column(db.string(150),nullable=False)
    pages = db.Column(db.Integer(100),nullable=False)
    price = db.Column(db.Integer(100),nullable=False)
    price_unit= db.Column(db.string(50),nullable=False,default="UGX")
    publication_date = db.Column(db.Date,nullable=False)
    isbn = db.Column(db.string(30),nullable=True,unique=True)
    genre = db.Column(db.string(50),nullable=False)
    description = db.Column(db.string(255),nullable=False)
    image = db.Column(db.string(255),nullable =False)
    User_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    company_id = db.Column(db.Integer,db.ForeignKey("company.id"))
    User =db.relationship("User",backref = "companies")
    company =db.relationship("company",backref = "books")
    created_at = db.Column(db.DateTime,default =datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

    def __init__(self,title,price,description,price_unit,publication_date,isbn,genre,image,User_id,company_id,user,company ):
        super(Book,self).__init__()
        self.title=title
        self.price=price
        self.description=description
        self.price_unit = price_unit
        self.publication_date =publication_date
        self.isbn= isbn
        self.genre = genre
        self.image = image
        self.User_id= User_id
        self.company_id = company_id
        self.company= company
        

def __repr__(self) ->str:
    return f"Book{self.title}"        
    






    