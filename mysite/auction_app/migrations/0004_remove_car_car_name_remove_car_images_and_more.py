# Generated by Django 5.1.7 on 2025-03-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0003_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_name',
        ),
        migrations.RemoveField(
            model_name='car',
            name='images',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
