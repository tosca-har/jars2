# Generated by Django 5.1.5 on 2025-01-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vessels', '0012_site_production_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='import_vessel',
            field=models.ManyToManyField(blank=True, related_name='isite', to='vessels.vessel'),
        ),
    ]
