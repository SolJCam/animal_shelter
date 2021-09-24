# About

Animal Shelter is an admin dashboard that allows the user to enter different rooms and view bigraphical data on the animals stored in the database.
Users can update room names and add animals to the database.


## Before getting started...

You will need to have a Postgres database, python3.9 and pip installed on you local drive.


#### Step One: Cloning the database

Clone the repo, useing the following url:
https://github.com/SolJCam/animal_shelter.git


#### Step Two: Setting up Dependencies

From the directory where the repository was cloned, run the following command to install all necessary dependencies:
pip install -r requirements.txt
    
*** It is strongly adivsed you set up a virtual environment to avoid installed packages from conflicting with other projects
You can read more about virtual environments here: https://realpython.com/python-virtual-environments-a-primer/ ***


#### Step Three: Exporting Environment Variables

Export the following environment variables - 

    export DATABASE_URL="postgresql:///animal_shelter"
    export APP_SETTINGS="config.DevelopmentConfig"
    export SECRET_KEY="this-is-a-secret-key"


#### Step Four: Getting the Database Set Up

part 1. Create a database called 'animal_shelter' through psql

part 2. Run the following commands from within the project root:
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

part 3. Populate the database with dummy starter data
``` 
python dummy_db_data.py 
```

You're All Set!!
To start the server run the followin command from the project root:
```
FLASK_ENV=development flask run
```
