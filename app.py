from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import env_config_classes 
import os, pdb

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(env_config_classes.DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

csrf = CSRFProtect(app)

from models import Room, Cage, Animal
from forms import AnimalForm, RoomForm



def get_cages(room):
    get_room = Room.query.filter_by(name=room).first()
    cages = Cage.query.filter_by(Room_id=get_room.id).all()
    cage_ids = {}
    for cage in cages:
        animals = []
        for animal in Animal.query.filter_by(Cage_id=cage.id).all():
            animals.append(animal)
        if animals:
            cage_ids[cage.id] = animals
    return cage_ids



@app.route("/")
def index():
    rooms = Room.query.all()
    form = RoomForm(request.form)
    return render_template('index.html', rooms=rooms, form=form)



@app.route("/room/<room>")
def enter_room(room):
    cage_ids = get_cages(room)
    form = AnimalForm(request.form)
    return render_template('room.html', cage_ids=cage_ids, room=room, form=form) 



@app.route("/change_room_name", methods=['POST'])
def change_room_name():
    rooms = Room.query.all()
    form = RoomForm(request.form)
    if request.method == 'POST' and form.validate():
        room = Room.query.filter_by(name=form.current_name.data).first()
        room.name = form.new_name.data
        db.session.merge(room)
        db.session.commit()
        return redirect(url_for('index'))
    error = form.new_name.errors[0]
    return render_template('index.html', rooms=rooms, form=form, error=error)



@app.route("/<room>/add_animal", methods=['POST'])
def add_animal(room):
    cage_ids = get_cages(room)
    form = AnimalForm(request.form)
    if request.method == 'POST' and form.validate():
        animal = Animal(
            form.name.data, 
            form.age.data,
            form.gender.data,
            form.species.data,
        )
        animal.Cage_id = form.cage.data
        db.session.add(animal)
        db.session.commit()
        return redirect(url_for('enter_room', room=room))
    # if 'cage' in form.errors:
    #     error = form.cage.errors[0]
    # else:
    #     error = form.name.errors[0]

    error = form.cage.errors[0]
    return render_template('room.html', cage_ids=cage_ids, room=room, form=form, error=error)
