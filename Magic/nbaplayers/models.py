from django.db import models

class NBAplayer(models.Model):
    playersname = models.CharField(max_length=150)
    portrait = models.ImageField(blank = True)
    number = models.IntegerField(default=0)
    club = models.CharField(max_length=150)
    trelniki = models.IntegerField(default=0)
    dvushki = models.IntegerField(default=0)
    blizniki = models.IntegerField(default=0)
    vsesrazu = models.IntegerField(default=0)
    bio = models.CharField(max_length=150)
