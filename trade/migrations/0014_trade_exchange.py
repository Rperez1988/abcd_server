# Generated by Django 4.0.2 on 2022-11-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0013_remove_trade_initialtradetype_remove_trade_tradetype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='exchange',
            field=models.CharField(default=1, max_length=255, verbose_name='exchange'),
            preserve_default=False,
        ),
    ]
