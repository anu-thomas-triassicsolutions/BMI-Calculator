from django.contrib import messages
from django.shortcuts import render

from BMI_App.filters import BmiFilter
from BMI_App.models import Bmi


#  Home page
def index(request):
    return render(request, 'Index.html')


#  BMI Calculator
def bmi_calculator(request):
    if request.method == 'POST':
        # Save all values  for calculate BMI
        age = request.POST['age']
        gender = request.POST['gender']
        height = request.POST['height']
        weight = request.POST['weight']
        #  Calculating BMI by height and weight
        bmi = float(weight)/(float(height) * float(height))

        #  Categorising BMI
        if bmi < 16:
            category = "Severe Thinness"
            result = Bmi(age=age, gender=gender, height=height, weight=weight, bmi=bmi, range=category)
            result.save()
            messages.info(request, " you are in Severe Thinness category.")
        elif bmi < 17:
            category = "Moderate Thinness"
            result = Bmi(age=age, gender=gender, height=height, weight=weight, bmi=bmi, range=category)
            result.save()
            messages.info(request, " you are in Moderate Thinness category.")
        elif bmi < 18.5:
            category = "Mild Thinness"
            result = Bmi(age=age, gender=gender, height=height, weight=weight, bmi=bmi, range=category)
            result.save()
            messages.info(request, " you are in Moderate Thinness category.")
        elif bmi < 25:
            category = "Normal"
            result = Bmi(age=age, gender=gender, height=height, weight=weight, bmi=bmi, range=category)
            result.save()
            messages.info(request, " you are lucky!!. You are in Normal category.")
        elif bmi < 35:
            category = "Overweight"
            result = Bmi(age=age, gender=gender, height=height, weight=weight, bmi=bmi, range=category)
            result.save()
            messages.info(request, " you are in Overweight category.")
        elif bmi < 35:
            category = "Obese Class I"
            result = Bmi(age=age, gender=gender, height=height, weight=weight, bmi=bmi, range=category)
            result.save()
            messages.info(request, " you are in Obese Class I category.")
        elif bmi < 40:
            category = "Obese Class II"
            result = Bmi(age=age, gender=gender, height=height, weight=weight, bmi=bmi, range=category)
            result.save()
            messages.info(request, " you are in Obese Class II category. ")
        elif bmi > 40:
            category = "Obese Class III"
            result = Bmi(age=age, gender=gender, height=height, weight=weight, bmi=bmi, range=category)
            result.save()
            messages.info(request, " you are in Obese Class III category.")
    return render(request, 'BMI Calculator.html')


#  List of different categories of BMI
def bmi_list(request):
    #  saving all bmi data in ascending order
    data = Bmi.objects.all().order_by('bmi').values()
    # filter bmi according to various category
    category_filter = BmiFilter(request.GET, queryset=data)
    # total_data = Bmi.objects.all().count()
    # print(total_data)

    return render(request, 'BMI List.html', {'data': data, "category_filter": category_filter})
