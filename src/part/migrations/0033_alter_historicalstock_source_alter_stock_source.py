# Generated by Django 4.1.3 on 2022-12-01 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("part", "0032_alter_historicalstock_source_alter_stock_source"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalstock",
            name="source",
            field=models.CharField(
                choices=[
                    ("hondaautomotiveparts", "www.hondaautomotiveparts.com"),
                    ("hondapartsnow", "www.hondapartsnow.com"),
                    ("hondapartsonline", "www.hondapartsonline.net"),
                    ("tegiwa", "www.tegiwaimports.com"),
                    ("amayama", "www.amayama.com"),
                    ("clockwise-motion", "www.clockwisemotion.co.uk"),
                    ("hondaspareparts", "www.hondaspareparts.co.uk"),
                    ("pieces-auto-honda", "www.pieces-auto-honda.fr"),
                    ("acuraexpressparts", "www.acuraexpressparts.com"),
                    ("acurapartsforless", "www.acurapartsforless.com"),
                    ("all4honda", "www.a4h-tech.com"),
                    ("cms", "www.cmsnl.com"),
                    ("nengun", "www.nengun.com"),
                    ("akr", "www.akr-performance.com"),
                    ("online-teile", "www.online-teile.com"),
                ],
                default=None,
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="stock",
            name="source",
            field=models.CharField(
                choices=[
                    ("hondaautomotiveparts", "www.hondaautomotiveparts.com"),
                    ("hondapartsnow", "www.hondapartsnow.com"),
                    ("hondapartsonline", "www.hondapartsonline.net"),
                    ("tegiwa", "www.tegiwaimports.com"),
                    ("amayama", "www.amayama.com"),
                    ("clockwise-motion", "www.clockwisemotion.co.uk"),
                    ("hondaspareparts", "www.hondaspareparts.co.uk"),
                    ("pieces-auto-honda", "www.pieces-auto-honda.fr"),
                    ("acuraexpressparts", "www.acuraexpressparts.com"),
                    ("acurapartsforless", "www.acurapartsforless.com"),
                    ("all4honda", "www.a4h-tech.com"),
                    ("cms", "www.cmsnl.com"),
                    ("nengun", "www.nengun.com"),
                    ("akr", "www.akr-performance.com"),
                    ("online-teile", "www.online-teile.com"),
                ],
                default=None,
                max_length=20,
            ),
        ),
    ]
