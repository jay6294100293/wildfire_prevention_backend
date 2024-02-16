# sensor_app/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData
from .serializers import SensorDataSerializer

@api_view(['POST'])
def update_sensor_data(request):
    data = request.data
    serializer = SensorDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)
