from rest_framework import serializers

from donor.models import DeliveredDonation


class DeliveredDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveredDonation
        fields = "__all__"
