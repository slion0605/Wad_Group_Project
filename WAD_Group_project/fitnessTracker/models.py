from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=128)
    calories = models.IntegerField(default=10)
    fat = models.IntegerField(default=4)
    protein = models.IntegerField(default=4)
    carbohydrate = models.IntegerField(default=4)

    class Meta:
        verbose_name_plural = 'Meals'




class Workout(models.Model):
    name = models.CharField(max_length=128)
    Exercises = models.IntegerField(default=10)


    class Meta:
        verbose_name_plural = 'Workouts'

class Exercise(models.Model):
    name = models.CharField(max_length=128)
    sets = models.IntegerField(default=10)
    reps = models.IntegerField(default=10)

    class Meta:
        verbose_name_plural = 'Exercies'

class UserProfile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
