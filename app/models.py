from . import db

class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(80))
    price = db.Column(db.Float)
    balcony = db.Column(db.Boolean)
    smoking = db.Column(db.Boolean)
    pets = db.Column(db.Boolean)
