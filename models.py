from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_URL= "https://i.postimg.cc/X7bM1pW6/download.png"

class Pet(db.Model):
    """Renders Pet Model"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                        nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)

    def pet_img(self):
        """Default image if none provided"""
        return self.photo_url or DEFAULT_IMG_URL

    
def connect_db(app):
    db.app = app
    db.init_app(app)