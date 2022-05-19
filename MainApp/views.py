from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import *
from .forms import AbilityForm, CategoriesForm, AddLoginForm


def user_profile(request, usr_login):
    user_info = get_object_or_404(Personal, login = usr_login)
    context = {
        'user_info': user_info,
    }
    return render(request, template_name = 'MainApp/profile.html', context = context)


def out_users(request):
    all_info = Personal.objects.all()
    all_ability = Ability.objects.all()
    context = {
        'all_info': all_info,
        'all_ability': all_ability,
    }
    return render(request, template_name = 'MainApp/allusers.html', context = context)


def usr_register(request):
    if request.method == 'POST':
        form_usr_db = AddLoginForm(request.POST)
        if form_usr_db.is_valid():
            Personal.objects.create(**form_usr_db.cleaned_data)
            messages.success(request, 'You registrated!!!!')
            return redirect('login')
        else:
            messages.error(request, 'Error')
    else:
        form_usr_db = AddLoginForm()
    return render(request, 'MainApp/register.html', { 'form_usr_db': form_usr_db })


def usr_login(request):
    login = request.POST.get('login')
    password = request.POST.get('password')
    user = authenticate(request, login = login, password = password)
    if user is not None:
        login(request, user)
        return redirect(f'profile/{login}')

    return render(request, f'MainApp/login.html')


def add_ability(request):
        if request.method == 'POST':
            form_ab = AbilityForm(request.POST)
            form_cate = CategoriesForm(request.POST)
            if form_ab.is_valid():
                Ability.objects.create(**form_ab.cleaned_data)
                return redirect('all_users')
            elif form_cate.is_valid():
                Categories.objects.create(**form_cate.cleaned_data)
                return redirect('all_users')
        else:
            form_ab = AbilityForm()
            form_cate = CategoriesForm()

        return render(request, 'MainApp/add_ability.html', { 'form_ab': form_ab, 'form_cate': form_cate })
