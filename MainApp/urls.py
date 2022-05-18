from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    path('all_users/', out_users, name = 'all_users')
]
