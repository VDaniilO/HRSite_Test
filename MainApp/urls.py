from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    path('', out_users, name='all_users'),
    path('profile/<str:usr_login>', user_profile, name='profile'),
    path('add_ability/', add_ability, name='add_ability'),
#    path('add_ability/', add_categories),
    path('register/', usr_register, name='register'),
    path('login/', usr_login, name='login'),
]
