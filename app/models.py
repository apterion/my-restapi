from app import db

class Contracts(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    signed_date = db.Column(db.Date, index = False, unique = False, required=True)
    text = db.Column(db.Text(), index = False, unique = False, required=True)
    updated_date = db.Column(db.Date)

    def __repr__(self):
        return '<Contracts ID %r>' % (self.id)
