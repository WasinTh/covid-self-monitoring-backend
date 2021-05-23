from django.contrib import admin
from monitor import models


@admin.register(models.Symptom)
class SymptomAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['user', 'created', 'temperature',
                    'o2sat', 'systolic', 'diastolic', 'symptoms_display']
    list_filter = ['user', 'created']
    filter_horizontal = ['symptoms']

