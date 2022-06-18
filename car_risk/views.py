import re
from django.http import HttpResponse
from django.shortcuts import render
import joblib

# model load
model = joblib.load('./savedModel/CarRisk.plk')

# Create your views here.


def car_risk(request):
    return render(request, 'carrisk/index.html')


def car_risk_predicted(request):
    speed = request.GET['speed']
    car_age = request.GET['car_age']
    experience = request.GET['experience']
    a = float(speed)
    b = float(car_age)
    c = float(experience)
    pred = model.predict([[a, b, c]])
    context = {
        'speed': a,
        'carage': b,
        'experience': c,
        "result": pred,
    }
    return render(request, 'carrisk/result.html', context)
