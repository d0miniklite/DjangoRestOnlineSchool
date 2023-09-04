from rest_framework import viewsets
from .serializers import HomeworkSerializer, StudentsHomeworkSerializer, CommentsSerializer
from .models import Homework, StudentsHomework, Comments
from user.permissions import HomeworkPermissions, CommentsPermissions, SendingStudentsHomework
# Create your views here.


class HomeworkView(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    permission_classes = [HomeworkPermissions]


class StudentsHomeworkView(viewsets.ModelViewSet):
    serializer_class = StudentsHomeworkSerializer
    queryset = StudentsHomework.objects.all()
    permission_classes = [SendingStudentsHomework]


class CommentsView(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    permission_classes = [CommentsPermissions]