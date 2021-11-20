from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=500)
    day = models.DateTimeField()
    reminder = models.BooleanField(default= True)
