# Generated by Django 5.1.5 on 2025-01-23 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vessels', '0019_vesselgroup_vg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vesselgroup',
            name='vg',
            field=models.ManyToManyField(blank=True, null=True, to='vessels.vesselgroup'),
        ),
    ]
