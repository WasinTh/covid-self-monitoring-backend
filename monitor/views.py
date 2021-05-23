import json
from django.http import HttpResponse
from monitor.models import Measurement


def current_temperature(request):
    data = {'temperature': str(Measurement.objects.last().temperature)}
    return HttpResponse(json.dumps(data))
