from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 
    'config.settings'
)

app = Celery('recipe-api')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# path/to/your/proj/src/cfehome/celery.py



# Below is for illustration purposes. We 
# configured so we can adjust scheduling 
# in the Django admin to manage all 
# Periodic Tasks like below
app.conf.beat_schedule = {
    'send-email': {
        'task': 'send_mail_app.views.send_email_view',
        'schedule': crontab(hour=14, minute=10),
    },
}
