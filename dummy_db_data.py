from app import db
from models import Room, Cage, Animal
import pdb

if __name__ == "__main__":
    # pdb.set_trace()

    def dummy_data():    
        room1 = Room("Alpha",15)
        room2 = Room("Omega",12)
        room3 = Room("Beta",3)
        room4 = Room("Kappa",6)
        room5 = Room("Sigma",11)
        db.session.add(room1)
        db.session.add(room2)
        db.session.add(room3)
        db.session.add(room4)
        db.session.add(room5)
        db.session.commit()



        cage1 = Cage(1)
        cage2 = Cage(2)
        cage3 = Cage(3)
        cage4 = Cage(4)
        cage5 = Cage(5)
        cage6 = Cage(6)
        cage7 = Cage(7)
        cage8 = Cage(8)
        cage9 = Cage(9)
        cage10 = Cage(10)
        cage11 = Cage(11)
        room_a = Room.query.filter_by(id=1).first().id
        room_b = Room.query.filter_by(id=2).first().id
        room_c = Room.query.filter_by(id=3).first().id
        room_d = Room.query.filter_by(id=1).first().id
        room_e = Room.query.filter_by(id=2).first().id
        room_f = Room.query.filter_by(id=3).first().id
        room_g = Room.query.filter_by(id=1).first().id
        room_h = Room.query.filter_by(id=2).first().id
        room_i = Room.query.filter_by(id=4).first().id
        room_j = Room.query.filter_by(id=5).first().id
        room_k = Room.query.filter_by(id=5).first().id
        cage1.Room_id = room_a
        cage2.Room_id = room_b
        cage3.Room_id = room_c
        cage4.Room_id = room_d
        cage5.Room_id = room_e
        cage6.Room_id = room_f
        cage7.Room_id = room_g
        cage8.Room_id = room_h
        cage9.Room_id = room_i
        cage10.Room_id = room_j
        cage11.Room_id = room_k
        db.session.add(cage1)
        db.session.add(cage2)
        db.session.add(cage3)
        db.session.add(cage4)
        db.session.add(cage5)
        db.session.add(cage6)
        db.session.add(cage7)
        db.session.add(cage8)
        db.session.add(cage9)
        db.session.add(cage10)
        db.session.add(cage11)
        db.session.commit()



        animal1 = Animal("spot",7,"male","dog")
        animal2 = Animal("peach",13,"male","orangutan")
        animal3 = Animal("tigger",11,"female","tiger")
        animal4 = Animal("hoot",15,"male","owl")
        animal5 = Animal("sal",5,"female","salamander")
        animal6 = Animal("spike",3,"female","dog")
        animal7 = Animal("oinky",6,"female","pig")
        animal8 = Animal("charolette",4,"female","spider")
        animal9 = Animal("piggy",12,"male","pig")
        animal10 = Animal("flutter",2,"male","butterfly")
        animal11 = Animal("anty",1,"male","ant")
        animal12 = Animal("A bug's Life",1,"male","bettle")
        animal13 = Animal("Beenie",2,"male","beetle")
        animal14 = Animal("felix",30,"female","cat")
        animal15 = Animal("garfield",40,"male","cat")

        cage_a = Cage.query.filter_by(id=1).first().id
        cage_b = Cage.query.filter_by(id=1).first().id
        cage_c = Cage.query.filter_by(id=1).first().id
        cage_d = Cage.query.filter_by(id=2).first().id
        cage_e = Cage.query.filter_by(id=3).first().id
        cage_f = Cage.query.filter_by(id=3).first().id
        cage_g = Cage.query.filter_by(id=4).first().id
        cage_h = Cage.query.filter_by(id=5).first().id
        cage_i = Cage.query.filter_by(id=5).first().id
        cage_j = Cage.query.filter_by(id=5).first().id
        cage_k = Cage.query.filter_by(id=6).first().id
        cage_l = Cage.query.filter_by(id=7).first().id
        cage_m = Cage.query.filter_by(id=8).first().id
        cage_n = Cage.query.filter_by(id=8).first().id
        cage_o = Cage.query.filter_by(id=9).first().id

        animal1.Cage_id = cage_a
        animal2.Cage_id = cage_b
        animal3.Cage_id = cage_c
        animal4.Cage_id = cage_d
        animal5.Cage_id = cage_e
        animal6.Cage_id = cage_f
        animal7.Cage_id = cage_g
        animal8.Cage_id = cage_h
        animal9.Cage_id = cage_i
        animal10.Cage_id = cage_j
        animal11.Cage_id = cage_k
        animal12.Cage_id = cage_l
        animal13.Cage_id = cage_m
        animal14.Cage_id = cage_n
        animal15.Cage_id = cage_o

        db.session.add(animal1)
        db.session.add(animal2)
        db.session.add(animal3)
        db.session.add(animal4)
        db.session.add(animal5)
        db.session.add(animal6)
        db.session.add(animal7)
        db.session.add(animal8)
        db.session.add(animal9)
        db.session.add(animal10)
        db.session.add(animal11)
        db.session.add(animal12)
        db.session.add(animal13)
        db.session.add(animal14)
        db.session.add(animal15)
        db.session.commit()

        return 'success!'

    dummy_data()


