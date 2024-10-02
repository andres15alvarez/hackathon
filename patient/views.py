from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework import status

from catalog.models import Illness, MedicineContainer
from hackaton.permissions import IsAdmin
from patient.models import Patient, PatientHistory, PatientIllness, PatientTreatment
from patient.serializers import PatientSerializer, PatientDetailSerializer


class PatientListAPIView(GenericAPIView, CreateModelMixin, ListModelMixin):
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = [JWTAuthentication]
    queryset = Patient.objects.filter(deleted_at__isnull=True)
    serializer_class = PatientSerializer

    def get_medicine(self, medicine_id, grammage):
        medicine, _ = MedicineContainer.objects.get_or_create(
            medicine_id=medicine_id,
            grammage=grammage
        )
        return medicine

    def get_illness(self, illness_id):
        try:
            return Illness.objects.get(id=illness_id)
        except Illness.DoesNotExist:
            raise exceptions.NotFound("Enfermedad no encontrada")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.data["created_by"] = request.user
        serializer.is_valid(raise_exception=True)
        medicine = self.get_medicine(
            serializer.validated_data["medicine"],
            serializer.validated_data["grammage"]
        )
        illness = self.get_illness(serializer.validated_data["illness"])
        obj = serializer.save()
        PatientHistory.objects.create(patient=obj)
        PatientIllness.objects.create(patient=obj, illness=illness)
        PatientTreatment.objects.create(
            patient=obj,
            medicine=medicine,
            quantity=serializer.validated_data["quantity"]
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PatientDetailAPIView(GenericAPIView, RetrieveModelMixin):
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = [JWTAuthentication]
    queryset = Patient.objects.filter(deleted_at__isnull=True)
    serializer_class = PatientDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
