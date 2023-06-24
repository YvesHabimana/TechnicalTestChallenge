from django.db import models

# Create your models here.

class ChallengeModel(models.Model):
    mission = models.TextField()
    vision = models.TextField()
    objectives = models.TextField()
