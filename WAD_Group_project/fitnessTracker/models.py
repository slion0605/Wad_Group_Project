import time
from django.db import models
from django.contrib.auth.models import User  # Use Django's built-in User model
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    # BEGINNER = "Beginner"
    # INTERMEDIATE = "Intermediate"
    # EXPERT = "Expert"

    # EXERCISE_CHOICES = [
    #     (BEGINNER, "Beginner"),
    #     (INTERMEDIATE, "Intermediate"),
    #     (EXPERT, "Expert")
        
    # ]
    
    # experience = models.CharField(max_length=20, choices=EXERCISE_CHOICES, default=BEGINNER) 
    # weight = models.IntegerField(default=10)
    # height = models.IntegerField(default=10)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Meal(models.Model):
    name = models.CharField(max_length=128)
    calories = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    carbohydrate = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = 'Meals'


class Workout(models.Model):
    CARDIO = "Cardio"
    STRENGTH = "Strength"
    FLEXIBILITY = "Flexibility"
    BALANCE = "Balance"

    EXERCISE_CHOICES = [
        (CARDIO, "Cardio"),
        (STRENGTH, "Strength"),
        (FLEXIBILITY, "Flexibility"),
        (BALANCE, "Balance"),
    ]

    name = models.CharField(max_length=128)
    exercise_type = models.CharField(max_length=20, choices=EXERCISE_CHOICES, default=CARDIO) 
    duration = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Workout, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Workouts'
    
    def __str__(self):
        return self.name


class Exercise(models.Model):
    
    name = models.CharField(max_length=128)
    sets = models.IntegerField(default=10)
    reps = models.IntegerField(default=10)

    workout = models.ManyToManyField(Workout)

    
    class Meta:
        verbose_name_plural = 'Exercises'

