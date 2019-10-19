# Generated by Django 2.2.6 on 2019-10-16 15:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='assists',
        ),
        migrations.RemoveField(
            model_name='player',
            name='scores',
        ),
        migrations.RemoveField(
            model_name='player',
            name='stats',
        ),
        migrations.RemoveField(
            model_name='player',
            name='strength',
        ),
        migrations.RemoveField(
            model_name='player',
            name='weakness',
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]