# Generated by Django 4.2.1 on 2023-05-31 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("folt_api", "0003_offeritem_offer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="offer",
            name="items",
            field=models.ManyToManyField(to="folt_api.offeritem"),
        ),
    ]