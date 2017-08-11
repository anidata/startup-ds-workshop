from flask import Flask, jsonify, request, render_template
import requests 
import json
import re

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!"
	

@app.route('/myName')
def display_name():
	return "Kaushik"
	

@app.route('/capitals')
def display_capitals():
	return jsonify({'Texas': 'Austin', 'California': 'Sacramento', 'Georgia': 'Atlanta'})


if __name__ == "__main__":
	app.run(debug=True, port = 8000)  