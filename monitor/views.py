import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from monitor.models import Measurement
from monitor.serializers import MeasurementSerializer


def current_temperature(request):
    data = {'temperature': str(Measurement.objects.last().temperature)}
    return HttpResponse(json.dumps(data))


@api_view(['GET'])
def all_measurement(request):
    serializer = MeasurementSerializer(Measurement.objects.all(), many=True)
    return Response(data=serializer.data)
