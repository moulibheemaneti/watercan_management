# Generated by Django 2.1.3 on 2018-12-07 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_partyorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='partyorders',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
