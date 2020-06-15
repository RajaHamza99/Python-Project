from application import db
from application.models import Playlists, Users


db.drop_all()
db.create_all()
