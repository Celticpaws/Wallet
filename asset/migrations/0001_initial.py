# Generated by Django 2.1.1 on 2018-10-11 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.CharField(default='XXX', max_length=3, primary_key=True, serialize=False)),
                ('number', models.CharField(default=0, max_length=40, unique=True)),
                ('bank', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Accounts',
                'db_table': 'accounts',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(default='XXX', max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('father', models.ForeignKey(default=None, null=None, on_delete=django.db.models.deletion.CASCADE, to='asset.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
                'ordering': ['id'],
            },
        ),
    ]
