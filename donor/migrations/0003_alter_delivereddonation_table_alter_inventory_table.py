# Generated by Django 4.2 on 2024-09-28 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("donor", "0002_inventory"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="delivereddonation",
            table="delivered_donation",
        ),
        migrations.AlterModelTable(
            name="inventory",
            table="inventory",
        ),
    ]
