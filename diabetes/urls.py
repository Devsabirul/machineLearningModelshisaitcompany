from django.urls import path
from .views import diabetes_predict
urlpatterns = [
    path('', diabetes_predict, name="diabetes_predict"),
]
