from django.urls import path

from mailapp.views import send_mail

urlpatterns =[
    path('send-mail', send_mail, name='send_mail'),

]