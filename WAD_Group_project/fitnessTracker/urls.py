from django.urls import path
from fitnessTracker import views

app_name = 'fitnessTracker'

urlpatterns = [
path('homepage/', views.homepage, name='homepage'),
path('', views.homepage, name='homepage'),
path('catalogue/', views.catalogue, name='catalogue'),
path('catalogue/<slug:workout_name_slug>/', views.show_workout, name='show_workout'),
path('workout/<slug:workout_name_slug>/', views.show_workout, name='show_workout'),
path('workout/<slug:workout_name_slug>/add-to-favourites/', views.add_to_favourite, name='add_to_favourites'),
path('add_workout/', views.add_workout, name='add_workout'),
path('add_meal/', views.add_meal, name='add_meal'),
path('workout/<slug:workout_name_slug>/add_exercise/', views.add_exercise, name='add_exercise'),
path('tracker/', views.tracker, name='tracker'),
path('profile/', views.profile, name='profile'),
path('add_log/', views.add_log, name='add_log'),
path('update_profile/', views.update_profile, name='update_profile'),
path('get_meal/', views.get_meal, name='get_meal'),
path('update_meal/', views.update_meal, name='update_meal'),
path('search/', views.search_results, name='search'),
]
  