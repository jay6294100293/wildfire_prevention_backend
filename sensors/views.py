# sensor_app/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData
from .serializers import SensorDataSerializer
# sensor_app/views.py
from django.shortcuts import render
from .models import SensorData

@api_view(['POST'])
def update_sensor_data(request):
    data = request.data
    serializer = SensorDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)


def sensor_data_view(request):
    latest_data = SensorData.objects.order_by('-id').first()  # Get the latest data

    risk_message = None
    if latest_data:
        if latest_data.temperature > 30:
            risk_message = "High temperature - increased risk of wildfire!"
        # Add more conditions for other risk factors if needed

    context = {
        'latest_data': latest_data,
        'risk_message': risk_message,
    }
    return render(request, 'sensor_app/sensor_data.html', context)
