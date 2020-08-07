from django.forms import ModelForm
from .models import Workout
from django import forms
import datetime

# Create a form for Workout model

class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = '__all__' # workout information fields
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }