# Generated by Django 4.2 on 2024-10-02 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0003_patientillness"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientillness",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="illnesses",
                to="patient.patient",
            ),
        ),
    ]
