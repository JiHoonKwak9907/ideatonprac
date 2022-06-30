from time import time
from turtle import title
from django.db import models

class Room(models.Model):
  title= models.CharField(max_length=50)
  body= models.CharField(max_length=100)
  time= models.TimeField()
  date= models.DateTimeField(auto_now_add=True)
  confirm = models.ImageField(blank=True, null=True, upload_to='room_photo')

  def __str__(self):
    return self.title

