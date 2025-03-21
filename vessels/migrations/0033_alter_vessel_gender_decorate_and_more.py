# Generated by Django 5.1.5 on 2025-03-21 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vessels', '0032_site_maptag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vessel',
            name='gender_decorate',
            field=models.CharField(choices=[('women', 'women'), ('men', 'men'), ('both', 'both'), ('unknown', 'unknown')], default='unknown', max_length=7),
        ),
        migrations.AlterField(
            model_name='vessel',
            name='gender_make',
            field=models.CharField(choices=[('women', 'women'), ('men', 'men'), ('both', 'both'), ('unknown', 'unknown')], default='unknown', max_length=7),
        ),
    ]
