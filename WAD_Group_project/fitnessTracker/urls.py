from django.urls import path
from fitnessTracker import views

app_name = 'fitnessTracker'

urlpatterns = [
path('homepage/', views.homepage, name='homepage'),
path('', views.homepage, name='homepage'),
path('login/', views.user_login, name='login'),
path('register/', views.register, name='register'),
path('catalogue/', views.catalogue, name='catalogue'),
path('workout/<slug:workout_name_slug>/', views.show_workout, name='show_workout'),
path('add_workout/', views.add_workout, name='add_workout'),
path('add_meal/', views.add_meal, name='add_meal'),
path('workout/<slug:workout_name_slug>/add_exercise/', views.add_exercise, name='add_exercise'),
path('tracker/', views.tracker, name='tracker'),
path('logout/', views.user_logout, name='logout'),
path('profile/', views.profile, name='profile'),
path('add_log/', views.add_log, name='add_log'),
]
  