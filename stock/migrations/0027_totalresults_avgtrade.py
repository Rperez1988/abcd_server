# Generated by Django 4.0.2 on 2022-07-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0026_remove_totalresults_avgtrade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalresults',
            name='avgTrade',
            field=models.CharField(default=1, max_length=255, verbose_name='avgTrade'),
            preserve_default=False,
        ),
    ]
