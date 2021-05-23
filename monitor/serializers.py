import datetime
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class MeasurementSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(default=datetime.datetime.now())
    temperature = serializers.DecimalField(max_digits=4, decimal_places=2)
    o2sat = serializers.IntegerField()
    systolic = serializers.IntegerField()
    diastolic = serializers.IntegerField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
