# coding: utf-8
import json
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passowrd = request.POST.get('password')
        if username == '2022-01-11' and passowrd == '2022-11-05':
            # return redirect('/index')
            return render(request, 'heart.html')
        else:
            return render(request, 'error.html')

    return render(request, 'login_cool.html')


def index(request):
    return render(request, 'index.html')


def error_deel(request):
    # return render(request, 'login_cool.html')
    return redirect('/login_new')


def login_new(request):
    return render(request, 'login_cool_new.html')
