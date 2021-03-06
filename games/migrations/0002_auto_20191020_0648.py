# Generated by Django 2.2.6 on 2019-10-20 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='tour_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='tour_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
