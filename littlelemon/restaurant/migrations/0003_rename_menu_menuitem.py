# Generated by Django 4.2.9 on 2024-01-24 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_boooking_booking'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='MenuItem',
        ),
    ]
