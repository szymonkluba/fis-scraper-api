# Generated by Django 3.2.9 on 2021-12-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='participantcountry',
            options={'verbose_name_plural': 'Participant countries'},
        ),
        migrations.AddField(
            model_name='race',
            name='fis_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
