from django import forms

from .models import *


class AddLoginForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields  = ['name', 'login', 'password']

class AbilityForm(forms.ModelForm):

    class Meta:
        model = Ability
        fields = ['name', 'category']


class CategoriesForm(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ['name']

# class PersonalAbilityAdd(forms.ModelForm):
#
#     class Meta:
#         model = Personal
#         fields = ['login', 'name', 'skills']
