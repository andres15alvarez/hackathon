from django.db import models

from catalog.models import Medicine
from hackaton.models import BaseModel, BaseTimestampedModel
from patient.models import Patient
from user.models import User


class Donation(BaseModel, BaseTimestampedModel):
    donated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()

    class Meta:
        db_table = "donation"


class DonationMedicine(BaseModel):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    expire_date = models.DateField()
    batch = models.CharField(max_length=15, null=True, blank=True)
    unit_price = models.FloatField()
    total_price = models.FloatField()

    class Meta:
        db_table = "donation_medicine"


class Expired(BaseModel):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    medicine_donated = models.ForeignKey(DonationMedicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    expired_at = models.DateField()

    class Meta:
        db_table = "expired"


class DeliveredDonation(BaseModel):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    medicine_donated = models.ForeignKey(DonationMedicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    other_notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "delivered_donation"


class Inventory(BaseModel):
    checked_at = models.DateField()
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    needed = models.IntegerField()
    available = models.IntegerField()
    other_notes = models.TextField()

    class Meta:
        db_table = "inventory"
