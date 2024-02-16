# sensor_app/urls.py
from django.urls import path
from .views import update_sensor_data

urlpatterns = [
    path('update_sensor_data/', update_sensor_data, name='update_sensor_data'),
]
