from django.urls import path
from .views import car_price


urlpatterns = [
    path('', car_price, name='carprice')
]
