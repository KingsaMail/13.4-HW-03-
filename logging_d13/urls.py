from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('index_2', index_2, name='index_2'),
]