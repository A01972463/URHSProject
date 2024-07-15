from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    name = models.CharField(max_length=20)
    grad_year = models.IntegerField(
        validators=[MinValueValidator(2020), MaxValueValidator(2100)]  # Adjust the range as needed
    )
    deadline = models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='courses')
    course_name = models.CharField(max_length=50)
    completion = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    full_length_req = models.BooleanField()
    class Semester(models.IntegerChoices):
        SEMESTER_1 = 1, 'Semester 1'
        SEMESTER_2 = 2, 'Semester 2'
    semester = models.IntegerField(choices=Semester.choices)

    def __str__(self):
        return self.course_name

