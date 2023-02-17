from rest_framework.response import Response
from rest_framework import generics

from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorMeasurementSerializer
from measurement.models import Sensor, Measurement


class SensorAPIView(generics.ListCreateAPIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        s = SensorSerializer(sensors, many=True)
        return Response(s.data)
    
    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class SensorUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(self, request, *args, **kwargs):
        queryset = Sensor.objects.filter(id = kwargs.get('pk', 1))
        s = SensorMeasurementSerializer(queryset, many=True)
        return Response(s.data)
    
        

class MeasurmentAPIView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

