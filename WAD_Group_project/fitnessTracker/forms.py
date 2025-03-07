from django import forms
from fitnessTracker.models import Meal, Workout, Exercise, CalanderDate

class MealForm(forms.ModelForm):
    name = forms.CharField(help_text="Meal name: ")
    calories = forms.IntegerField(help_text="Calories: ")
    fat = forms.IntegerField(help_text="fat: ")
    protein = forms.IntegerField(help_text="protein: ")
    carbohydrate = forms.IntegerField(help_text="Carbohydrates: ")

    class Meta:
        model = Meal
        fields = ('name', 'calories', 'fat', 'protein', 'carbohydrate')


class ExerciseForm(forms.ModelForm):
    
    name = forms.CharField(help_text="Exercise name: ")
    sets = forms.IntegerField(help_text="Sets: ")
    reps = forms.IntegerField(help_text="Reps: ")
    workout = forms.ModelMultipleChoiceField( queryset=Workout.objects.all(),widget=forms.CheckboxSelectMultiple, required=True)

    class Meta:
        model = Exercise
        fields = ('name', 'sets', 'reps', 'workout')

class WorkoutForm(forms.ModelForm):
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

    
    name = forms.CharField(help_text="Name: ")
    exercise_type = forms.ChoiceField(choices=EXERCISE_CHOICES)
    duration = forms.IntegerField(help_text="Duration: ")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Workout
        fields = ('name', 'exercise_type','duration')

class CalanderDateForm(forms.ModelForm):
    MONTHS = [
        ("JANUARY", "January"),
        ("FEBRUARY", "February"),
        ("MARCH", "March"),
        ("APRIl", "April"),
        ("MAY", "May"),
        ("JUNE", "June"),
        ("JULY", "July"),
        ("AUGUST", "August"),
        ("SEPTEMBER", "September"),
        ("OCTOBER", "October"),
        ("NOVEMBER", "November"),
        ("DECEMBER", "December")
    ] 

    day = forms.IntegerField(help_text="Day: ", min_value=1, max_value=31)
    month = forms.ChoiceField(help_text="Month: ", choices=MONTHS)
    year = forms.IntegerField(help_text= "Year: ", min_value=1900, max_value=2100)
    workouts = forms.ModelMultipleChoiceField( queryset=Workout.objects.all(),widget=forms.CheckboxSelectMultiple, required=True )
    meals = forms.ModelMultipleChoiceField( queryset=Meal.objects.all(),widget=forms.CheckboxSelectMultiple, required=True)

    class Meta:
        model = CalanderDate
        fields = ('day', 'month','year', 'workouts', 'meals')

