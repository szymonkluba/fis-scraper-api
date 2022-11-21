# Generated by Django 4.0.1 on 2022-11-14 22:39

from django.db import migrations, models
import scraper.models


class Migration(migrations.Migration):

    dependencies = [
        ("scraper", "0006_filemetadata_folder"),
    ]

    operations = [
        migrations.AddField(
            model_name="race",
            name="file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=scraper.models.tournament_directory_path,
            ),
        ),
    ]