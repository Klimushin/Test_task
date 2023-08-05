For running project rename .env.example file to .env . 
Insert into .env file BEARER_TOKEN and API_URL for source API

In source dir run command:
    docker-compose up --build

For adding db data connect to django container with command
    docker exec -it nimble_test_task_django_1 bash
and run script with command
    python manage.py db_update

For searching contact in db use GET request to http://0.0.0.0:8000/search with query params 'string'
