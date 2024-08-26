We are using psycopg2-binary instead of psycopg2.
Using coverage here for unit testing
celery -A config worker --loglevel=info --pool=solo
CELERY_RESULT_BACKEND_TRANSPORT_OPTIONS = {'socket_timeout': 30, 'retry_on_timeout': True}
docker build --no-cache -t sampleptt .


Steps to run:

1. Ensure that latest python server is installed in your system.
2. Open the powershell terminal and run d