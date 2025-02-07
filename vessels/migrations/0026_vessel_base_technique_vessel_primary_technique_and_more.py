# Generated by Django 5.1.5 on 2025-02-02 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vessels', '0025_remove_vessel_feature_vessel_common_feature_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vessel',
            name='base_technique',
            field=models.CharField(choices=[('B', 'ball'), ('S', 'spiral'), ('SL', 'slab'), ('ST', 'strip'), ('O', 'other'), ('U', 'unknown')], default='U', max_length=20),
        ),
        migrations.AddField(
            model_name='vessel',
            name='primary_technique',
            field=models.CharField(choices=[('C', 'coil'), ('CS', 'coil-spiral'), ('CR', 'coil-ring'), ('S', 'slab'), ('M', 'molded'), ('W', 'wheel'), ('O', 'other'), ('U', 'unknown')], default='U', max_length=20),
        ),
        migrations.AddField(
            model_name='vessel',
            name='rim_technique',
            field=models.CharField(choices=[('C', 'coil'), ('CS', 'coil-spiral'), ('CR', 'coil-ring'), ('S', 'slab'), ('M', 'molded'), ('W', 'wheel'), ('O', 'other'), ('U', 'unknown')], default='U', max_length=20),
        ),
        migrations.AddField(
            model_name='vessel',
            name='secondary_technique',
            field=models.CharField(choices=[('B', 'beating'), ('N', 'none'), ('O', 'other'), ('U', 'unknown')], default='U', max_length=20),
        ),
    ]
