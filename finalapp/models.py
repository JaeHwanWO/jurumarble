from django.db import models

class Data(models.Model):
    players = models.IntegerField(default=0)
    turn = models.IntegerField(default=1)
    isPageVisited = models.BooleanField(default=False)
    diceNum = models.IntegerField(default=0)

    pos1_2pmode = models.IntegerField(default=0)
    pos2_2pmode = models.IntegerField(default=0)

    pos1_3pmode = models.IntegerField(default=0)
    pos2_3pmode = models.IntegerField(default=0)
    pos3_3pmode = models.IntegerField(default=0)

    pos1_4pmode = models.IntegerField(default=0)
    pos2_4pmode = models.IntegerField(default=0)
    pos3_4pmode = models.IntegerField(default=0)
    pos4_4pmode = models.IntegerField(default=0)