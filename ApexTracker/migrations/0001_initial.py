# Generated by Django 5.0.6 on 2024-07-15 17:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('grad_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2020), django.core.validators.MaxValueValidator(2100)])),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('completion', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('full_length_req', models.BooleanField()),
                ('semester', models.IntegerField(choices=[(1, 'Semester 1'), (2, 'Semester 2')])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='ApexTracker.student')),
            ],
        ),
    ]