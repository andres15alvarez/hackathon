from django.urls import path

from donor.views import DeliveredDonationAPIView


app_name = "donor"
urlpatterns = [
    path("delivered/<str:document>", DeliveredDonationAPIView.as_view()),
]
