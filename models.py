from app import db


class Room(db.Model):
    __tablename__ = 'room'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)
    number_of_cages = db.Column(db.Integer)
    cage = db.relationship('Cage', backref='Room', lazy=True)

    def __init__(self, name, number_of_cages):
        self.name = name
        self.number_of_cages = number_of_cages

    def __repr__(self):
        return '<id {}>'.format(self.id)




class Cage(db.Model):
    __tablename__ = 'cage'

    id = db.Column(db.Integer, primary_key=True)
    cage_number = db.Column(db.Integer)
    animal = db.relationship('Animal', backref='Cage', lazy=True)
    Room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)

    def __init__(self, cage_number):
        self.cage_number = cage_number

    def __repr__(self):
        return '<id {}>'.format(self.id)




class Animal(db.Model):
    __tablename__ = 'animal'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(6))
    species = db.Column(db.String(15))
    Cage_id = db.Column(db.Integer, db.ForeignKey('cage.id'), nullable=False)

    def __init__(self, name, age, gender, species):
        self.name = name
        self.age = age
        self.gender = gender
        self.species = species

    def __repr__(self):
        return '<id {}>'.format(self.id)