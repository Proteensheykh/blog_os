# Generated by Django 3.1.2 on 2020-10-20 05:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201018_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 20, 6, 22, 10, 606815)),
        ),
    ]
