# Generated by Django 5.0.6 on 2024-07-16 16:33

from random import randint
from django.db import migrations


def populate_db(apps, schema_editor):
    Student = apps.get_model('ApexTracker', 'Student')
    Course = apps.get_model('ApexTracker', 'Course')

    for i in range(4):
        student = Student(
            name = 'TestStudent' + str(i),
            grad_year = 2024 + i,
            deadline = '2025-05-30'
            )
        student.save()

        for j in ['Math', 'Science', 'English', 'Social Studies']:
            course = Course(
                course_name = j,
                completion = randint(0, 50),
                full_length_req = True,
                semester = randint(1,3),
                student = student
                )
            course.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ApexTracker', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
    ]
