# Generated by Django 4.0.2 on 2023-06-27 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0035_rename_trade_all_trades'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_trades',
            name='length',
            field=models.JSONField(null=True),
        ),
    ]