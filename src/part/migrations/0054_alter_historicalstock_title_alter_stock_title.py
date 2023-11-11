# Generated by Django 4.1.3 on 2023-11-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("part", "0053_alter_historicalstock_source_alter_stock_source"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalstock",
            name="title",
            field=models.CharField(blank=True, db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name="stock",
            name="title",
            field=models.CharField(blank=True, db_index=True, max_length=128),
        ),
    ]
