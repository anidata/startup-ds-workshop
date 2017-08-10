from titanic import db


class Titanic(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    passengerid = db.Column('passengerid', db.Integer, unique=True)
    survived = db.Column('survived', db.Integer)
    pclass = db.Column('pclass', db.Integer)
    name = db.Column('name', db.String(30))
    sex = db.Column('sex', db.String(30))
    age = db.Column('age', db.Integer)
    sibsp = db.Column('sibsp', db.Integer)
    parch = db.Column('parch', db.Integer)
    ticket = db.Column('ticket', db.String)
    fare = db.Column('fare', db.Integer)
    cabin = db.Column('cabin', db.String(30))
    embarked = db.Column('embarked', db.String(30))


class Class_agg(db.Model):
    index = db.Column('index', db.Integer, primary_key=True)
    pclass = db.Column('pclass', db.Integer)
    count = db.Column('count', db.Integer)