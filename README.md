# Django + Django Rest Framework API + Docker

A simple Django REST API set up with Algolia search. We leverage the power of Docker containers, making the app more modular.


## Getting started with development

Before firing up the python server you will need to add a .env file in the backend/cfehome path. Alternatively, you can add the below  you can change your environment variables in case you don't want to place them in the .env file. Get your APPLICATION ID, API KEY and INDEX PREFIX from your Algolia dashboard. As for your SECRET KEY and DEBUG, this have been hived off the settings file.
```
SECRET_KEY
DEBUG
APPLICATION_ID
API_KEY
INDEX_PREFIX
```
Run this comand to fire nginx and gunicorn as services.
```
docker-compose up --build
```