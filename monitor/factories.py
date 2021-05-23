import factory
from django.utils import timezone
from django.contrib.auth import get_user_model
from monitor import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Faker('user_name')


class SymptomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Symptom

    name = factory.Sequence(lambda n: f"อาการ {n}")


class MeasurementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Measurement

    created = factory.Faker('past_datetime', tzinfo=timezone.get_current_timezone())
    user = factory.SubFactory(UserFactory)
    temperature = factory.Faker('pydecimal', min_value=36, max_value=40)
    o2sat = factory.Faker('pyint', min_value=90, max_value=100)
    systolic = factory.Faker('pyint', min_value=120, max_value=130)
    diastolic = factory.Faker('pyint', min_value=90, max_value=100)

    @factory.post_generation
    def symptoms(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for symptom in extracted:
                self.symptoms.add(symptom)
