# Generated by Django 4.0.2 on 2023-04-29 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy_settings', '0003_alter_strategysettings_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategysettings',
            name='settingsName',
            field=models.TextField(max_length=25, verbose_name='settingsName'),
        ),
    ]
