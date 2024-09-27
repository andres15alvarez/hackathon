from django.urls import path

from patient.views import PatientListAPIView


app_name = "patient"

urlpatterns = [
    path("", PatientListAPIView.as_view(), name="patient_list"),
]
