from unittest import result
from django.shortcuts import render
import joblib
from matplotlib.style import context

carPrice_model = joblib.load('./savedModel/car_price_model.pkl')

# Create your views here.


def car_price(request):
    return render(request, 'carprice/index.html')


def car_price_predicted(request):
    carname = request.GET['carname']
    fueltype = request.GET['fueltype']
    doornumber = request.GET['doornumber']
    carbody = request.GET['carbody']
    enginelocation = request.GET['enginelocation']
    wheelbase = request.GET['wheelbase']
    carlength = request.GET['carlength']
    carwidth = request.GET['carwidth']
    carheight = request.GET['carheight']
    enginesize = request.GET['enginesize']

#    conditions use for car name -------------------

    cn = ""

    if carname == "1":
        cn = "alfa-romero Quadrifoglio"
    elif carname == "2":
        cn = "alfa-romero giulia"
    elif carname == "3":
        cn = "Alfa-romero stelvio"
    elif carname == "26":
        cn = "Chevroletvega 2300"
    elif carname == "5":
        cn = "audi 100ls"
    elif carname == "60":
        cn = "mazda rx-7 gs"
    elif carname == "50":
        cn = "jaguar xk"
    elif carname == "47":
        cn = "isuzu MU-X"
    elif carname == "9":
        cn = "audi fox"
    elif carname == "10":
        cn = "bmw 320i"
    elif carname == "12":
        cn = "bmw x3"
    elif carname == "109":
        cn = "subaru "
    elif carname == "223":
        cn = "toyota corona mark ii"
    elif carname == "143":
        cn = "volvo 264gl"
    elif carname == "140":
        cn = "volvo 244dl"
    elif carname == "135":
        cn = "volkswagen rabbit custom"
    elif carname == "107":
        cn = "subaru dl"
    elif carname == "110":
        cn = "subaru trezia"

    # Fuel type condition

    ft = ""

    if fueltype == "0":
        ft = "Diesel"
    elif fueltype == "1":
        ft = "Gas"

    #  door number

    doorn = ""

    if doornumber == "0":
        doorn = "Four"
    elif doornumber == "1":
        doorn = "Two"

    # carbody condition

    cb = ""

    if carbody == "0":
        cb = "convertible"
    elif carbody == "1":
        cb = "hardtop"
    elif carbody == "2":
        cb = "hatchback"
    elif carbody == "3":
        cb = "sedan"
    elif carbody == "4":
        cb = "wagon"

    # engine location

    el = ""

    if enginelocation == "0":
        el = "Front"
    elif enginelocation == "1":
        el = "Rear"


#    for prediction ---------------------------------
    car_name = float(carname)
    fuel_type = float(fueltype)
    door_number = float(doornumber)
    car_body = float(carbody)
    engine_location = float(enginelocation)
    wheel_base = float(wheelbase)
    car_length = float(carlength)
    car_width = float(carwidth)
    car_height = float(carheight)
    engine_size = float(enginesize)

    car_price_predict = carPrice_model.predict(
        [[car_name, fuel_type, door_number, car_body, engine_location, wheel_base, car_length, car_width, car_height, engine_size]])

    context = {
        'carname': cn,
        'fueltype': ft,
        'doornumber': doorn,
        'carbody': cb,
        'enginelocation': el,
        'wheelbase': wheel_base,
        'carlength': car_length,
        'carwidth': car_width,
        'carheight': car_height,
        'enginesize': enginesize,
        'result': car_price_predict,
    }

    return render(request, 'carprice/result.html', context)
