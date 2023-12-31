# Generated by Django 4.1.5 on 2023-12-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bag",
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
                ("name", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=50)),
                ("material", models.CharField(max_length=50)),
                ("size", models.CharField(max_length=20)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity_available", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
