import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from fitnessTracker.models import Meal, Workout, Exercise, CalanderDate,UserProfile
from fitnessTracker.forms import MealForm, WorkoutForm, ExerciseForm, CalanderDateForm, RegistrationForm, UserProfileForm
from registration.backends.default.views import RegistrationView
from django.contrib.auth.views import PasswordChangeView
from django.views.decorators.csrf import csrf_exempt

class MyRegistrationView(RegistrationView):
    form_class = RegistrationForm

    def register(self, form):
        new_user = form.save(commit=True)
        new_user.is_active = True
        new_user.save()
        return new_user

    def get_success_url(self, user=None):
        return '/accounts/login/'

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('auth_login') 

@login_required
def add_to_favourite(request, workout_name_slug):
    fav_workout = Workout.objects.get(slug = workout_name_slug)
    cur_user = UserProfile.objects.get(user=request.user)
    if fav_workout in cur_user.favourites.all():
        cur_user.favourites.remove(fav_workout)
    else:
        cur_user.favourites.add(fav_workout)

    return redirect('fitnessTracker:show_workout', workout_name_slug=workout_name_slug)

def homepage(request):
    context_dict = {}

    if request.user.is_authenticated:
        context_dict['meals'] = Meal.objects.filter(user = request.user)
        logs = CalanderDate.objects.filter(user = request.user)
        context_dict['logs'] = logs
  
    context_dict['workouts'] = Workout.objects.all()
    return render(request, 'fitnessTracker/homepage.html', context=context_dict)

def show_workout(request, workout_name_slug):
    context_dict = {}
    try:
        workout = Workout.objects.get(slug=workout_name_slug)
        exercises = Exercise.objects.filter(workout=workout)
        context_dict['workout'] = workout
        context_dict['exercises']= exercises

        total= 0
        for exercise in exercises:
            total += 1

        context_dict['total'] = total

        user = request.user
        if user.is_authenticated:
            userProfile = UserProfile.objects.get(user = user)
            favourites = userProfile.favourites.all()
            isAFavourite = False
            for favourite in favourites:
                if favourite.name == workout.name:
                    isAFavourite= True
            context_dict['favourites'] = isAFavourite

        else:
            context_dict['favourites'] = False
    except Workout.DoesNotExist:
        context_dict['workout'] = None
        context_dict['exercises'] = None
        context_dict['total'] = None
    return render(request, 'fitnessTracker/workout.html', context=context_dict)

@login_required
def add_workout(request):
    form = WorkoutForm()

    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        form.save(commit=True)
        return redirect('fitnessTracker:homepage')
    else:
        print(form.errors)

    return render(request, 'fitnessTracker/add_workout.html', {'form': form})

@login_required
def add_meal(request):
    form = MealForm()
    
    if request.method == 'POST':
        form = MealForm(request.POST)

        if form.is_valid(): 
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect('fitnessTracker:homepage')
    else:
        print(form.errors)
    return render(request, 'fitnessTracker/add_meal.html', {'form': form})

@login_required
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
                form.save(commit=True)
                return redirect(reverse('fitnessTracker:show_workout',kwargs={'workout_name_slug': workout_name_slug}))

    else:
        print(form.errors)

    context_dict = {'form': form, 'workout': workout}
    return render(request, 'fitnessTracker/add_exercise.html', context=context_dict)

@login_required
def add_log(request):
    form = CalanderDateForm()

    if request.method == 'POST':
        form = CalanderDateForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            form.save_m2m()
            return redirect('fitnessTracker:homepage')
    else:
        print(form.errors)

    return render(request, 'fitnessTracker/add_log.html', {'form': form})

def send_home(request):
    return redirect(reverse('fitnessTracker:homepage'))

def catalogue(request):
    context_dict = {}
    temporary = Workout.objects.all()
    workout_by_exercise = {}
    for entry in temporary:
        workouts = workout_by_exercise.get(entry.exercise_type, [])
        workouts.append(entry)
        workout_by_exercise[entry.exercise_type] = workouts
    
    context_dict['workouts'] = workout_by_exercise
        
    return render(request, 'fitnessTracker/catalogue.html', context=context_dict)

@login_required
def tracker(request):
    context_dict={}
    if request.user.is_authenticated:
        logs = CalanderDate.objects.filter(user=request.user).order_by('year', 'month', 'day')

        xValues = ""
        yValues = ""

        for log in logs:
            xValues += (f"{log.day} {log.month} {log.year}, ") 
            count = 0
            for meal in log.meals.all():
                count += meal.calories
            yValues += f"{count} " 

        
        if logs != None :
            context_dict['newestLog'] = logs.last()

        else:
            context_dict['newestLog'] = None
        
        context_dict['xValue'] = xValues
        context_dict['yValue'] = yValues
        
    user = request.user
    userProfile = UserProfile.objects.get(user = user)
    goal = userProfile.goal
    context_dict['goal'] = goal
    if goal == "Lose weight":
        context_dict['exercises']  = Workout.objects.filter(exercise_type = "Cardio")
    elif goal == "Maintain weight":
        context_dict['exercises']  = Workout.objects.filter(exercise_type = "Balance")
    elif goal == "Gain weight":
        context_dict['exercises']  = Workout.objects.filter(exercise_type = "Strength")
    return render(request, 'fitnessTracker/tracker.html', context=context_dict)

@login_required
def profile(request):
    context_dict ={}
    user = request.user
    context_dict['user'] = user
    context_dict['userProfile'] = UserProfile.objects.get(user = user)
    context_dict['meals'] = Meal.objects.filter(user=request.user)
    return render(request, 'fitnessTracker/profile.html', context=context_dict)


def update_profile(request):
    if request.method == 'POST':
        try:
            user_profile = UserProfile.objects.get(user=request.user)

            user_profile.weight = request.POST.get('weight', user_profile.weight)
            user_profile.experience = request.POST.get('experience', user_profile.experience)
            user_profile.goal = request.POST.get('goal', user_profile.goal)
            user_profile.save()

            return JsonResponse({
                'status': 'success',
                'data': {
                    'weight': user_profile.weight,
                    'experience': user_profile.experience,
                    'goal': user_profile.goal,
                }
            })
        except UserProfile.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User profile not found.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def get_meal(request):
    meal_id = request.GET.get('meal_id')
    try:
        meal = Meal.objects.get(pk=meal_id, user=request.user)
        meal_data = {
            'name': meal.name,
            'calories': meal.calories,
            'protein': meal.protein,
            'fat': meal.fat,
            'carbohydrate': meal.carbohydrate,
            'description': meal.description
        }
        return JsonResponse(meal_data)
    except Meal.DoesNotExist:
        return JsonResponse({'error': 'Meal not found'}, status=404)
    

def update_meal(request):
    if request.method == 'POST':
        meal_id = request.POST.get('meal_id')
        if not meal_id:
            return JsonResponse({'status': 'error', 'message': 'Meal ID not found'}, status=400)
        try:
            meal = Meal.objects.get(pk=meal_id, user=request.user)
            meal.description = request.POST.get('description', meal.description)
            meal.save()
            return JsonResponse({
                'status': 'success',
                'data': meal.description,
            })
        except Meal.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Meal not found.'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)