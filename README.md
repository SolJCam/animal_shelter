# About

Animal Shelter is an admin dashboard that allows the user to enter different rooms and view bigraphical data on the animals stored in the database.
Users can update room names and add animals to the database.


## Getting Started

### Before getting started...

You will need to have a Postgres database, python3.9 and pip installed on you local drive.


### Step One: Cloning the database

Clone the repo, using the following url:
https://github.com/SolJCam/animal_shelter.git


### Step Two: Setting up Dependencies

On the command line in the project's root directory, run the following command to install all necessary dependencies:
```pip install -r requirements.txt```
    
**It is strongly adivsed you set up a virtual environment to avoid installed packages from conflicting with other python projects you may have on your harddrive.
You can read more about virtual environments here: https://realpython.com/python-virtual-environments-a-primer/**


### Step Three: Exporting Environment Variables

In the root directory, export the following environment variables: 

    export DATABASE_URL="postgresql:///animal_shelter"
    export APP_SETTINGS="config.DevelopmentConfig"
    export SECRET_KEY="you-need-to-update-this"

***Yes the string passed to ```SECRET_KEY``` is a hint; you should update this with your own value***

### Step Four: Getting the Database Set Up

#### part 1. Create a database called 'animal_shelter' through psql

#### part 2. Run the following commands from within the project root:
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

#### part 3. Populate the database with dummy starter data 
```python dummy_db_data.py```

### You're All Set!!
To start the prdoduction server run the following command from the project root:
```flask run```

## Stack
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- WTForms
- psql
- semantic-ui
- jQuery
