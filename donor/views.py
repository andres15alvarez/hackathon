from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from donor.models import DeliveredDonation
from donor.serializers import DeliveredDonationSerializer
from hackaton.permissions import IsAdmin


class DeliveredDonationAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    @extend_schema(responses=DeliveredDonationSerializer(many=True))
    def get(self, request, document):
        queryset = DeliveredDonation.objects.filter(patient__document=document)
        serializer = DeliveredDonationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
