# Generated by Django 5.1.7 on 2025-03-21 06:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='model',
            name='model',
        ),
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='auction_app.model'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='auction_app.brand'),
        ),
    ]
