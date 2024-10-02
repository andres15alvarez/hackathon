from django.db import models

from catalog.models import Illness, MedicineContainer, Sector
from hackaton.models import BaseModel, BaseTimestampedModel
from user.models import User


class SexChoices(models.TextChoices):
    MALE = "M", "male"
    FEMALE = "F", "female"


class IllnessGravityChoices(models.TextChoices):
    I = "I", "estadio 1"
    II = "II", "estadio 2"


class Patient(BaseModel, BaseTimestampedModel):
    first_names = models.CharField(max_length=255)
    last_names = models.CharField(max_length=255)
    document = models.CharField(max_length=10)
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255)
    phone_number1 = models.CharField(11, blank=True, null=True)
    phone_number2 = models.CharField(11, blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SexChoices.choices)
    purchase_power = models.CharField(max_length=255, blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    class Meta:
        db_table = "patient"


class PatientHistory(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed_bound = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    erc = models.BooleanField(default=False)
    iam = models.BooleanField(default=False)
    acv = models.BooleanField(default=False)
    dyslipidemia = models.BooleanField(default=False)
    obesity = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    allergies = models.BooleanField(default=False)
    other_meds = models.TextField()
    other_notes = models.TextField()

    class Meta:
        db_table = "patient_history"


class PatientTreatment(BaseModel, BaseTimestampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(MedicineContainer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    available = models.BooleanField(default=False)
    done = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "patient_treatment"


class PatientIllness(models.Model):
    illness_gravity = models.CharField(
        choices=IllnessGravityChoices.choices,
        blank=True,
        null=True
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="illnesses")
    illness = models.ForeignKey(Illness, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "patient_illness"
