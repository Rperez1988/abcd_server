# Generated by Django 4.0.2 on 2023-02-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0029_rename_pivotd_trade_pivotinfo_remove_trade_pivota_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='cdRetracement',
            field=models.CharField(default=1, max_length=25, verbose_name='cdRetracement'),
            preserve_default=False,
        ),
    ]
