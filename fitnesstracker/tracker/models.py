from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Workout(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
   
    duration=models.PositiveBigIntegerField()
    date=models.DateField(auto_now_add=True)
    reps=models.PositiveBigIntegerField(default=50)
    workoutName=models.CharField(default=50,max_length=10)
    weight=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} workout on {self.date}" 

class Activity(models.Model):
    name=models.CharField(max_length=100)
    sets=models.IntegerField(default=50)
    reps=models.PositiveBigIntegerField(default=50)
    image=models.ImageField(default="/",upload_to="images/")
    tutorial=models.TextField(default=50 ,max_length=500)
    history=models.FloatField(default=50,max_length=100)
    weight=models.FloatField(default=2)
    completed=models.BooleanField(default=False)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='activities') 
    
    def _str_(self):
        return self.name    