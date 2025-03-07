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
from fitnessTracker.models import Meal, Workout, Exercise, CalanderDate
from fitnessTracker.forms import MealForm, WorkoutForm, ExerciseForm, CalanderDateForm

def homepage(request):
    context_dict = {}
    context_dict['meals'] = Meal.objects.all()
    context_dict['workouts'] = Workout.objects.all()
    return render(request, 'fitnessTracker/homepage.html', context=context_dict)

def show_workout(request, workout_name_slug):
    context_dict = {}
    try:
        workout = Workout.objects.get(slug=workout_name_slug)
        exercises = Exercise.objects.filter(workout=workout)
        context_dict['workout'] = workout
        context_dict['exercises']= exercises
    except Workout.DoesNotExist:
        context_dict['workout'] = None
        context_dict['exercises'] = None
    return render(request, 'fitnessTracker/workout.html', context=context_dict)


def add_workout(request):
    form = WorkoutForm

    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        form.save(commit=True)
        return redirect('fitnessTracker:homepage')
    else:
        print(form.errors)

    return render(request, 'fitnessTracker/add_workout.html', {'form': form})


def add_meal(request):
    form = MealForm()

    if request.method == 'POST':
        form = MealForm(request.POST)

        if form.is_valid(): 
            form.save(commit=True)
            return redirect('fitnessTracker:homepage')
    else:
        print(form.errors)
    return render(request, 'fitnessTracker/add_meal.html', {'form': form})

def add_exercise(request, workout_name_slug):
    try:
        workout = Workout.objects.get(slug=workout_name_slug)
    except Workout.DoesNotExist:
        workout = None

    if workout is None:
        return redirect('fitnessTracker:homepage')
    
    form = ExerciseForm()

    if request.method == 'POST':
        form = ExerciseForm(request.POST)

        if form.is_valid(): 
            if workout:
                exercise = form.save(commit=True)
                return redirect(reverse('fitnessTracker:show_workout',kwargs={'workout_name_slug': workout_name_slug}))

    else:
        print(form.errors)

    context_dict = {'form': form, 'workout': workout}
    return render(request, 'fitnessTracker/add_exercise.html', context=context_dict)

def add_log(request):
    form = CalanderDateForm()

    if request.method == 'POST':
        form = CalanderDateForm(request.POST)
        form.save(commit=True)
        return redirect('fitnessTracker:homepage')
    else:
        print(form.errors)

    return render(request, 'fitnessTracker/add_log.html', {'form': form})


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
    context_dict = {}
    context_dict['workouts'] = Workout.objects.all()
    return render(request, 'fitnessTracker/catalogue.html', context=context_dict)

def tracker(request):
    return render(request, 'fitnessTracker/tracker.html')

def profile(request):
    return render(request, 'fitnessTracker/profile.html')


