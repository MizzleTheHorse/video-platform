# models.py

from flask_login import UserMixin
#from . import db

#class UserEdit(UserMixin, db.Model):
#    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#    email = db.Column(db.String(100), unique=True)
#    password = db.Column(db.String(100))
#    name = db.Column(db.String(1000))#
#
#    def __repr__(self):
#        return '<User %r>' % self.name


class User(UserMixin):

    def __init__(self, user_id, name, email,  hashed_password):
        super().__init__()
        self.user_id = user_id
        self.id = user_id
        self.email = email
        self.name = name
        self.hashed_password = hashed_password
            
    def __repr__(self):
        return '<User %r>' % self.name


class Video(UserMixin):
    #video_i, duser_id, title, resume, category = False

    def __repr__(self):
        return '<Video %r>' % self.title

