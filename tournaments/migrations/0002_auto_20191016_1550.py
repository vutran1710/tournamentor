# Generated by Django 2.2.6 on 2019-10-16 15:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='knockouttour',
            name='player_per_team',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leaguetour',
            name='double_round',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='leaguetour',
            name='player_per_team',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
            preserve_default=False,
        ),
    ]
