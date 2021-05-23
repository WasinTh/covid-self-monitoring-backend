# Generated by Django 3.2.2 on 2021-05-23 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.DecimalField(decimal_places=2, help_text='อุณหภูมิร่างกาย', max_digits=4)),
                ('o2sat', models.IntegerField(help_text='อ๊อกซิเจนในเลือด')),
                ('systolic', models.IntegerField(help_text='ความดันตัวบน')),
                ('diastolic', models.IntegerField(help_text='ความดันตัวล่าง')),
                ('symptoms', models.ManyToManyField(blank=True, help_text='อาการที่พบ', to='monitor.Symptom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
