import json
from django.http import HttpResponse
from monitor.models import Measurement


def current_temperature(request):
    data = {'temperature': str(Measurement.objects.last().temperature)}
    return HttpResponse(json.dumps(data))


def all_measurement(request):
    data = []
    for m in Measurement.objects.all():
        data.append({
            'created': str(m.created),
            'user': m.user.id,
            'temperature': str(m.temperature),
            'o2sat': m.o2sat,
            'systolic': m.systolic,
            'diastolic': m.diastolic,
            'symptoms': m.symptoms_display,
        })
    return HttpResponse(json.dumps(data))
