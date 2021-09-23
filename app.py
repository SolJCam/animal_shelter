from flask import Flask, session, render_template
from flask_sqlalchemy import SQLAlchemy
import os, pdb

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from models import Room, Cage, Animal, Admin


@app.route("/")
def index():
    rooms = Room.query.all()
    return render_template('index.html', rooms=rooms)

@app.route("/room/<room>")
def enter_room(room):
    get_room = Room.query.filter_by(name=room).first()
    cages = Cage.query.filter_by(Room_id=get_room.id).all()
    cage_ids = {}
    for cage in cages:
        animals = []
        for animal in Animal.query.filter_by(Cage_id=cage.id).all():
            animals.append(animal)
        if animals:
            cage_ids[cage.id] = animals
    # pdb.set_trace()
    return render_template('room.html', cage_ids=cage_ids, room=room)

@app.route("/admin_login")
def admin_login():
    return "Hello admin"

@app.route("/submit_credentials/<username>/<password>")
def submit_credentials(username=None, password=None):
    # bcrypt.check_password_hash(password, 'hunter2')
    return "Sccuessfully logged in!"    

@app.route("/<room>/<int:room_id>")
def edit_room_name(post_id):
    return "New name"

@app.route("/add_animal")
def add_animal():
    return "Added an animal!"
