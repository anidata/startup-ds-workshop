from flask import Flask, jsonify, request, render_template, g
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from models import *
import requests 
import json
import re



app = Flask(__name__)

DATABASE = "../db/database.sqlite"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

db = get_db()

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message': 'It works!'})


@app.route('/home')
def index():
    cur = get_db().cursor()


@app.route('/api/titanic/aggregates', methods=['GET'])
def get_content(backpage_content_id):
    contents = (Backpagecontent.query.all())

    return jsonify({'data': [
        dict(id=c.index, pclass=c.pclass, count=c.count)
        for c in contents
    ]})


if __name__ == "__main__":
	app.run(debug=True, port = 8000)