from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class Playlists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    songs_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)


    def __repr__(self):
        return ''.join([
            'User: ', self.user_id, '\r\n',
            'Title: ', self.title, '\r\n', self.content
            ])



class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=False)
    artist = db.Column(db.String(100), nullable=False, unique=False)
    length = db.Column(db.Float, nullable=True, unique=False)
    playlists = db.relationship('Playlists', lazy=True)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    playlists = db.relationship('Playlists', backref='author', lazy=True)

    def __repr__(self):
        return ''.join([
            'UserID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])
        


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
