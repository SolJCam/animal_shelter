from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
from config import env_config_classes 
import os, pdb

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object(env_config_classes.DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

csrf = CSRFProtect(app)

from models import Room, Cage, Animal
from forms import AnimalForm, RoomForm



def get_cages(room):
    get_room = Room.query.filter_by(name=room).first()
    cages = Cage.query.filter_by(Room_id=get_room.id).all()
    cage_numbers = {}
    for cage in cages:
        animals = []
        for animal in Animal.query.filter_by(Cage_id=cage.id).all():
            animals.append(animal)
        if animals:
            cage_numbers[cage.cage_number] = animals
    return cage_numbers



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
        
        if bool(room) == False:
            error = f"There is no room named {form.current_name.data}. Please try again"
            return render_template('index.html', rooms=rooms, form=form, error=error)

        room.name = form.new_name.data
        db.session.merge(room)
        db.session.commit()
        flash('Room name successfully updated!')    
        return redirect(url_for('index'))
    error = [form.new_name.errors[0]]
    return render_template('index.html', rooms=rooms, form=form, error=error)



@app.route("/<room>/add_animal", methods=['POST'])
def add_animal(room):
    cage_ids = get_cages(room)
    form = AnimalForm(request.form)
    photo = AnimalForm(CombinedMultiDict((request.files,request.form)))
    if request.method == 'POST' and form.validate():
        animal = Animal(
            form.name.data, 
            form.age.data,
            form.gender.data,
            form.species.data,
        )
        if bool(photo.image_upload.data):
            f = photo.image_upload.data
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.root_path, 'static', filename))
            animal.image = filename

        cage_exists = Cage.query.filter_by(cage_number=form.cage.data).first()
        if bool(cage_exists) == True:
            animal.Cage_id = cage_exists.id
            db.session.add(animal)
            db.session.commit()
        else:
            room_id = Room.query.filter_by(name=form.room.data).first().id
            cage = Cage(form.cage.data)
            cage.Room_id = room_id
            db.session.add(cage)
            db.session.commit()
            animal.Cage_id = cage.id
            db.session.add(animal)
            db.session.commit()

        flash('Animal successfully added!')    
        return redirect(url_for('enter_room', room=room))

    if request.method == 'POST' and type(form.name.data) == int:
        try:
            if bool(Animal.query.filter_by(id=form.name.data).first().id) == True:
                animal = Animal.query.filter_by(id=form.name.data).first()
                db.session.delete(animal)
                db.session.commit()

                flash(f'{animal.name}, Unique ID# {form.name.data}, successfully removed!')    
                return redirect(url_for('enter_room', room=room))
        except AttributeError:
            print(AttributeError)
            error = [f"Unique Id {form.name.data} does not exist. Please try again."]   
            return render_template('room.html', cage_ids=cage_ids, room=room, form=form, error=error)         

    error = []

    if form.name.data == '':
        error.append("name : Field must be between 2 and 15 characters long.") 
    for item in form._fields.items(): 
        try:
            error.append(item[0]+" : "+form.errors[item[0]][0])
        except KeyError as e:
            print(f"No {e} error")
    return render_template('room.html', cage_ids=cage_ids, room=room, form=form, error=error)
