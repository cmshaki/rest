# Django + Django Rest Framework API + Docker

A simple Django REST API set up with Algolia search. We leverage the power of Docker containers, making the app more modular.


## Getting Started with Development

Before firing up the django server you will need to add a .env file in the backend/cfehome path. Alternatively, you can add this to your local environment variables. Get your APPLICATION_ID, API_KEY and INDEX_PREFIX from your Algolia dashboard. As for your SECRET_KEY and DEBUG, this have been hived off the django main app settings file.
```
SECRET_KEY
DEBUG
APPLICATION_ID
API_KEY
INDEX_PREFIX
```
There are two ways you can run the django server thats using its development server or using a docker container. We will go through the first step and that's through its inbuilt development server.

## Using Django Development Server
First ensure that you have python installed [here](https://www.python.org/downloads/). Next you will need to create a virtual environment.
```
python -m venv venv
```
Next you will need to activate the virtual environment.
```
~/venv/Scripts/activate
```
After activation, you will need to upgrade pip.
```
pip install --upgrade pip
```
Then run this command to install all dependencies, at the root of this repo where the requirements.txt file is.
```
pip install -r requirements.txt
```
After which you'll be ready to run the server change your terminal's folder to backend/cfehome and execute the command below
```
python manage.py runserver
```

## Using Docker
There are two base images that are used here that is python and nginx. Using compose we fire both up together, ensuring we have our production environment on the go. The service is exposed on port 80 and 8000 of the localhost. Port 8000 is being served by the gunicorn wsgi server while port 80 is being served by nginx. Run the command below to fire both services up.
```
docker-compose up --build
```