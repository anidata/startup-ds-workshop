from flask import Flask, jsonify, request, render_template, g
from flask_sqlalchemy import SQLAlchemy
from models import *
import requests 
import json
import re


app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/Titanic"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def test():
	return jsonify({'message': 'It works!'})


@app.route('/home')
def index():
    cur = get_db().cursor()


@app.route('/titanic/aggregates', methods=['GET'])
def get_content():
    contents = (Class_agg.query.all())

    return jsonify({'data': [
        dict(id=c.index, pclass=c.pclass, count=c.count)
        for c in contents
    ]})


if __name__ == "__main__":
	app.run(debug=True, port = 8000)