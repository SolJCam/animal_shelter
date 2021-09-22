
flask run
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade


# <<<<<<<<<<<<<<<<<STACK OVERFLOW SOLUTION FOR 'No changes in schema detected' error>>>>>>>>>>>>>>>>>>>>>>
from models import Room, Cage, Animal, Admin
# <<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>