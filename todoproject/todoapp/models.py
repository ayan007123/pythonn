from django.db import models
app_name='todoapp'
# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=250)
    priority=models.IntegerField()

def __str__(self):
    return self.name