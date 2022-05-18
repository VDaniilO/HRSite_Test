from django.shortcuts import render

from .models import *


def out_users(request):

    all_info = Personal.objects.all()
    context ={
        'all_info': all_info,
    }
    return render(request, template_name = 'MainApp/allusers.html', context=context)
