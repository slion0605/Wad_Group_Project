import time
from django.db import models
from django.contrib.auth.models import User  # Use Django's built-in User model
from django.template.defaultfilters import slugify

    

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    calories = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    carbohydrate = models.IntegerField(default=0)
    description = models.TextField(blank=True)


    class Meta:
        verbose_name_plural = 'Meals'

    def __str__(self):
        return self.name


class Workout(models.Model):
    CARDIO = "Cardio"
    STRENGTH = "Strength"
    FLEXIBILITY = "Flexibility"
    BALANCE = "Balance"
    CHEST = "Chest"
    BICEP = "Bicep"
    TRICEP = "Tricep"
    SHOULDER = "Shoulder"
    FOREARM = "Forearm"
    BACK = "Back"
    LEGS = "Legs"
    ABS = "Abs"

    EXERCISE_CHOICES = [
        (CARDIO, "Cardio"),
        (STRENGTH, "Strength"),
        (FLEXIBILITY, "Flexibility"),
        (BALANCE, "Balance"),
        (CHEST, "Chest"),
        (BICEP, "Bicep"),
        (TRICEP, "Tricep"),
        (SHOULDER, "Shoulder"),
        (FOREARM, "Forearm"),
        (BACK, "Back"),
        (LEGS, "Legs"),
        (ABS, "Abs"),
    ]

    name = models.CharField(max_length=128)
    exercise_type = models.CharField(max_length=20, choices=EXERCISE_CHOICES, default=CARDIO) 
    duration = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    video_url = models.URLField(max_length=200, blank=True, null=True)

    def get_embed_url(self):
        video_id = self.video_url.split('v=')[-1]
        return f"https://www.youtube.com/embed/{video_id}"
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Workout, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Workouts'
    
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    EXPERT = "Expert"

    EXERCISE_CHOICES = [ 
        (BEGINNER, "Beginner"),
        (INTERMEDIATE, "Intermediate"),
        (EXPERT, "Expert")
    ]

    MALE = "Male"
    FEMALE = "Female"

    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female")
    ]

    LOSE_WEIGHT = "Lose weight"
    MAINTAIN_WEIGHT = "Maintain weight"
    GAIN_WEIGHT = "Gain weight"

    GOAL_CHOICES = [
       (LOSE_WEIGHT, "Lose weight"),
       (MAINTAIN_WEIGHT, "Maintain weight"),
       (GAIN_WEIGHT, "Gain weight")
    ]

    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    experience = models.CharField(max_length=20, choices=EXERCISE_CHOICES, default=BEGINNER) 
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, null=True, blank=True)
    favourites = models.ManyToManyField(Workout)
    def __str__(self):
        return self.user.username

class Exercise(models.Model):
    
    name = models.CharField(max_length=128)
    sets = models.IntegerField(default=10)
    reps = models.IntegerField(default=10)

    workout = models.ManyToManyField(Workout)

    
    class Meta:
        verbose_name_plural = 'Exercises'

    def __str__(self):
        return self.name

class CalanderDate(models.Model):

    MONTHS = [
        ("January", "January"),
        ("February", "February"),
        ("March", "March"),
        ("April", "April"),
        ("May", "May"),
        ("June", "June"),
        ("July", "July"),
        ("August", "August"),
        ("September", "September"),
        ("October", "October"),
        ("November", "November"),
        ("December", "December")
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meals = models.ManyToManyField(Meal)
    workouts = models.ManyToManyField(Workout)
    month =  models.CharField(max_length=20, choices=MONTHS)
    year = models.IntegerField(default=2025)
    day = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.day} {self.month} {self.year}"
