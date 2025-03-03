from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def homepage(request):
    pass

def show_workout(request):
    pass

def add_workout(request):
    pass

def add_meal(request):
    pass

def register(request):
    pass

def user_login(request):
    pass

@login_required
def user_logout(request):
    pass

def send_home(request):
    pass

def catalogue(request):
    pass

def tracker(request):
    pass


