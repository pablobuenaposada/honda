# Generated by Django 4.1.3 on 2023-09-05 22:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("part", "0044_alter_historicalstock_title_alter_stock_title"),
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
                    ("japserviceparts", "www.japserviceparts.co.uk"),
                    ("icb", "www.icbmotorsport.com"),
                    ("ipgparts", "www.ipgparts.com"),
                    ("bernardiparts", "www.bernardiparts.com"),
                    ("alvadi", "www.alvadi.ee"),
                ],
                db_index=True,
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
                    ("japserviceparts", "www.japserviceparts.co.uk"),
                    ("icb", "www.icbmotorsport.com"),
                    ("ipgparts", "www.ipgparts.com"),
                    ("bernardiparts", "www.bernardiparts.com"),
                    ("alvadi", "www.alvadi.ee"),
                ],
                db_index=True,
                max_length=20,
            ),
        ),
    ]
