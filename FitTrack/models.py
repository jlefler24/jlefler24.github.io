from django.db import models


TYPE_EXERCISES = (('Bench Press','Bench Press'), ('Incline Bench Press','Incline Bench Press'), ('BB Bentover Row',' BB Bentover Row'), ('Upright Row','Upright Row'),
('BB Curl','BB Curl'), ('DB Curl','DB Curl'), ('Dips','Dips'), ('Triceps Extention','Tricep Extention'), ('Back Squat','Back Squat'), ('Box Squat','Box Squat'),
('Romanian Deadlift','Romanian Deadlift'), ('Olympic Deadlift','Olympic Deadlift'), ('Military Press','Military Press'), ('Lateral Raise','Lateral Raise'),
('Sit-Ups','Sit-Ups'), ('Plank','Plank'))

class Workout(models.Model):
    date = models.DateField(default=None)
    name = models.CharField(max_length=30)
    exercises = models.CharField(max_length=30, default="blank", choices=TYPE_EXERCISES)
    sets = models.PositiveSmallIntegerField(default=0)
    reps = models.PositiveSmallIntegerField(default=0)
    weight = models.PositiveSmallIntegerField(default=0)

    Workouts = models.Manager()

