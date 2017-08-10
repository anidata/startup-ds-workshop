from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from models import *
import requests 
import json
import re


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/crawler"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message': 'It works!'})


# Backpagecontent table API endpoints with integer params and text search - returns title, body, postid
@app.route('/api/titanic/aggregates', methods=['GET'])
def get_content(backpage_content_id):
    contents = (Backpagecontent.query.all())

    return jsonify({'data': [
        dict(id=c.index, pclass=c.pclass, count=c.count)
        for c in contents
    ]})


if __name__ == "__main__":
	app.run(debug=True, port = 8000)