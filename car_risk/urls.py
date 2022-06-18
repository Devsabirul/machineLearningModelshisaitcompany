from django.urls import path

from .views import car_risk, car_risk_predicted


urlpatterns = [
    path('', car_risk, name="car_risk"),
]
