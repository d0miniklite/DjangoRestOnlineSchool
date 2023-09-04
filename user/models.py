from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    teacher = 'teacher'
    student = 'student'

    role_choices = [
        (teacher, 'teacher'),
        (student, 'student'),
    ]
    is_teacher = models.CharField(max_length=10, choices=role_choices, default=student)

    def __str__(self):
        return self.username