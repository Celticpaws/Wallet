# Generated by Django 2.1.1 on 2018-10-17 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 10, 17, 9, 21, 27, 451885)),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 10, 17, 9, 21, 27, 452247)),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 10, 17, 9, 21, 27, 452621)),
        ),
    ]
