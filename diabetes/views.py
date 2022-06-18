from cmath import inf
from tkinter.tix import INTEGER
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
import joblib
diabetes_model = joblib.load('./savedModel/daibetes.pkl')


def diabetes_predict(request):
    return render(request, 'diabetes/index.html')


def diabetes_result(request):
    pregnancies = request.GET['pregnancies']
    glucose = request.GET['glucose']
    blodPressure = request.GET['blodPressure']
    skinThickness = request.GET['skinThickness']
    insulin = request.GET['insulin']
    bmi = request.GET['bmi']
    diabetesPedigressFunction = request.GET['dpfc']
    age = request.GET['age']

    pg = int(pregnancies)
    gl = int(glucose)
    bp = int(blodPressure)
    sk = int(skinThickness)
    ins = int(insulin)
    bmi_ = float(bmi)
    dpf = float(diabetesPedigressFunction)
    ag = int(age)

    result = diabetes_model.predict([[pg, gl, bp, sk, ins, bmi, dpf, ag]])
    result_format = " "
    if result == 1:
        result_format = "Yes"
    elif result == 0:
        result_format = "No"

    context = {
        'pregnancies': pg,
        'glucose': gl,
        'blodPressure': bp,
        'skinThickness': sk,
        'insulin': ins,
        'bmi': bmi_,
        'dpfc': dpf,
        'age': ag,
        'result': result_format,
    }

    return render(request, 'diabetes/result.html', context)
