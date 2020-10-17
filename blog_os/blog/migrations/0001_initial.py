# Generated by Django 3.1.2 on 2020-10-15 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('category', models.CharField(choices=[('business', 'Business'), ('management', 'Management'), ('technology', 'Technology'), ('design', 'Design'), ('culture', 'Culture')], default='business', max_length=50)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('excerpt', models.CharField(max_length=150)),
                ('month', models.CharField(max_length=3)),
                ('day', models.CharField(max_length=3)),
                ('content', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2020, 10, 15, 18, 35, 32, 841109))),
            ],
        ),
    ]
