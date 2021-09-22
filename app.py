from flask import Flask, session, render_template
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os, pdb

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Room, Cage, Animal, Admin

# encrypt (or rather decrypt) admin psswrd credentials
bcrypt = Bcrypt(app)

# begin admin user session
SESSION_TYPE = 'Redis'
app.config.from_object(__name__)
Session(app)


@app.route("/")
def index():
    # pdb.set_trace()
    return render_template('index.html', message='Welcome to Queens animal shelter!!')

@app.route("/<room>")
def enter_room(room):
    return "You're in a room :)"

@app.route("/admin_login")
def admin_login():
    return "Hello admin"

@app.route("/submit_credentials/<username>/<password>")
def submit_credentials(username=None, password=None):
    bcrypt.check_password_hash(password, 'hunter2')
    return "Sccuessfully logged in!"    

@app.route("/<room>/<int:room_id>")
def edit_room_name(post_id):
    return "New name"

@app.route("/add_animal")
def add_animal():
    return "Added an animal!"


# pw_hash = bcrypt.generate_password_hash('hunter2').decode(‘utf-8’)
