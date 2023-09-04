from rest_framework import viewsets, status
from .models import Courses, Lecture
from .serializers import CoursesSerializer, LectureSerializer
from user.permissions import CoursePermissions, LecturePermissions
from requests import Response
from rest_framework.decorators import action
from user.models import User


class CoursesView(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
    permission_classes = [CoursePermissions]

    @action(detail=True, methods=['post', 'delete'])
    def add_student(self, request, pk=None):
        course = self.get_object()
        student_id = request.data.get('student_id')

        if student_id is not None:
            student = User.objects.get(id=student_id)
            course.students.add(student)
            return Response({'status': 'student added'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'student_id is required'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post', 'delete'])
    def add_professor(self, request, pk=None):
        course = self.get_object()
        professor_id = request.data.get('professor_id')

        if professor_id is not None:
            professor = User.objects.get(id=professor_id)
            course.professors.add(professor)
            return Response({'status': 'professor added'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'professor_id is required'}, status=status.HTTP_400_BAD_REQUEST)


class LectureView(viewsets.ModelViewSet):
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
    permission_classes = [LecturePermissions]