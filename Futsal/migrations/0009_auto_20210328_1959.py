# Generated by Django 3.1.6 on 2021-03-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Futsal', '0008_auto_20210328_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='caption',
            field=models.TextField(default='Manang Marshyangdi', max_length=255, null=True),
        ),
    ]
