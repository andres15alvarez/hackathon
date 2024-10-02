from rest_framework import serializers

from patient.models import Patient, PatientHistory, PatientIllness, PatientTreatment


class PatientSerializer(serializers.ModelSerializer):
    illness = serializers.UUIDField(required=True)
    medicine = serializers.UUIDField(required=True)
    grammage = serializers.FloatField(required=True)
    quantity = serializers.IntegerField(required=True)
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
            },
            "quantity": {
                "write_only": True
            },
            "created_by": {
                "required": False
            }
        }


class PatientIllnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientIllness
        fields = "__all__"


class PatientTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientTreatment
        fields = "__all__"


class PatientHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = "__all__"


class PatientDetailSerializer(serializers.ModelSerializer):
    illnesses = PatientIllnessSerializer(many=True)
    treatments = PatientTreatmentSerializer(many=True)
    histories = PatientHistorySerializer(many=True)

    class Meta:
        model = Patient
        fields = "__all__"
        fields = ["illnesses", "treatments", "histories"]
