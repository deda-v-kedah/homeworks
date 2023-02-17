from django.urls import path
from measurement.views import SensorAPIView, SensorUpdateAPIView, MeasurmentAPIView

urlpatterns = [
    path('sensors/', SensorAPIView.as_view()),
    path('sensors/<pk>/', SensorUpdateAPIView.as_view()),
    path('measurements/', MeasurmentAPIView.as_view())
    
]
