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

    beginner_chest = [
        {'name': 'Smith Machine Incline Press', 'sets': 3, 'reps': 15},
        {'name': 'Dumbbell Flat Press', 'sets': 2, 'reps': 10},
        {'name': 'Flat Bench Dumbbell Flys', 'sets': 2, 'reps': 10}
    ]

    superhuman_chest = [
        {'name': 'Incline Bench Press', 'sets': 6, 'reps': 5},
        {'name': 'Low Incline Dumbbell Fly', 'sets': 3, 'reps': 6},
        {'name': 'Weighted Dip', 'sets': 3, 'reps': 10},
        {'name': 'Flat Bench Cable Fly', 'sets': 3, 'reps': 10}
    ]

    bench_press_strength = [
        {'name': 'Bench Press', 'sets': 4, 'reps': 4},
        {'name': 'Close Grip Bench Press', 'sets': 3, 'reps': 8},
        {'name': 'Incline Dumbbell Bench Press', 'sets': 3, 'reps': 12},
        {'name': 'Dumbbell Flys', 'sets': 5, 'reps': 10}
    ]

    big_arm = [
        {'name': 'Barbell Curl', 'sets': 5, 'reps': 8},
        {'name': 'Incline Dumbbell Curl', 'sets': 5, 'reps': 8},
        {'name': 'Close Grip Bench Press', 'sets': 5, 'reps': 8},
        {'name': 'Dumbbell Flys', 'sets': 5, 'reps': 10}
    ]

    arm_ageddon = [
        {'name': 'Standing Barbell Curl', 'sets': 2, 'reps': 6},
        {'name': 'Barbell Preacher Curl', 'sets': 2, 'reps': 7},
        {'name': 'Cable Rope Hammer Curl', 'sets': 2, 'reps': 21}
    ]

    blast_pump_arm = [
        {'name': 'Standing Barbell Curl', 'sets': 6, 'reps': 10},
        {'name': 'Alternate Seated Dumbbell Curl', 'sets': 6, 'reps': 10}
    ]

    beginner_tricep = [
        {'name': 'Close grip bench press', 'sets': 3, 'reps': 15},
        {'name': 'Straight bar push downs', 'sets': 2, 'reps': 10},
        {'name': 'Close grip push ups', 'sets': 1, 'reps': 10}
    ]

    titanic_tricep_builder = [
        {'name': 'Close grip bench press', 'sets': 3, 'reps': 10},
        {'name': 'Tricep Dips (Weighted, if possible)', 'sets': 3, 'reps': 10},
        {'name': 'EZ Bar Skull crusher', 'sets': 1, 'reps': 10},
        {'name': 'French Press', 'sets': 3, 'reps': 10}
    ]

    power_muscle_burn_tricep = [
        {'name': 'Close grip bench press', 'sets': 4, 'reps': 3},
        {'name': 'EZ Bar Skull crusher', 'sets': 2, 'reps': 6},
        {'name': 'Seated French Press', 'sets': 2, 'reps': 12},
        {'name': 'Cable Tricep Extension', 'sets': 1, 'reps': 40}
    ]

    coconut_shoulders = [
        {'name': 'Military Press', 'sets': 3, 'reps': 8},
        {'name': 'Seated Dumbbell Press', 'sets': 3, 'reps': 10},
        {'name': 'Seated Dumbbell Lateral Raise', 'sets': 3, 'reps': 12},
        {'name': 'Dumbbell Reverse Fly', 'sets': 3, 'reps': 12}
    ]

    beginner_shoulder = [
        {'name': 'Seated Dumbbell Press', 'sets': 3, 'reps': 15},
        {'name': 'Dumbbell Lateral Raise', 'sets': 2, 'reps': 12},
        {'name': 'Dumbbell Reverse Fly', 'sets': 2, 'reps': 12},
        {'name': 'Upright Row', 'sets': 2, 'reps': 10}
    ]

    super_shoulder = [
        {'name': 'Seated Rack Barbell Press', 'sets': 5, 'reps': 5},
        {'name': 'Seated Lateral Raise', 'sets': 4, 'reps': 10},
        {'name': 'Cable Face Pull', 'sets': 3, 'reps': 15},
        {'name': 'Alternated Machine Shoulder Press', 'sets': 4, 'reps': 12},
        {'name': 'Machine Shrug', 'sets': 3, 'reps': 15}
    ]

    beginner_forearm = [
        {'name': 'Reverse wrist curl', 'sets': 1, 'reps': 12},
        {'name': 'Wrist curl', 'sets': 1, 'reps': 12}
    ]

    big_forearm = [
        {'name': 'Dumbbell Wrist Flexion', 'sets': 2, 'reps': 12},
        {'name': 'Dumbbell Wrist Extension', 'sets': 2, 'reps': 12}
    ]

    power_forearm = [
        {'name': 'Dumbbell Wrist Flexion', 'sets': 3, 'reps': 8},
        {'name': 'Dumbbell Wrist Extension', 'sets': 3, 'reps': 8},
        {'name': 'Dumbbell Reverse Curl', 'sets': 2, 'reps': 12},
        {'name': 'Hammer Curl', 'sets': 2, 'reps': 10}
    ]

    grow_your_back = [
        {'name': 'Barbell Row', 'sets': 5, 'reps': 5},
        {'name': 'One Arm Dumbbell Row', 'sets': 3, 'reps': 8},
        {'name': 'Wide Grip Lat Pulldown', 'sets': 3, 'reps': 10},
        {'name': 'High Machine Seated Row', 'sets': 3, 'reps': 12}
    ]
    
    heavy_high_volume_back = [
        {'name': 'Deadlift', 'sets': 5, 'reps': 3},
        {'name': 'Rack Pulls', 'sets': 5, 'reps': 3},
        {'name': 'T-bar Row', 'sets': 5, 'reps': 10},
        {'name': 'Standing Dumbbell Row', 'sets': 3, 'reps': 5},
        {'name': 'Reverse Hyperextension', 'sets': 3, 'reps': 10}
    ]

    beginner_back_workout = [
        {'name': 'Front lat pulldown', 'sets': 3, 'reps': 15},
        {'name': 'Seated rows', 'sets': 2, 'reps': 10},
        {'name': 'One arm dumbbell row', 'sets': 2, 'reps': 10}
    ]

    beginner_leg_workout = [
        {'name': 'Leg press', 'sets': 3, 'reps': 15},
        {'name': 'Leg extension', 'sets': 2, 'reps': 10},
        {'name': 'Leg curl', 'sets': 2, 'reps': 10},
        {'name': 'Seated calf raise', 'sets': 2, 'reps': 10}
    ]

    bigger_quads = [
        {'name': 'Barbell Hack Squat', 'sets': 5, 'reps': 5},
        {'name': 'Leg Press', 'sets': 5, 'reps': 5},
        {'name': 'Leg Curl', 'sets': 5, 'reps': 5},
        {'name': 'Seated Calf Raises', 'sets': 25, 'reps': 5}
    ]

    absolute_leg_carnage = [
        {'name': 'Hack Squats', 'sets': 4, 'reps': 5},
        {'name': 'Leg Press', 'sets': 3, 'reps': 20},
        {'name': 'Leg Extensions', 'sets': 2, 'reps': 9},
        {'name': 'Lying Leg Curl', 'sets': 2, 'reps': 6},
        {'name': 'Stiff Leg Deadlift', 'sets': 3, 'reps': 20},
        {'name': 'Seated Leg Curl', 'sets': 2, 'reps': 7}
    ]

    core_conditioning = [
        {'name': 'Sit Up', 'sets': 2, 'reps': 15},
        {'name': 'Alternate Straight Leg Lower', 'sets': 2, 'reps': 15},
        {'name': 'Side Plank', 'sets': 2, 'reps': 15},
        {'name': 'Plank to Hip Raise', 'sets': 2, 'reps': 15},
        {'name': 'Stomach Vacuum', 'sets': 2, 'reps': 15}
    ]

    increase_ab_size = [
        {'name': 'Cable crunch', 'sets': 3, 'reps': 12},
        {'name': 'Weighted leg raise', 'sets': 3, 'reps': 10},
        {'name': 'Weighted exercise ball crunch', 'sets': 3, 'reps': 12}
    ]

    beginner_core_strength = [
        {'name': 'DB Crunch', 'sets': 1, 'reps': 10},
        {'name': 'DB Pullovers', 'sets': 1, 'reps': 20},
        {'name': 'Plate Arches', 'sets': 2, 'reps': 12},
        {'name': 'Side Bridge', 'sets': 1, 'reps': 20}
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
        
        'Beginner Chest Workout': {'exercise_type': Workout.CHEST, 'duration': 30, 'exercises': beginner_chest, 'video_url': ""},
        'Superhuman Chest': {'exercise_type': Workout.CHEST, 'duration': 45, 'exercises': superhuman_chest, 'video_url': ""},
        'Bench Press Strength': {'exercise_type': Workout.CHEST, 'duration': 60, 'exercises': bench_press_strength, 'video_url': ""},

        'Big Arm': {'exercise_type': Workout.BICEP, 'duration': 60, 'exercises': big_arm, 'video_url': ""},
        'Arm Ageddon': {'exercise_type': Workout.BICEP, 'duration': 45, 'exercises': arm_ageddon, 'video_url': ""},
        'Blast And Pump Arm': {'exercise_type': Workout.BICEP, 'duration': 30, 'exercises': blast_pump_arm, 'video_url': ""},

        'Beginner Tricep': {'exercise_type': Workout.TRICEP, 'duration': 15, 'exercises': beginner_tricep, 'video_url': ""},
        'Titanic Tricep Builder': {'exercise_type': Workout.TRICEP, 'duration': 30, 'exercises': titanic_tricep_builder, 'video_url': ""},
        'Power Muscle Burn Tricep': {'exercise_type': Workout.TRICEP, 'duration': 20, 'exercises': power_muscle_burn_tricep, 'video_url': ""},

        'Coconut Shoulders': {'exercise_type': Workout.SHOULDER, 'duration': 30, 'exercises': coconut_shoulders, 'video_url': ""},
        'Beginner Shoulder': {'exercise_type': Workout.SHOULDER, 'duration': 20, 'exercises': beginner_shoulder, 'video_url': ""},
        'Super Shoulder': {'exercise_type': Workout.SHOULDER, 'duration': 60, 'exercises': super_shoulder, 'video_url': ""},

        'Beginner Forearm': {'exercise_type': Workout.FOREARM, 'duration': 5, 'exercises': beginner_forearm, 'video_url': ""},
        'Big Forearms': {'exercise_type': Workout.FOREARM, 'duration': 10, 'exercises': big_forearm, 'video_url': ""},
        'Power Forearms': {'exercise_type': Workout.FOREARM, 'duration': 20, 'exercises': power_forearm, 'video_url': ""},

        'Grow Your Back': {'exercise_type': Workout.BACK, 'duration': 45, 'exercises': grow_your_back, 'video_url': ""},
        'Heavy High Volume Back': {'exercise_type': Workout.BACK, 'duration': 60, 'exercises': heavy_high_volume_back, 'video_url': ""},
        'Beginner Back Workout': {'exercise_type': Workout.BACK, 'duration': 15, 'exercises': beginner_back_workout, 'video_url': ""},

        'Beginner Leg Workout': {'exercise_type': Workout.LEGS, 'duration': 25, 'exercises': beginner_leg_workout, 'video_url': ""},
        'Bigger Quads': {'exercise_type': Workout.LEGS, 'duration': 60, 'exercises': bigger_quads, 'video_url': ""},
        'Absolute Leg Carnage': {'exercise_type': Workout.LEGS, 'duration': 45, 'exercises': absolute_leg_carnage, 'video_url': ""},

        'Core Conditioning': {'exercise_type': Workout.ABS, 'duration': 15, 'exercises': core_conditioning, 'video_url': ""},
        'Increase Ab Size': {'exercise_type': Workout.ABS, 'duration': 15, 'exercises': increase_ab_size, 'video_url': ""},
        'Beginner Core Strength': {'exercise_type': Workout.ABS, 'duration': 15, 'exercises': beginner_core_strength, 'video_url': ""},
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
