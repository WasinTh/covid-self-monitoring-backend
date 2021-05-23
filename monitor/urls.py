from django.urls import path
from monitor import views

urlpatterns = [
    path('current-temperature/', views.current_temperature),
    path('all-measurement/', views.all_measurement),
    path('all-measurement-api-view/', views.AllMeasurementView.as_view()),
]
