from django.contrib import admin
from fitnessTracker.models import Meal, Workout, Exercise, UserProfile
admin.site.register(Meal)
admin.site.register(Workout)
admin.site.register(UserProfile)
