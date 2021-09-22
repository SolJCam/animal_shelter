from app import db


class Room(db.Model):
    __tablename__ = 'Room'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    number_of_cages = db.Column(db.Integer)
    cage = db.relationship('Cage', backref='room', lazy=True)

    def __init__(self, name, number_of_cages):
        self.name = name
        self.number_of_cages = number_of_cages

    def __repr__(self):
        return '<id {}>'.format(self.id)




class Cage(db.Model):
    __tablename__ = 'Cage'

    id = db.Column(db.Integer, primary_key=True)
    animal = db.relationship('Animal', backref='cage', lazy=True)
    Room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)

    def __init__(self, animal, Room_id):
        self.animal = animal
        self.Room_id = Room_id

    def __repr__(self):
        return '<id {}>'.format(self.id)




class Animal(db.Model):
    __tablename__ = 'Animal'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
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




class Admin(db.Model):
    __tablename__ = 'Admin'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    email = db.Column(db.String(25), nullable=False, unique=True)
    password = db.Column(db.String(15), nullable=False, unique=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)