# Generated by Django 5.0.2 on 2024-02-12 03:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("diseaseapp", "0002_rename_person_dummy"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="dummy",
            new_name="person",
        ),
    ]
