from app.extensions import db
from datetime import datetime

class Author(db.Model):
    __tablename__ = "users"
    id = db.column(db.Integer,primary_key = True)
    first_name = db.Column(db.string(50),nullable=False)
    last_name = db.Column(db.string(100),nullable=False)
    email = db.Column(db.string(100),nullable=Flase,unique =True)
    contact = db.Column(db.string(50),nullable=Flase,unique=True)
    image= db.Column(db.string(255),nullable=True)
    password = db.Column(db.Text(),nullable=False)
    biography = db.Column(db.Text(),nullable=False)
    user_type = db.Column(db.string(20),default="author")
    created_at = db.Column(db.DateTime,default =datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())


    def __init__(self,id,first_name,last_name,email,contact,password,biography,user_type,image=None)
        super(User,self).__init__()
        self.first_name =first_name
        self.last_name =last_name
        self.email=email
        self.contact = contact
        self.password =password
        self.biography = biography
        self.user_type = user_type
        self.image = image

def get_full_name(self):
    return f"{self.last_name} {self.first_name}"        
    






    