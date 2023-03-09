# Generated by Django 3.2.18 on 2023-02-16 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garden', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Enter your complaint')),
                ('details', models.TextField(verbose_name='Explain in more detail')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Solved')], default=1)),
                ('garden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden.garden')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=120)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint_management.complaint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
