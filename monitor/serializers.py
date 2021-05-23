import datetime
from rest_framework import serializers
from django.contrib.auth import get_user_model
from monitor.models import Measurement, Symptom

User = get_user_model()


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(default=datetime.datetime.now())
    symptoms = SymptomSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),
                                              default=serializers.CurrentUserDefault())

    class Meta:
        model = Measurement
        fields = '__all__'
