from django.contrib import admin
from django.urls import path, include
from .views import mail_sender
from django.views import View



app_name = 'new_mailer'


urlpatterns = [
    path('send_mail/', mail_sender, name='send_mail' )
]
