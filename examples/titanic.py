from flask import Flask, jsonify, request, render_template, g, make_response
from flask_sqlalchemy import SQLAlchemy
from models import *
import requests
import json
import re


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://root:password@172.17.0.1:5432/titanic"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def test():
	return jsonify({'message': 'It works!'})


@app.route('/titanic/aggregates', methods=['GET'])
def get_content():
    contents = (Class_agg.query.all())

    json_data = jsonify({'data': [
        dict(id=c.index, pclass=c.pclass, count=c.count)
        for c in contents
    ]})

    # The following to used to handle some security implemented by
    # browsers/servers. For more info see the following
    #
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS
    # http://flask.pocoo.org/snippets/56/
    response = make_response(json_data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8000)
