We are using psycopg2-binary instead of psycopg2.
Using coverage here for unit testing
celery -A config worker --loglevel=info --pool=solo
CELERY_RESULT_BACKEND_TRANSPORT_OPTIONS = {'socket_timeout': 30, 'retry_on_timeout': True}
docker build --no-cache -t sampleptt .


Steps to run on local machine:

1. Ensure that latest python server is installed in your system.
2. Run python manage.py runserver.
3. Open the powershell terminal and run this command - "docker run -d --name redis-server -p 6379:6379 redis".
4. Open another terminal and run this command - "celery -A config.celery worker --loglevel=info".
5. Now you can open the localhost:8000 and run the application.

Note: Email scheduling is not working properly because of some caching issues. For email to be sent to the users 
      you have to hit the endpoint "/email/send".