# Generated by Django 4.0.1 on 2022-01-04 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scraper", "0002_auto_20211205_1607"),
    ]

    operations = [
        migrations.AddField(
            model_name="race",
            name="details",
            field=models.BooleanField(default=False),
        ),
    ]
