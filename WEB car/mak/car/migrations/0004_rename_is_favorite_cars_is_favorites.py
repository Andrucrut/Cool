# Generated by Django 4.2.2 on 2023-06-21 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_delete_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='is_favorite',
            new_name='is_favorites',
        ),
    ]
