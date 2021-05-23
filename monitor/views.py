import json
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from monitor.models import Measurement, Symptom
from monitor.serializers import MeasurementSerializer, SymptomSerializer


def current_temperature(request):
    data = {'temperature': str(Measurement.objects.last().temperature)}
    return HttpResponse(json.dumps(data))


@api_view(['GET'])
def all_measurement(request):
    serializer = MeasurementSerializer(Measurement.objects.all(), many=True)
    return Response(data=serializer.data)


class AllMeasurementView(APIView):
    def get(self, request):
        serializer = MeasurementSerializer(Measurement.objects.all(), many=True)
        return Response(data=serializer.data)


class MeasurementGenericsView(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SymptomGenericsView(generics.ListCreateAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer


class MeasurementViewsets(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SymptomViewsets(viewsets.ReadOnlyModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

