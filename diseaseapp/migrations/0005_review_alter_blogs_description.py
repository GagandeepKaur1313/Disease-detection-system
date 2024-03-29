# Generated by Django 5.0.2 on 2024-02-14 05:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diseaseapp", "0004_blogs_doctors_delete_person"),
    ]

    operations = [
        migrations.CreateModel(
            name="review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("message", models.TextField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name="blogs",
            name="description",
            field=models.CharField(max_length=2000),
        ),
    ]
