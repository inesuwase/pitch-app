from . import db

#...

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    password_harsh
    Bio = db.Column(db.String(255))
    

    def __repr__(self):
        return f'User {self.username}'
