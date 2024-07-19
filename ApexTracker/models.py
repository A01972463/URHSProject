from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

// Learn how Django handles bridging
// many to many relationships use a third table that Django has it's own way to do so
// Enrollment table tracks completion as well


class Student(models.Model):
    name = models.CharField(max_length=20)
    grad_year = models.IntegerField(
        validators=[MinValueValidator(2020), MaxValueValidator(2100)]  # Adjust the range as needed
    )
    deadline = models.DateField()
// Create Many to Many relationship with course

    def __str__(self):
        return self.name

// Add enrollment bridge between Student and Course
// enrollment model tracks anything that is specific to a Student TO a Course
    // I.E. A student has This much progress in This course

class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='courses')  // Link to student THROUGH new enrollment class
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

