# Generated by Django 3.0.6 on 2020-05-13 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0005_scannedsubdomains_alive_subdomain'),
    ]

    operations = [
        migrations.AddField(
            model_name='scannedsubdomains',
            name='http_status',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
    ]
