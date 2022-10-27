from django.db import models
from django.forms import IntegerField

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(maxlength=300) 
    last_name = models.CharField(maxlength=300)
    age = models.IntegerField()
    
class Song(models.Model):
    title = models.CharField(maxlength = 250)
    date_released = models.CharField(maxlength = 250)
    likes = models.IntegerField()
    artiste_id = models.IntegerField()

class Lyric(models.Model):
    content = models.CharField(maxlength = 5000)
    song_id = models.IntegerField()