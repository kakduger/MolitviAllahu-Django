from django.db import models

class NBAplayer(models.Model):
    playersname = models.CharField(max_length=150)
    portrait = models.ImageField(blank = True)
    number = models.IntegerField
    club = models.CharField(max_length=150)
    trelniki = models.IntegerField
    dvushki = models.IntegerField
    blizniki = models.IntegerField
    vsesrazu = models.IntegerField
    bio = models.CharField(max_length=150)
