# Generated by Django 4.0.2 on 2023-04-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy_settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strategysettings',
            name='aBelowb',
        ),
        migrations.RemoveField(
            model_name='strategysettings',
            name='aToBLength',
        ),
        migrations.RemoveField(
            model_name='strategysettings',
            name='bToShortLength',
        ),
        migrations.RemoveField(
            model_name='strategysettings',
            name='isAbnormalPriceActive',
        ),
        migrations.RemoveField(
            model_name='strategysettings',
            name='isPivotSteepnessActive',
        ),
        migrations.RemoveField(
            model_name='strategysettings',
            name='isRsiActive',
        ),
        migrations.RemoveField(
            model_name='strategysettings',
            name='length',
        ),
        migrations.RemoveField(
            model_name='strategysettings',
            name='marketType',
        ),
        migrations.RemoveField(
            model_name='strategysettings',
            name='name',
        ),
        migrations.RemoveField(
            model_name='strategysettings',
            name='rsi',
        ),
        migrations.RemoveField(
            model_name='strategysettings',
            name='singlePivot',
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='aBelowB',
            field=models.CharField(default=1, max_length=25, verbose_name='isAbnormalPriceActive'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='abnormalPriceJump',
            field=models.CharField(default=1, max_length=25, verbose_name='rsi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='entryRSI',
            field=models.CharField(default=1, max_length=25, verbose_name='isRsiActive'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='isComplete',
            field=models.CharField(default=1, max_length=25, verbose_name='isComplete'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='isSelected',
            field=models.CharField(default=1, max_length=25, verbose_name='isComplete'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='market',
            field=models.CharField(default=1, max_length=25, verbose_name='market'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='maxAtoBLength',
            field=models.CharField(default=1, max_length=25, verbose_name='bToShortLength'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='maxBtoCLength',
            field=models.CharField(default=1, max_length=25, verbose_name='marketType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='maxCtoDLength',
            field=models.CharField(default=1, max_length=25, verbose_name='singlePivot'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='pivotLength',
            field=models.CharField(default=1, max_length=25, verbose_name='pivotLength'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='pivotSteepness',
            field=models.CharField(default=1, max_length=25, verbose_name='isPivotSteepnessActive'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='rrr',
            field=models.CharField(default=1, max_length=25, verbose_name='rrr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='sAndr',
            field=models.CharField(default=1, max_length=25, verbose_name='aToBLength'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategysettings',
            name='settingsName',
            field=models.CharField(default=1, max_length=25, verbose_name='settingsName'),
            preserve_default=False,
        ),
    ]