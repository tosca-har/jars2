# Generated by Django 5.0.8 on 2024-08-14 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vessels', '0008_remove_vessel_vesselgroup_vessel_vesselgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vessel',
            old_name='lip_bulge_in',
            new_name='lip_bulge_inside',
        ),
        migrations.RenameField(
            model_name='vessel',
            old_name='lip_bulge_out',
            new_name='lip_bulge_outside',
        ),
        migrations.RemoveField(
            model_name='vessel',
            name='decoration_finger',
        ),
    ]
