from food import db


class Foods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Nome %r>' % self.name
