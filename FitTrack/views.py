from django.shortcuts import render, redirect, get_object_or_404
from .forms import WorkoutForm
from .models import Workout

def home(request):
    return render(request, 'FitTrack/fittrack_home.html')


def add_workout(request):
    form = WorkoutForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fittrack')
    else:
        print(form.errors)
        form = WorkoutForm()
    return render(request, 'FitTrack/fittrack_create.html', {'form': form})


def index(request):
    get_workouts = Workout.Workouts.all()      #Gets workouts from the database
    context = {'workouts': get_workouts}      #Creates a dictionary object of all workouts for the template
    return render(request, 'FitTrack/fittrack_index.html', context)

def details_workout(request, pk):
    pk = int(pk)                                #Casts value of pk to an int so it's in the proper form
    workout = get_object_or_404(Workout, pk=pk)
    context = {'workout':workout}                   #Creates dictionary object
    return render(request, 'FitTrack/fittrack_details.html', context)

def edit_workout(request, pk):
    pk = int(pk)
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            workout = form.save()
            workout.save()
            return redirect('workoutDetails', pk=workout.pk)
        else:
            print(form.errors)
            form = WorkoutForm(instance=workout)
    else:
        form = WorkoutForm(instance=workout)
        context = {'form': form, 'pk': pk}
        return render(request, 'FitTrack/fittrack_edit.html', context)


def delete_workout(request, pk):
    pk = int(pk)
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        workout.delete()
        return redirect('listWorkouts')
    context = {'workout': workout, 'pk': pk}
    return render(request, 'FitTrack/fittrack_delete.html', context)
