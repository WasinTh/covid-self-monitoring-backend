from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Symptom(models.Model):
    """อาการผิดปกติ"""
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    """การวัดค่า"""
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=4, decimal_places=2, help_text='อุณหภูมิร่างกาย')
    o2sat = models.IntegerField(help_text='อ๊อกซิเจนในเลือด')
    systolic = models.IntegerField(help_text='ความดันตัวบน')
    diastolic = models.IntegerField(help_text='ความดันตัวล่าง')
    symptoms = models.ManyToManyField(Symptom, help_text='อาการที่พบ')

    @property
    def symptoms_display(self):
       return ', '.join(self.symptoms.values_list('name', flat=True))

    class Meta:
       ordering = ['-created']

