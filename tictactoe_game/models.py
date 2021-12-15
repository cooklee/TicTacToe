from django.db import models
from django.conf import settings


# Create your models here.

class Game(models.Model):
    board_size = models.IntegerField(default=3)
    line_length = models.IntegerField(default=3)
    players = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
