from django.urls import path
from monitor import views

urlpatterns = [
    path('current-temperature/', views.current_temperature),
]
