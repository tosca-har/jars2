# Generated by Django 5.1.5 on 2025-03-25 10:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vessels', '0040_remove_vessel_all_feature_vessel_use_baking_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vessel',
            name='use_transfer',
            field=models.IntegerField(default='0', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
    ]
