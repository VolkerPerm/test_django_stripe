# Generated by Django 4.1.7 on 2023-02-17 04:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                (
                    "name",
                    models.CharField(
                        max_length=250, verbose_name="Наименование товара"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=5000, verbose_name="Описание"
                    ),
                ),
                ("price", models.FloatField(max_length=20, verbose_name="Цена")),
            ],
            options={
                "verbose_name": "Item",
                "verbose_name_plural": "Items",
            },
        ),
    ]