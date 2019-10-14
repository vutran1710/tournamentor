# Generated by Django 2.2.6 on 2019-10-14 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='tour_type',
            field=models.ForeignKey(limit_choices_to=models.Q(('model', 'LeagueTour'), ('model', 'KnockoutTour'), ('model', 'Game'), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
