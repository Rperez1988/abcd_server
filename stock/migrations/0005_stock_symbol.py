# Generated by Django 4.0.2 on 2022-04-25 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_remove_traderesults_days_between_pivots_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='symbol',
            field=models.CharField(default=1, max_length=255, verbose_name='Symbol'),
            preserve_default=False,
        ),
    ]
