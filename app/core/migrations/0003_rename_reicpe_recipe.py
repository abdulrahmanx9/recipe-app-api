# Generated by Django 5.1.3 on 2024-11-26 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_reicpe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reicpe',
            new_name='Recipe',
        ),
    ]