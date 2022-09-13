from django.contrib import messages
from django.shortcuts import render
from BMI_App.filters import BmiFilter
from BMI_App.models import Bmi
from asgiref.sync import sync_to_async


#  Home page
def index(request):
    return render(request, 'Home.html')


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


#  List of different categories of BMI in asynchronous view
@sync_to_async
def bmi_list(request):
    #  saving all bmi data in ascending order
    data = Bmi.objects.all().order_by('bmi').values()
    # filter bmi according to various category
    category_filter = BmiFilter(request.GET, queryset=data)
    return render(request, 'BMI List.html', {'data': data, "category_filter": category_filter})


#  Histogram based on category
def plot(request):
    #  calculating the count of each category
    severe_thinness = Bmi.objects.filter(range="Severe Thinness").count()
    moderate_thinness = Bmi.objects.filter(range="Moderate Thinness").count()
    mild_thinness = Bmi.objects.filter(range="Mild Thinness").count()
    normal = Bmi.objects.filter(range="Normal").count()
    overweight = Bmi.objects.filter(range="Overweight").count()
    obese_class_i = Bmi.objects.filter(range="Obese Class I").count()
    obese_class_ii = Bmi.objects.filter(range="Obese Class II").count()
    obese_class_iii = Bmi.objects.filter(range="Obese Class III").count()
    # save as list
    category_count = [severe_thinness, moderate_thinness, mild_thinness,
                      normal, overweight, obese_class_i, obese_class_ii, obese_class_iii]
    return render(request, 'Plot.html', {'category_count': category_count})
