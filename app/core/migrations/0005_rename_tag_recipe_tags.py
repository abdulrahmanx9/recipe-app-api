# Generated by Django 5.1.3 on 2024-12-01 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tag_recipe_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='tag',
            new_name='tags',
        ),
    ]
