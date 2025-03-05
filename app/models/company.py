from app.extensions import db


class Company(db.Model):
    __tablename__= "companies"
    id = db.column(db.Integer,primary_key = True)
    name = db.Column(db.string(50),nullable=True)
    origin = db.Column(db.string(100),nullable=False)
    description = db.Column(db.Text(100),nullable=False,unique =True)
    user_id= db.Column(db.Integer,db.ForeignKey("users.id"))
    user =db.relationship("User",backref ="companies")
    created_at = db.Column(db.DateTime,default =datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())


    def __init__(self,name,origin,description,user_id)
        super(User,self).__init__()
        self.name =name
        self.origin =origin
        self.description=description
        self.user_id = user_id
        
def __repr__(self):
    return f"{self.name} {self.origin}"       
    


