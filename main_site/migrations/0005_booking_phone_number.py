# Generated by Django 3.0.7 on 2020-06-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0004_remove_booking_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
