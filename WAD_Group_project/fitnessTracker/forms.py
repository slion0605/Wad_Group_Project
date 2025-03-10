from django import forms
from registration.forms import RegistrationForm
from fitnessTracker.models import Meal, Workout, Exercise, CalanderDate, User, UserProfile

class RegistrationForm(RegistrationForm):
    birth_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=UserProfile.GENDER_CHOICES, required=True)
    weight = forms.DecimalField(max_digits=5, decimal_places=2, required=True)
    height = forms.DecimalField(max_digits=5, decimal_places=2, required=True)
    goal = forms.ChoiceField(choices=UserProfile.GOAL_CHOICES, required=True)
    experience = forms.ChoiceField(choices=UserProfile.EXERCISE_CHOICES, required=False)

    class Meta:
        model = User 
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False) 
        user.set_password(self.cleaned_data["password1"]) 
        user.is_active = True
        if commit:
            user.save() 
            UserProfile.objects.create(
                user=user,
                birth_date=self.cleaned_data['birth_date'],
                gender=self.cleaned_data['gender'],
                weight=self.cleaned_data['weight'],
                height=self.cleaned_data['height'],
                goal=self.cleaned_data['goal'],
                experience=self.cleaned_data['experience']
            )
        return user

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

    day = forms.IntegerField(help_text="Day: ", min_value=1, max_value=31)
    month = forms.ChoiceField(help_text="Month: ", choices=MONTHS)
    year = forms.IntegerField(help_text= "Year: ", min_value=1900, max_value=2100)
    workouts = forms.ModelMultipleChoiceField( queryset=Workout.objects.all(),widget=forms.CheckboxSelectMultiple, required=True )
    meals = forms.ModelMultipleChoiceField( queryset=Meal.objects.all(),widget=forms.CheckboxSelectMultiple, required=True)

    class Meta:
        model = CalanderDate
        fields = ('day', 'month','year', 'workouts', 'meals')

