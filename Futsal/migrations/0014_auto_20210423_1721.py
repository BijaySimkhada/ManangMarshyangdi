# Generated by Django 3.1.6 on 2021-04-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Futsal', '0013_bookinghistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinghistory',
            name='booked_time',
            field=models.TimeField(null=True),
        ),
    ]
