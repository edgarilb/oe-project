# OE project

OE needs to process so-called “flow” files in order to communicate with the energy industry.
These are pipe-delimited text files that are sent to us via sFTP. Our systems then import
each file into our database.


## The first thing to do is to clone the repository:

cd octopus


## Create a virtual environment to install dependencies in and activate it:

$ virtualenv venv -p python3
$ source env/bin/activate

## Then install the dependencies:

(env)$ pip install django

## Start db.sqlite3 :

(env)$ python manage.py migrate

## Create migration:

(env)$ python manage.py makemigrations

env)$ python manage.py migrate

## Once pip has finished downloading the dependencies:

(env)$ python manage.py runserver

## Walkthrough

- files can be imported via the command-line: Use command => python manage.py mycommand PATH_DIR_FILE --option1 INT_NUMBER. This will display to user at least 20 records from D0010 flow file, depending on the number input on --option1. If it is more than 20 will display more than 20, unless it reaches the maximum in the file, in which scenario the max number contained in the file will be shown. 

- files can be uploaded via web on the UPLOAD TAB. => Choose a .uff file (D0010) and click on upload file. Then it will be saved to the data base as well as displaying to the user. 

## Comments

If I would have more time:
- I would write functions to difirentiate each meter data, reading, meter point, MPAN, etc. 
- I would add search capabilities based on values provided on serial number or meter point
- Unit testing


