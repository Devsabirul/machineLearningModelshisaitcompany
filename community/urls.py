from django.urls import path
from .views import community
urlpatterns = [
    path('', community, name="community"),
]
