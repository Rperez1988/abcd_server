# Generated by Django 4.0.2 on 2022-11-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0011_trade_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='returnPercentage',
            field=models.CharField(default=1, max_length=255, verbose_name='returnPercentage'),
            preserve_default=False,
        ),
    ]