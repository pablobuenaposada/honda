# Generated by Django 4.1.3 on 2024-01-09 23:18

from django.db import migrations, models

import part.validators


class Migration(migrations.Migration):
    dependencies = [
        ("part", "0061_alter_historicalstock_source_alter_stock_source"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalpart",
            name="reference",
            field=models.CharField(
                db_index=True,
                default=None,
                max_length=15,
                validators=[
                    part.validators.validate_reference,
                    part.validators.validate_if_exists,
                ],
            ),
        ),
        migrations.AlterField(
            model_name="part",
            name="reference",
            field=models.CharField(
                default=None,
                max_length=15,
                unique=True,
                validators=[
                    part.validators.validate_reference,
                    part.validators.validate_if_exists,
                ],
            ),
        ),
    ]
