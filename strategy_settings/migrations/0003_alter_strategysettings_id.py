# Generated by Django 4.0.2 on 2023-04-24 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy_settings', '0002_remove_strategysettings_abelowb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategysettings',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]