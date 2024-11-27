from india.views import *
from django.urls import path

urlpatterns=[
    path('topcar/',topcar,name='topcar'),
    path('sectopcar/',sectopcar,name='sectopcar'),
]