# Generated by Django 4.2.5 on 2024-01-19 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_patterns', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern_abcd',
            name='current_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='selected_abcd',
            name='current_date',
            field=models.DateField(null=True),
        ),
    ]
