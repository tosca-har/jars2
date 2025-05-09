# Generated by Django 5.1.5 on 2025-01-25 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vessels', '0021_remove_vessel_tags_remove_vessel_imagename_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vessel',
            name='base_technique',
        ),
        migrations.RemoveField(
            model_name='vessel',
            name='primary_technique',
        ),
        migrations.RemoveField(
            model_name='vessel',
            name='rim_technique',
        ),
        migrations.RemoveField(
            model_name='vessel',
            name='secondary_technique',
        ),
        migrations.RemoveField(
            model_name='vessel',
            name='use',
        ),
        migrations.AddField(
            model_name='report',
            name='doi',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
