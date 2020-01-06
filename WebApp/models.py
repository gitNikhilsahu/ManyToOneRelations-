from django.db import models

class Team(models.Model):
    tname = models.CharField(max_length=255)

    def __str__(self):
        return self.tname

class Player(models.Model):
    pname = models.CharField(max_length=255, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, )

    def __str__(self):
        return self.pname
