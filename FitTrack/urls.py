from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fittrack'),
    path('create/', views.add_workout, name='create'),   #add workout
    path('myWorkouts/', views.index, name='listWorkouts'),
    path('myWorkouts/<int:pk>/Details/', views.details_workout, name='workoutDetails'),
    path('myWorkouts/<int:pk>/Edit/', views.edit_workout, name='editWorkout'), #edit workout
    path('myWorkouts/<int:pk>/Edit/Delete', views.delete_workout, name='deleteWorkout'), #delete workout
]
