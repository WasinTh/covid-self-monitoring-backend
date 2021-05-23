from django.test import TestCase
from monitor.models import Measurement
from monitor.factories import UserFactory, SymptomFactory, MeasurementFactory


class TestCreateMeasurement(TestCase):
    def setUp(self):
        self.user_1 = UserFactory()
        self.user_2 = UserFactory()
        self.symptoms = [SymptomFactory() for _ in range(0, 3)]

    def test_create_single_user(self):
        for _ in range(0, 10):
            MeasurementFactory(user=self.user_1, symptoms=self.symptoms)

        self.assertEqual(10, Measurement.objects.count())

    def test_create_multiple_user(self):
        for _ in range(0, 10):
            MeasurementFactory(user=self.user_1, symptoms=self.symptoms)

        for _ in range(0, 5):
            MeasurementFactory(user=self.user_2)

        self.assertEqual(15, Measurement.objects.count())
        self.assertEqual(10, Measurement.objects.filter(user=self.user_1).count())
        self.assertEqual(5, Measurement.objects.filter(user=self.user_2).count())
