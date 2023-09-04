from django.db import models
from user.models import User
# Create your models here.


class Courses(models.Model):
    title = models.CharField(max_length=50, default="Default Title")
    description = models.TextField(default='')
    price = models.PositiveIntegerField(default=0)
    students = models.ManyToManyField(User, verbose_name='students_on_course', related_name='student_courses')
    professors = models.ManyToManyField(User, verbose_name='professors_on_course', related_name='professor_courses')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lecture(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.title