# Generated by Django 2.2.7 on 2019-12-14 15:54

import Base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_app_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='api_token',
            field=models.CharField(default=Base.models.random_api, max_length=17),
        ),
    ]
