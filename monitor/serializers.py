import datetime
from rest_framework import serializers


class MeasurementSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(default=datetime.datetime.now())
    temperature = serializers.DecimalField(max_digits=4, decimal_places=2)
    o2sat = serializers.IntegerField()
    systolic = serializers.IntegerField()
    diastolic = serializers.IntegerField()
