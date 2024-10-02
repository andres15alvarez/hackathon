from rest_framework import serializers

from patient.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    illness = serializers.UUIDField(required=True)
    medicine = serializers.UUIDField(required=True)
    grammage = serializers.FloatField(required=True)
    class Meta:
        model = Patient
        fields = "__all__"
        extra_kwargs = {
            "illness": {
                "write_only": True
            },
            "medicine": {
                "write_only": True
            },
            "grammage": {
                "write_only": True
            }
        }
