from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    biography = models.TextField()
    style = models.CharField(max_length=50)
    location = models.IntegerField()
    experience = models.TextField()
    playingTime = models.IntegerField()
    type = models.IntegerField()

