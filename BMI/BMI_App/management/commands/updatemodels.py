from django.core.management.base import BaseCommand
import pandas as pd
from BMI_App.models import Bmi


# For updating bulk data to database
class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
          data = pd.read_csv("bmi.csv")

          for AGE, GENDER, HEIGHT, WEIGHT, BMI, RANGE in zip(data.age,
                                                             data.gender, data.height, data.weight, data.bmi, data.range):
              models = Bmi(age=AGE, gender=GENDER, height=HEIGHT, weight=WEIGHT, bmi=BMI, range=RANGE)
              models.save()
