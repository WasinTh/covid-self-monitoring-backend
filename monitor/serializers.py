import datetime
from rest_framework import serializers
from django.contrib.auth import get_user_model
from monitor.models import Measurement, Symptom

User = get_user_model()


class SymptomSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Symptom
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(default=datetime.datetime.now())
    symptoms = SymptomSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),
                                              default=serializers.CurrentUserDefault())

    def validate_temperature(self, data):
        if data < 30 or data > 50:
            raise serializers.ValidationError('Unreasonable temperature')
        return data

    def validate_user(self, data):
        if self.instance and self.instance.user != data:
            raise serializers.ValidationError('Cannot update other user instance')
        return data

    class Meta:
        model = Measurement
        fields = '__all__'

    def create(self, validated_data):
        symptoms = validated_data.pop('symptoms')
        measurement = Measurement.objects.create(**validated_data)
        measurement.symptoms.set(Symptom.objects.filter(id__in=[s['id'] for s in symptoms]))
        return measurement

    def update(self, instance, validated_data):
        symptoms = validated_data.pop('symptoms')
        measurement = super().update(instance, validated_data)
        measurement.symptoms.set(Symptom.objects.filter(id__in=[s['id'] for s in symptoms]))
        return measurement

