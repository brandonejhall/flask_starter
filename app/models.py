from app import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(),unique = True)
    numbed = db.Column(db.String())
    numbath = db.Column(db.String())
    location = db.Column(db.Text())
    price = db.Column(db.Text())
    r_type = db.Column(db.Text())
    description = db.Column(db.Text())
    photo = db.Column(db.Text())