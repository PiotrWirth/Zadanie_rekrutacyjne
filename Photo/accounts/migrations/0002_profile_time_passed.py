# Generated by Django 4.1.7 on 2023-02-21 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='time_passed',
            field=models.DurationField(default=datetime.timedelta),
        ),
    ]
