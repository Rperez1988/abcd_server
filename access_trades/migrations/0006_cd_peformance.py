# Generated by Django 4.2.5 on 2023-10-16 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_trades', '0005_rename_retracement_cd_pef_bc_cd_pef_cd'),
    ]

    operations = [
        migrations.CreateModel(
            name='CD_Peformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bc_retracement_range', models.IntegerField()),
                ('cd_retracement_range', models.IntegerField()),
                ('trades', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('active', models.IntegerField()),
                ('average_price_dropped', models.IntegerField()),
                ('lowest_price_dropped', models.IntegerField()),
                ('win_pct', models.IntegerField()),
                ('rsi_wr', models.IntegerField()),
                ('volume_change_win_pct', models.IntegerField()),
                ('volume_change_lose_pct', models.IntegerField()),
                ('average_length_win', models.IntegerField()),
                ('average_length', models.IntegerField()),
            ],
        ),
    ]
