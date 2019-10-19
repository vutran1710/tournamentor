# Generated by Django 2.2.6 on 2019-10-19 15:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_auto_20191016_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knockouttour',
            name='player_per_team',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='leaguetour',
            name='player_per_team',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
    ]
