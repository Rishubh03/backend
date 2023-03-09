# Generated by Django 3.2.18 on 2023-02-16 01:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
import garden.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ward_name', models.CharField(max_length=100, unique=True)),
                ('ward_description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Wards',
            },
        ),
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('garden_name', models.CharField(max_length=100)),
                ('garden_description', models.TextField()),
                ('open_time', models.TimeField(default=datetime.time(5, 0))),
                ('close_time', models.TimeField(default=datetime.time(20, 0))),
                ('address', models.TextField()),
                ('image_url', models.ImageField(blank=True, null=True, upload_to=garden.models.upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ward_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden.ward')),
            ],
            options={
                'verbose_name_plural': 'Gardens',
            },
        ),
    ]