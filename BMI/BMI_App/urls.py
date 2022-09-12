from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("bmi_calculator/", views.bmi_calculator, name="bmi_calculator"),  # BMI Calculator
    path("bmi_list/", views.bmi_list, name="bmi_list"),  # BMI List
]
