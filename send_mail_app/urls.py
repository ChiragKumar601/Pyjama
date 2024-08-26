# myproject/urls.py

# send_mail_app/urls.py

from django.urls import path
from . import views

app_name = 'send_mail_app'  # This defines the namespace for the app

urlpatterns = [
    path('send/', views.send_email_view, name='send_email'),
    # Add other URL patterns here
]
