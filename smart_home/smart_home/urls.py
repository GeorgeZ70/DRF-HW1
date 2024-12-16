from django.contrib import admin
from django.urls import path
from measurement.views import AddMeasurementView, SensorsChangesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('measurements/', AddMeasurementView.as_view()),
    path('sensors/', SensorsChangesView.as_view()),
    path('sensors/<int:pk>/', SensorsChangesView.as_view()),
    ]


