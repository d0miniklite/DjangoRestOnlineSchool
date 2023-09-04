from django.db import models
from courses.models import Lecture
from user.models import User


class Homework(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class StudentsHomework(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return f"Student: {self.student.username}, Homework: {self.homework.title}"


class Comments(models.Model):
    student_homework = models.ForeignKey(StudentsHomework, on_delete=models.CASCADE)
    comment = models.TextField()
    grade = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Comment on: {self.student_homework}"