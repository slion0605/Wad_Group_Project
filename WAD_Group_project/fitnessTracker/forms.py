from django import forms
from fitnessTracker.models import Meal, Workout, Exercise

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

    
    name = forms.CharField()
    exercise_type = forms.ChoiceField(choices=EXERCISE_CHOICES)
    duration = forms.IntegerField()
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Workout
        fields = ('name', 'exercise_type','duration')