from wtforms import Form, StringField, IntegerField, SelectField, HiddenField, validators, ValidationError
from models import Cage, Animal

number_of_cages = Cage.query.all()

def current_cage(form, field):
    cage_id = Cage.query.filter_by(id=field.data).first().id
    animals = Animal.query.filter_by(Cage_id=cage_id).all()
    if len(animals) > 2:
        raise ValidationError('This cage is already full')

class AnimalForm(Form):
    name = StringField('Name', [validators.Length(min=2, max=15)])
    age = IntegerField('Age', [validators.NumberRange(min=0, max=100)])
    gender = SelectField(u'Gender', choices=['male', 'female'])
    species = StringField('Species', [validators.Length(min=3, max=20)])
    cage = IntegerField('Cage', [validators.NumberRange(min=0, max=len(number_of_cages)), current_cage])

class RoomForm(Form):
    current_name = StringField('Current_name', [validators.Length(min=4, max=25)])
    new_name = StringField('New_name', [validators.Length(min=4, max=25)])