from django.urls import path
from monitor import views
from django.urls import include
from rest_framework.routers import DefaultRouter
from monitor import views

router = DefaultRouter()
router.register('measurement-viewsets', views.MeasurementViewsets)
router.register('symptom-viewsets', views.SymptomViewsets)

urlpatterns = [
    path('', include(router.urls)),
    path('current-temperature/', views.current_temperature),
    path('all-measurement/', views.all_measurement),
    path('all-measurement-api-view/', views.AllMeasurementView.as_view()),
    path('measurement-generics-view/', views.MeasurementGenericsView.as_view()),
    path('symptom-generics-view/', views.SymptomGenericsView.as_view()),
]
