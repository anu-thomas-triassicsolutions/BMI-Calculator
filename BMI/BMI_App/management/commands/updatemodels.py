from django.core.management.base import BaseCommand
import pandas as pd
from BMI_App.models import Bmi


class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
          df = pd.read_csv("bmi.csv")
          for AGE, GENDER, HEIGHT, WEIGHT, BMI, RANGE in zip(df.age, df.gender, df.height, df.weight, df.bmi, df.range):
              models = Bmi(age=AGE, gender=GENDER, height=HEIGHT, weight=WEIGHT, bmi=BMI, range=RANGE)
              models.save()