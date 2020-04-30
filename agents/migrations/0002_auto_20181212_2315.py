# Generated by Django 2.1.3 on 2018-12-12 17:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='no_of_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='agent',
            name='rating',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]