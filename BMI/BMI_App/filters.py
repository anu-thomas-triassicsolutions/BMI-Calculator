import django_filters as filters
from BMI_App.models import Bmi


class BmiFilter(filters.FilterSet):
    #  data to be filterd
    range = filters.CharFilter(label='Search by category')
    gender = filters.CharFilter(label='Search by gender')

    class Meta:
        model = Bmi
        fields = {'range': ['exact'], 'gender': ['exact']}
