from django.utils.timezone import now
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from catalog.models import FrequentQuestion, Illness, IllnessMedicine, Medicine, Sector
from catalog.serializers import FrequentQuestionSerializer, IllnessMedicineSerializer, IllnessSerializer, MedicineSerializer, SectorSerializer


class SectorViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


class IllnessViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
    queryset = Illness.objects.filter(deleted_at__isnull=False)
    serializer_class = IllnessSerializer

    def perform_destroy(self, instance):
        instance.deleted_at = now()
        instance.save()


class MedicineViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
    queryset = Medicine.objects.filter(deleted_at__isnull=False)
    serializer_class = MedicineSerializer

    def perform_destroy(self, instance):
        instance.deleted_at = now()
        instance.save()


class IllnessMedicineViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
    queryset = IllnessMedicine.objects.all()
    serializer_class = IllnessMedicineSerializer


class FrequentQuestionViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
    queryset = FrequentQuestion.objects.filter(deleted_at__isnull=False, is_visible=True)
    serializer_class = FrequentQuestionSerializer

    def perform_destroy(self, instance):
        instance.deleted_at = now()
        instance.save()
