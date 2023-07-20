# Generated by Django 4.0.2 on 2022-06-10 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0019_stockstested'),
    ]

    operations = [
        migrations.CreateModel(
            name='savedLists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('stock', models.CharField(max_length=255, verbose_name='stock')),
            ],
        ),
        migrations.AlterField(
            model_name='stockstested',
            name='stock',
            field=models.CharField(max_length=255, verbose_name='stock'),
        ),
    ]