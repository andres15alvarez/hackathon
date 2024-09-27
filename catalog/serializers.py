from rest_framework import serializers

from catalog.models import FrequentQuestion, Illness, IllnessMedicine, Medicine, Sector


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = "__all__"
        read_only_fields = ["id"]


class IllnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illness
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "deleted_at"]


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "deleted_at"]


class IllnessMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = IllnessMedicine
        fields = "__all__"


class FrequentQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentQuestion
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "deleted_at"]
