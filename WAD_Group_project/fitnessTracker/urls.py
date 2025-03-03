from django.urls import path
from fitnessTracker import views

app_name = 'fitnessTracker'

urlpatterns = [
path('', views.homepage, name='homepage'),
path('login/', views.user_login, name='login'),
path('register/', views.register, name='register'),
path('catalogue/', views.catalogue, name='catalogue'),
path('catalogue/<muscle_group>/', views.show_workout, name='show_workout'),
path('catalogue/<muscle_group>/<workout_name>', views.show_workout, name='show_workout'),
path('add_workout/', views.add_workout, name='add_workout'),
path('add_workout/', views.add_meal, name='add_meal'),
path('tracker/', views.tracker, name='tracker'),
path('logout/', views.user_logout, name='logout'),
]
  