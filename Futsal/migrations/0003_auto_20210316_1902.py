# Generated by Django 3.1.6 on 2021-03-16 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Futsal', '0002_auto_20210316_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
