from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    return "Welcome to Queens animal shelter!!"

@app.route("/<room>")
def enter_room(room):
    return "Welcome to Queens animal shelter!!"

@app.route("/<room>/<int:room_id>")
def edit_room_name(post_id):
    return "Welcome to Queens animal shelter!!"

@app.route("/add_animal")
def add_animal():
    return "Welcome to Queens animal shelter!!"