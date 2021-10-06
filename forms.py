from wtforms import Form, StringField, IntegerField, SelectField, FileField, validators, ValidationError, Field
from wtforms.widgets import TextInput
from wtforms.compat import text_type
from wtforms.utils import unset_value
from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileAllowed
from models import Room, Cage, Animal
import pdb




class StringOrIntegerField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return self.data
        elif self.data is not None:
            return text_type(self.data)
        else: 
            return ''

    def process_data(self, value):
        if value is not None and value is not unset_value:
            try:
                self.data = int(value)
            except (ValueError, TypeError):
                self.data =  str(value)
        else:
            self.data = None

    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = int(valuelist[0])
            except ValueError:
                self.data = valuelist[0]


def current_cage(form, field):
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

images = UploadSet('images', IMAGES)

def unique_room_name(form, field):
    is_room_name_taken = Room.query.filter_by(name=field.data).first()
    if is_room_name_taken:
        raise ValidationError(f"Please try a different name. {field.data} is already being used")


class AnimalForm(Form):
    name = StringOrIntegerField('Name or Id')
    # name = StringField('Name', [validators.Length(min=2, max=15), unique_animal_name])
    age = IntegerField('Age', [validators.NumberRange(min=0, max=100)])
    gender = SelectField(u'Gender', choices=['male', 'female'])
    species = StringField('Species', [validators.Length(min=3, max=20)])
    image_upload = FileField(u'Photo', validators=[FileAllowed(images, 'Images only!')])
    room = StringField('Room', [validators.Length(min=2, max=15)])
    cage = IntegerField('Cage', [current_cage])


class RoomForm(Form):
    current_name = StringField('Current_name', [validators.Length(max=25)])
    new_name = StringField('New_name', [validators.Length(min=3, max=25), unique_room_name])