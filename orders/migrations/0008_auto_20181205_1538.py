# Generated by Django 2.1.3 on 2018-12-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20181205_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='preferred_time',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
