from django.db import models
from django.contrib.auth.models import AbstractUser
from hackaton.models import BaseModel, BaseTimestampedModel


class User(AbstractUser, BaseModel, BaseTimestampedModel):
    USERNAME_FIELD = "document"
    REQUIRED_FIELDS = []
    username = None
    first_names = models.CharField(max_length=255)
    last_names = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True)
    document = models.CharField(max_length=10, unique=True)
    phone_number1 = models.CharField(11, blank=True, null=True)
    phone_number2 = models.CharField(11, blank=True, null=True)
    donor_type = models.CharField(255, blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = "user"

