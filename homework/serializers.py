from rest_framework import serializers
from .models import Homework, StudentsHomework, Comments


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class StudentsHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsHomework
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'