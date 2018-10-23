# Generated by Django 2.1.1 on 2018-10-17 07:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0002_auto_20181011_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2018, 10, 17, 9, 30, 31, 285810))),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category', models.ForeignKey(default=None, null=None, on_delete=django.db.models.deletion.CASCADE, to='asset.Category')),
            ],
        ),
    ]
