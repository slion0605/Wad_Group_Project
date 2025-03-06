from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse

def homepage(request):
    return render(request, 'fitnessTracker/homepage.html')

def show_workout(request):
    return render(request, 'fitnessTracker/workout.html')

@login_required
def add_workout(request):
    return render(request, 'fitnessTracker/addWorkout.html')

@login_required
def add_meal(request):
    return render(request, 'fitnessTracker/addMeal.html')

def register(request):
    return render(request, 'fitnessTracker/register.html')

def user_login(request):
    return render(request, 'fitnessTracker/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('fitnessTracker:homepage'))

def send_home(request):
    return redirect(reverse('fitnessTracker:homepage'))

def catalogue(request):
    return render(request, 'fitnessTracker/catalogue.html')

def tracker(request):
    return render(request, 'fitnessTracker/tracker.html')

def profile(request):
    return render(request, 'fitnessTracker/profile.html')


