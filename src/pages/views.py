from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def about_view(request, *args, **kwargs):
    about_info = {
        "text": "admin username",
        "my_number": 123,
        "my_list": [43, 12, 5]
    }
    return render(request, 'about.html', about_info)


def social_view(request, *args, **kwargs):
    return render(request, 'social.html', {})