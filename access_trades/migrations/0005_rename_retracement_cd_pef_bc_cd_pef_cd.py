# Generated by Django 4.2.5 on 2023-10-14 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_trades', '0004_rename_cd_peformance_cd_pef'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cd_pef',
            old_name='retracement',
            new_name='bc',
        ),
        migrations.AddField(
            model_name='cd_pef',
            name='cd',
            field=models.JSONField(null=True),
        ),
    ]
