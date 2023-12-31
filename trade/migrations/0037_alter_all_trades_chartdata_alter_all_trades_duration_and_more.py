# Generated by Django 4.2.3 on 2023-07-20 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0036_all_trades_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_trades',
            name='chartData',
            field=models.JSONField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='all_trades',
            name='duration',
            field=models.JSONField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='all_trades',
            name='enterExitInfo',
            field=models.JSONField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='all_trades',
            name='length',
            field=models.JSONField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='all_trades',
            name='movement',
            field=models.JSONField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='all_trades',
            name='pivotInfo',
            field=models.JSONField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='all_trades',
            name='pnl',
            field=models.JSONField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='all_trades',
            name='retracement',
            field=models.JSONField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='all_trades',
            name='settings',
            field=models.JSONField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='all_trades',
            name='tradeInfo',
            field=models.JSONField(max_length=254, null=True),
        ),
    ]
