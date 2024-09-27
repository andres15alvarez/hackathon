from django.db import models

from catalog.models import Sector
from hackaton.models import BaseModel, BaseTimestampedModel
from user.models import User


class SexChoices(models.TextChoices):
    MALE = "M", "male"
    FEMALE = "F", "female"


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
