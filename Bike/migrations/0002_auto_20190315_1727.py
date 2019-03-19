# Generated by Django 2.1.5 on 2019-03-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bike', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='available_bike_stands',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bike',
            name='available_bikes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bike',
            name='banking',
            field=models.BooleanField(max_length=5),
        ),
        migrations.AlterField(
            model_name='bike',
            name='bike_stands',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bike',
            name='bonus',
            field=models.BooleanField(max_length=5),
        ),
        migrations.AlterField(
            model_name='bike',
            name='status',
            field=models.CharField(max_length=10),
        ),
    ]
