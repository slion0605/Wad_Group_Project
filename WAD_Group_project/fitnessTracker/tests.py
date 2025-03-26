from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Meal, Workout
from .forms import RegistrationForm, MealForm, WorkoutForm

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            birth_date='1990-01-01',
            gender='Male',
            weight=70.5,
            height=175.0,
            goal='Lose weight',
            experience='Beginner'
        )

    def test_user_profile_creation(self):
        self.assertEqual(self.user_profile.user.username, 'testuser')
        self.assertEqual(self.user_profile.birth_date, '1990-01-01')
        self.assertEqual(self.user_profile.gender, 'Male')
        self.assertEqual(self.user_profile.weight, 70.5)
        self.assertEqual(self.user_profile.height, 175.0)
        self.assertEqual(self.user_profile.goal, 'Lose weight')
        self.assertEqual(self.user_profile.experience, 'Beginner')

    def test_user_profile_str(self):
        self.assertEqual(str(self.user_profile), 'testuser')

class MealModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.meal = Meal.objects.create(
            user=self.user,
            name='Test Meal',
            calories=500,
            fat=20,
            protein=30,
            carbohydrate=50
        )

    def test_meal_creation(self):
        self.assertEqual(self.meal.user.username, 'testuser')
        self.assertEqual(self.meal.name, 'Test Meal')
        self.assertEqual(self.meal.calories, 500)
        self.assertEqual(self.meal.fat, 20)
        self.assertEqual(self.meal.protein, 30)
        self.assertEqual(self.meal.carbohydrate, 50)

    def test_meal_str(self):
        self.assertEqual(str(self.meal), 'Test Meal')

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            exercise_type='Cardio',
            duration=60
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(self.workout.exercise_type, 'Cardio')
        self.assertEqual(self.workout.duration, 60)
        self.assertEqual(self.workout.slug, 'test-workout')

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')

    def test_workout_get_embed_url(self):
        self.workout.video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        self.assertEqual(self.workout.get_embed_url(), 'https://www.youtube.com/embed/dQw4w9WgXcQ')

class RegistrationFormTest(TestCase):
    def test_registration_form_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'birth_date': '1990-01-01',
            'gender': 'Male',
            'weight': 70.5,
            'height': 175.0,
            'goal': 'Lose weight',
            'experience': 'Beginner'
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'differentpass',
            'birth_date': '1990-01-01',
            'gender': 'Male',
            'weight': 70.5,
            'height': 175.0,
            'goal': 'Lose weight',
            'experience': 'Beginner'
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

class MealFormTest(TestCase):
    def test_meal_form_valid(self):
        form_data = {
            'name': 'Test Meal',
            'calories': 500,
            'fat': 20,
            'protein': 30,
            'carbohydrate': 50,
            'description': 'This is a test meal.'  # Add description field
        }
        form = MealForm(data=form_data)
        if not form.is_valid():
            print(form.errors)  # Print form errors for debugging
        self.assertTrue(form.is_valid())

    def test_meal_form_invalid(self):
        form_data = {
            'name': '',
            'calories': 500,
            'fat': 20,
            'protein': 30,
            'carbohydrate': 50,
            'description': 'This is a test meal.'  # Add description field
        }
        form = MealForm(data=form_data)
        self.assertFalse(form.is_valid())

class WorkoutFormTest(TestCase):
    def test_workout_form_valid(self):
        form_data = {
            'name': 'Test Workout',
            'exercise_type': 'Cardio',
            'duration': 60
        }
        form = WorkoutForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_workout_form_invalid(self):
        form_data = {
            'name': '',
            'exercise_type': 'Cardio',
            'duration': 60
        }
        form = WorkoutForm(data=form_data)
        self.assertFalse(form.is_valid())
