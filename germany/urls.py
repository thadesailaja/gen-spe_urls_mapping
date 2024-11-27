from germany.views import *
from django.urls import path

urlpatterns=[
    path('topcar/',topcar,name='topcar'),
]