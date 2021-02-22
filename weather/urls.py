from django.urls import path

from .views import *

urlpatterns = [
    path('', weather, name='weather'),
    path('<int:pk>/delete', CityDeleteView.as_view(), name='delete')
]