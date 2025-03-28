# Generated by Django 5.1.5 on 2025-02-11 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vessels', '0029_alter_site_region'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vesselgroup',
            old_name='vg',
            new_name='vg_parent',
        ),
        migrations.AlterField(
            model_name='vessel',
            name='region',
            field=models.CharField(choices=[('MAR', 'Marianas'), ('CAR', 'Carolines'), ('BIS', 'Bismarck'), ('PNG', 'PNG'), ('SOL', 'Solomons'), ('VAN', 'Vanuatu'), ('MAL', 'Maluku'), ('NCA', 'New Caledonia'), ('FIJ', 'Fiji'), ('SAM', 'Samoa'), ('TON', 'Tonga'), ('MAQ', 'Marquesa'), ('NME', 'NE Melanesia'), ('COO', 'Cook'), ('TUV', 'Tuvalu'), ('PHI', 'Philippines'), ('TAI', 'Taiwan'), ('OTH', 'Other'), ('U', 'unknown')], default='U', max_length=20),
        ),
    ]
