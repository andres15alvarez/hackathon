from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from hackaton.permissions import IsAdmin
from patient.models import Patient
from patient.serializers import PatientSerializer


class PatientListAPIView(GenericAPIView, CreateModelMixin, ListModelMixin):
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = [JWTAuthentication]
    queryset = Patient.objects.filter(deleted_at__isnull=True)
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
