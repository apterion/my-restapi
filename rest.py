#!/usr/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

@app.route('/users', methods=['GET'])
def get_users():
    return "GET /users"

@app.route('/users', methods=['POST'])
def post_users():
    return "POST /users"

if __name__ == '__main__':
    app.run(debug=True)
