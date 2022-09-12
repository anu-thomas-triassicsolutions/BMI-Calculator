from django.db import models


class Bmi(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField()
    range = models.CharField(max_length=20)

    def __str__(self):
        return self.gender
