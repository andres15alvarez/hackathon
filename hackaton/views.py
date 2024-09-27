from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from drf_spectacular.utils import extend_schema

from hackaton.serializers import HomeSerializer


class HomeView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(responses=HomeSerializer)
    def get(self, request):
        return Response({"status": "up"}, status=status.HTTP_200_OK)
