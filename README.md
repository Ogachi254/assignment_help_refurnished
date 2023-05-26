# assignment_help_refurnished
# Assignment Help Project

This project is a web application for providing assignment help services. It allows users to create posts, view posts, and interact with other users in a collaborative environment.

## Features

- User registration and authentication
- Create and manage posts
- View and comment on posts
- User profiles and settings
- Responsive design for different devices

## Technologies Used

- HTML
- CSS
- JavaScript
- Python
- Django Web Framework
- Bootstrap Framework

## Setup and Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Ogachi254/assignment_help_refurnished.git

Navigate to the project directory:
cd assignment-help

install django 
pipenv install django 

activate the virtual enviroment 
pipenv shell 

Install project dependencies:
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

Start the development server:
python manage.py runserver

Open a web browser and access the application at http://localhost:8000.

Directory Structure
├── assignment_help/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── post/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   ├── static/
│   └── ...
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   ├── static/
│   └── ...
├── static/
│   ├── css/
│   ├── js/
│   └── ...
├── templates/
│   ├── base.html
│   ├── home.html
│   └── ...
├── manage.py
└── requirements.txt


License
This project is licensed under the MIT License. See the LICENSE file for details

And here's a sample `requirements.txt` file:
asgiref==3.6.0
certifi==2023.5.7
cffi==1.15.1
charset-normalizer==3.1.0
cryptography==40.0.2
defusedxml==0.7.1
dj-database-url==0.5.0
Django==3.2.0
django-allauth==0.54.0
django-appconf==1.0.5
django-crispy-forms==2.0
django-heroku==0.3.1
django-imagekit==4.1.0
gunicorn==20.1.0
idna==3.4
oauthlib==3.2.2
pilkit==2.0
Pillow==9.5.0
psycopg2==2.9.6
psycopg2-binary==2.9.6
pycparser==2.21
PyJWT==2.7.0
python-decouple==3.8
python-dotenv==0.21.0
python3-openid==3.2.0
pytz==2023.3
requests==2.30.0
requests-oauthlib==1.3.1
six==1.16.0
sqlparse==0.4.4
typing_extensions==4.5.0
tzdata==2023.3
urllib3==2.0.2
waitress==2.1.2
whitenoise==6.4.0


on deployment on render 
makesure you have procfile in your project directory with the following code in it.
web: waitress-serve --port=21029 pages_project.wsgi:application

now on deployment 
make sure you fill the rest of the informatio correctly.

build command is 
pip install -r requirements.txt

start command is 
waitress-serve --port $PORT pages_project.wsgi:application