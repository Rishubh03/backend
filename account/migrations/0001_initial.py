# Generated by Django 3.2.16 on 2022-12-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'public'), (2, 'volunteer'), (3, 'supervisor'), (4, 'engineeer'), (5, 'admin')], default=1)),
                ('firstname', models.CharField(max_length=25, verbose_name='First Name')),
                ('middlename', models.CharField(blank=True, max_length=25, null=True, verbose_name='Middle Name')),
                ('lastname', models.CharField(max_length=25, verbose_name='Last Name')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
