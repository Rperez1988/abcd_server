# Generated by Django 4.0.2 on 2022-05-05 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_chartimage_remove_traderesults_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='traderesults',
            name='image',
            field=models.ImageField(default=1, upload_to='media/images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chartimage',
            name='image',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
