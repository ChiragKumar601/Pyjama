from .base import *


DEBUG = True
ALLOWED_HOSTS = ['localhost']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# config/settings/development.py or settings.py

# settings.py

# CELERY_BROKER_URL = 'redis://localhost:6380/0'
# CELERY_RESULT_BACKEND = 'redis://localhost:6380/0'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'UTC'

