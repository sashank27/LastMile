# Generated by Django 2.1.5 on 2019-01-26 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lastMileApp', '0002_auto_20190126_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_id',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='flight_id',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='passenger_id',
        ),
    ]
