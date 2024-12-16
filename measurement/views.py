# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SensorDetailSerializer, MeasurementSerializer
from .models import Sensor


class SensorsChangesView(APIView):

    def get(self, request, pk=None):
        if pk is None:
            sensors = Sensor.objects.all()
            ser = SensorDetailSerializer(sensors, many=True)
            return Response(ser.data)
        else:
            sensor = get_object_or_404(Sensor.objects.all(), id=pk)
            serializer = SensorDetailSerializer(sensor)
            return Response(serializer.data)

    def post(self, request):
        serializer = SensorDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def put(self, request, pk):
        sensor_instance = get_object_or_404(Sensor.objects.all(), pk=pk)
        serializer = SensorDetailSerializer(instance=sensor_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response({"post": serializer.data})


class AddMeasurementView(APIView):

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post".serializer.data})



