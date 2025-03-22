import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WAD_Group_project.settings')
django.setup()

from fitnessTracker.models import Workout, Exercise

def populate():
    cardio_exercises = [
        {'name': 'Running', 'sets': 10, 'reps': 5},
        {'name': 'Burpees', 'sets': 6, 'reps': 5},
        {'name': 'Skipping', 'sets': 7, 'reps': 4}
    ]

    cardio_exercises_2 = [
        {'name': 'Jumping', 'sets': 10, 'reps': 5},
        {'name': 'Jumping Jacks', 'sets': 6, 'reps': 5},
        {'name': 'Skipping', 'sets': 7, 'reps': 4}
    ]

    cardio_exercises_3 = [
        {'name': 'Crunches', 'sets': 10, 'reps': 5},
        {'name': 'Burpees', 'sets': 6, 'reps': 5},
        {'name': 'Running', 'sets': 7, 'reps': 4}
    ]
    
    strength_exercises = [
        {'name': 'Arm Curls', 'sets': 1, 'reps': 52},
        {'name': 'Squats', 'sets': 13, 'reps': 10},
        {'name': 'Deadlifts', 'sets': 5, 'reps': 8}
    ]

    strength_exercises_2 = [
        {'name': 'Curls', 'sets': 13, 'reps': 5},
        {'name': 'Squats', 'sets': 23, 'reps': 12},
        {'name': 'Deadlifts', 'sets': 5, 'reps': 3}
    ]

    strength_exercises_3 = [
        {'name': 'Leg extensions', 'sets': 10, 'reps': 5},
        {'name': 'Jump Squats', 'sets': 13, 'reps': 10},
        {'name': 'Arm curls', 'sets': 3, 'reps': 6}
    ]
    
    flexibility_exercises = [
        {'name': 'Stretching', 'sets': 3, 'reps': 15},
        {'name': 'Yoga Poses', 'sets': 4, 'reps': 10}
    ]

    flexibility_exercises_2 = [
        {'name': 'Tree pose', 'sets': 3, 'reps': 1},
        {'name': 'Streches', 'sets': 42, 'reps': 12}
    ]
    
    flexibility_exercises_3 = [
        {'name': 'Toe Touches', 'sets': 30 , 'reps': 1},
        {'name': 'Arm Curls', 'sets': 4, 'reps': 10}
    ]

    balance_exercises = [
        {'name': 'One-Leg Stand', 'sets': 3, 'reps': 20},
        {'name': 'Heel-to-Toe Walk', 'sets': 3, 'reps': 15}
    ]

    balance_exercises_2 = [
        {'name': 'Jumping Jacks', 'sets': 5, 'reps': 7},
        {'name': 'Lunges', 'sets': 13, 'reps': 5}
    ]

    balance_exercises_3 = [
        {'name': 'Jump on one leg', 'sets': 5, 'reps': 2},
        {'name': 'Heel-to-Toe Walk', 'sets': 13, 'reps': 15}
    ]
    
    workouts = {
        'Cardio Blast': {'exercise_type': Workout.CARDIO, 'duration': 30, 'exercises': cardio_exercises,'video_url':"https://www.youtube.com/watch?v=a-V4Or5xyis"},
        'Get Cardio': {'exercise_type': Workout.CARDIO, 'duration': 120, 'exercises': cardio_exercises_2, 'video_url':"https://www.youtube.com/watch?v=kZDvg92tTMc"},
        'Cardio Quick': {'exercise_type': Workout.CARDIO, 'duration': 60, 'exercises': cardio_exercises_3, 'video_url':"https://www.youtube.com/watch?v=ImI63BUUPwU"},
        'Expert Strength Trainer': {'exercise_type': Workout.STRENGTH, 'duration': 40, 'exercises': strength_exercises, 'video_url':"https://www.youtube.com/watch?v=36BuhRO3zng"},
        'Get Strong': {'exercise_type': Workout.STRENGTH, 'duration': 40, 'exercises': strength_exercises_2, 'video_url':"https://www.youtube.com/watch?v=LdFgFco_8p8"},
        'Athlete Strength': {'exercise_type': Workout.STRENGTH, 'duration': 95, 'exercises': strength_exercises_3, 'video_url':"https://www.youtube.com/watch?v=Cl7E5GoFv6k&t=311s"},
        'Flexibility Flow': {'exercise_type': Workout.FLEXIBILITY, 'duration': 21, 'exercises': flexibility_exercises,'video_url':"https://www.youtube.com/watch?v=i6TzP2COtow"},
        'Flexibility Upgrades': {'exercise_type': Workout.FLEXIBILITY, 'duration': 20, 'exercises': flexibility_exercises_2, 'video_url':"https://www.youtube.com/watch?v=itJE4neqDJw"},
        'Get Flex': {'exercise_type': Workout.FLEXIBILITY, 'duration': 30, 'exercises': flexibility_exercises_3, 'video_url':"https://www.youtube.com/watch?v=t2jel6q1GRk"},
        'Balance Boost': {'exercise_type': Workout.BALANCE, 'duration': 100, 'exercises': balance_exercises, 'video_url':"https://www.youtube.com/watch?v=w3XJEcRpKhI"},
        'Balance Better': {'exercise_type': Workout.BALANCE, 'duration': 105, 'exercises': balance_exercises_2,'video_url':"https://www.youtube.com/watch?v=s6I78a_szkU"},
        'Gymnast Balance': {'exercise_type': Workout.BALANCE, 'duration': 95, 'exercises': balance_exercises_3, 'video_url':"https://www.youtube.com/watch?v=uth_9K3EmDI"},
    }

    for workout_name, workout_data in workouts.items():
        workout = add_workout(workout_name, workout_data['exercise_type'], workout_data['duration'],workout_data['video_url'])
        for exercise_data in workout_data['exercises']:
            exercise = add_exercise(exercise_data['name'], exercise_data['sets'], exercise_data['reps'])
            exercise.workout.add(workout)

    print("Database population complete!")

def add_workout(name, exercise_type, duration, video_url):
    workout, created = Workout.objects.get_or_create(name=name, exercise_type=exercise_type, duration=duration, video_url=video_url)
    return workout

def add_exercise(name, sets, reps):
    exercise, created = Exercise.objects.get_or_create(name=name, sets=sets, reps=reps)
    return exercise

if __name__ == '__main__':
    print('Starting fitnessTracker population script...')
    populate()
