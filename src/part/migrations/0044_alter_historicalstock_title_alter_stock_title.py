# Generated by Django 4.1.3 on 2023-07-18 21:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("part", "0043_alter_historicalstock_title_alter_stock_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalstock",
            name="title",
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="stock",
            name="title",
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
