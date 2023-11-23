# Django + Django Rest Framework API

A simple Django REST API set up with Algolia search.


## Getting started with development

Before firing up the python server you will need to add a .env file in the backend/cfehome path. Make sure that you add these fields in the .env file.
```
APPLICATION_ID
API_KEY
INDEX_PREFIX
```
Then run this command to install all dependencies, at the root of this repo where requirements.txt file is.
```
pip install -r requirements.txt
```
After which you'll be ready to run the server change your terminal's folder to backend/cfehome and execute the command below
```
python manage.py runserver
```
