"""ml_model URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from car_risk.views import car_risk_predicted
from car_price.views import car_price_predicted
from diabetes.views import diabetes_result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('car_risk', include("car_risk.urls")),
    path('car_result', car_risk_predicted, name='carresult'),
    path('car_price', include('car_price.urls')),
    path('car_price_result', car_price_predicted, name='carprice'),
    path('diabetes_predict', include('diabetes.urls')),
    path('diabetes_result', diabetes_result, name='diabetes_result'),
    path('about', include('about.urls')),
    path('community', include('community.urls')),
]
