from wtforms import Form, StringField, IntegerField, SelectField, validators, ValidationError
from models import Room, Cage, Animal
import pdb



# def current_cage(form, field):
#     pdb.set_trace()
#     cage_id = Cage.query.filter_by(id=field.data).first().id
#     animals = Animal.query.filter_by(Cage_id=cage_id).all()
#     if len(animals) > 2:
#         raise ValidationError('Please try a cage with fewer than 3 animals. The cage you selected is already full')

def current_cage(form, field):
    # pdb.set_trace()
    cage_exists = Cage.query.filter_by(cage_number=field.data).first()
    if bool(cage_exists) == True:
        cage_id = cage_exists.id
        animals = Animal.query.filter_by(Cage_id=cage_id).all()
        if len(animals) > 2:
            raise ValidationError(f'Please try a cage with fewer than 3 animals. Cage {field.data} is already full')

# def unique_animal_name(form, field):
#     is_name_taken = Animal.query.filter_by(name=field.data).first()
#     if is_name_taken:
#         raise ValidationError(f"Please try a different name. There's already an animal named {field.data} in our records")

number_of_cages = Cage.query.all()


def unique_room_name(form, field):
    is_room_name_taken = Room.query.filter_by(name=field.data).first()
    if is_room_name_taken:
        raise ValidationError(f"Please try a different name. {field.data} is already being used")


class AnimalForm(Form):
    name = StringField('Name or Id', [validators.Length(min=2, max=15)])
    # name = StringField('Name', [validators.Length(min=2, max=15), unique_animal_name])
    age = IntegerField('Age', [validators.NumberRange(min=0, max=100)])
    gender = SelectField(u'Gender', choices=['male', 'female'])
    species = StringField('Species', [validators.Length(min=3, max=20)])
    room = StringField('Room', [validators.Length(min=2, max=15)])
    cage = IntegerField('Cage', [current_cage])
    # cage = IntegerField('Cage', [validators.NumberRange(min=0, max=len(number_of_cages)), current_cage])


class RoomForm(Form):
    current_name = StringField('Current_name', [validators.Length(max=25)])
    new_name = StringField('New_name', [validators.Length(min=3, max=25), unique_room_name])