# Generated by Django 3.2.16 on 2022-12-07 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Job ID')),
                ('job_dept', models.CharField(max_length=50, verbose_name='Job Department')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Added')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
            ],
            options={
                'verbose_name_plural': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Employee ID')),
                ('gender', models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'not specified')], default=0, verbose_name='Gender')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('contact_no', models.CharField(max_length=12, verbose_name='Contact Number')),
                ('address', models.TextField(verbose_name='Address')),
                ('date_hired', models.DateField(verbose_name='Date Hired')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Added')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee_information.department', verbose_name='Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('leave_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Leave ID')),
                ('leave_type', models.IntegerField(choices=[(0, 'Privilege Leave (PL)'), (1, 'Casual Leave (CL)'), (2, 'Sick Leave (SL)'), (3, 'Maternity Leave (ML)'), (4, 'Paternity Leave (PL)'), (5, 'Emergency Leave (EL)'), (6, 'Vacation Leave (VL)'), (7, 'Special Leave (SL)')], default=0, verbose_name='Leave Type')),
                ('reason', models.TextField(verbose_name='Reason')),
                ('date_from', models.DateField(verbose_name='Date From')),
                ('date_to', models.DateField(verbose_name='Date To')),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Approved'), (3, 'Rejected'), (4, 'Cancelled')], default=1, verbose_name='Status')),
                ('date_applied', models.DateField(auto_now_add=True, verbose_name='Date Applied')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee_information.employees', verbose_name='Employee ID')),
            ],
            options={
                'verbose_name_plural': 'Leave',
            },
        ),
    ]