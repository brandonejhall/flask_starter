from app import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(),unique = True)
    numbed = db.Column(db.String())
    numbath = db.Column(db.String())
    location = db.Column(db.String())
    price = db.Column(db.String(18))
    r_type = db.Column(db.String())
    description = db.Column(db.String(500))
    photo = db.Column(db.String())