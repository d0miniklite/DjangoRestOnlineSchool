from rest_framework import serializers
from .models import Courses, Lecture


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('title', 'description', 'course')


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('title', 'description', 'price', 'students', 'professors')