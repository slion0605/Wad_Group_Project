from django.contrib import admin
from fitnessTracker.models import Meal, Workout, Exercise, UserProfile

class WorkoutAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Meal)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(UserProfile)


