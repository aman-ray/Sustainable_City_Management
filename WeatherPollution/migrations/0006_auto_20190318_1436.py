# Generated by Django 2.1.5 on 2019-03-18 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WeatherPollution', '0005_auto_20190318_1359'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Weather',
            new_name='WeatherData',
        ),
    ]