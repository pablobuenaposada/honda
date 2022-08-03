# Generated by Django 4.0.6 on 2022-07-29 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("part", "0004_alter_part_reference"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="stock",
            options={},
        ),
        migrations.AddField(
            model_name="stock",
            name="quantity",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name="stock",
            unique_together={("part", "source")},
        ),
    ]