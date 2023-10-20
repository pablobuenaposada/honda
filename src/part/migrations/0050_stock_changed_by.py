# Generated by Django 4.1.3 on 2023-10-20 21:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("part", "0049_remove_image_stock_alter_image_stocks"),
    ]

    operations = [
        migrations.AddField(
            model_name="stock",
            name="changed_by",
            field=models.ForeignKey(
                blank=True,
                help_text="Only for grafana purposes",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
