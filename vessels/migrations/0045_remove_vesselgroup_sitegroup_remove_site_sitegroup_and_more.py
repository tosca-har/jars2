# Generated by Django 5.1.5 on 2025-04-03 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vessels', '0044_alter_vessel_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vesselgroup',
            name='sitegroup',
        ),
        migrations.RemoveField(
            model_name='site',
            name='sitegroup',
        ),
        migrations.DeleteModel(
            name='Sitegroup',
        ),
    ]
