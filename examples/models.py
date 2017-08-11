from titanic import db

class Class_agg(db.Model):
    index = db.Column('index', db.Integer, primary_key=True)
    pclass = db.Column('pclass', db.Integer)
    count = db.Column('count', db.Integer)