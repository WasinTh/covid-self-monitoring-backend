from django.http import HttpResponse
from monitor.models import Measurement


def current_temperature(request):
    return HttpResponse(f"Temperature : {Measurement.objects.last().temperature}")
