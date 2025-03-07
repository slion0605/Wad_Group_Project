from django.contrib import admin
from fitnessTracker.models import Meal, Workout, Exercise, UserProfile, CalanderDate

class WorkoutAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Meal)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(UserProfile)
admin.site.register(Exercise)
admin.site.register(CalanderDate)

