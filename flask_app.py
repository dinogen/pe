
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = {"user_id": user_id, "name": "mario"}
    return json.dumps(user)



