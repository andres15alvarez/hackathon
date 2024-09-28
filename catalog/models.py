from django.db import models

from hackaton.models import BaseModel, BaseTimestampedModel


class Sector(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "sector"


class Illness(BaseModel, BaseTimestampedModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "illness"


class Medicine(BaseModel, BaseTimestampedModel):
    name = models.CharField(max_length=255)
    illnesses = models.ManyToManyField(Illness, through="IllnessMedicine")

    class Meta:
        db_table = "medicine"


class IllnessMedicine(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    illness = models.ForeignKey(Illness, on_delete=models.CASCADE)

    class Meta:
        db_table = "illness_medicine"


class FrequentQuestion(BaseModel, BaseTimestampedModel):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True)

    class Meta:
        db_table = "frequent_question"
