# sensor_app/urls.py
from django.urls import path
from .views import update_sensor_data, sensor_data_view

urlpatterns = [
    path('update_sensor_data/', update_sensor_data, name='update_sensor_data'),
    path('sensor_data/', sensor_data_view, name='sensor_data_view'),
]
