# Generated by Django 5.0.1 on 2024-02-12 10:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 12, 10, 55, 44, 708660, tzinfo=datetime.timezone.utc)),
        ),
    ]
