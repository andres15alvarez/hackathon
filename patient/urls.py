from django.urls import path

from patient.views import PatientListAPIView, PatientDetailAPIView


app_name = "patient"

urlpatterns = [
    path("", PatientListAPIView.as_view(), name="patient_list"),
    path("<uuid:pk>", PatientDetailAPIView.as_view(), name="patient_detail"),
]
