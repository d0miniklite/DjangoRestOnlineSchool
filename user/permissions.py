from rest_framework import permissions
from user.models import User
from courses.models import Courses


class CoursePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_teacher == 'teacher' and obj.professors.filter(id=request.user.id).exists()


class LecturePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_teacher == 'teacher':
            return obj.course.professors.filter(id=request.user.id).exists()
        return False


class HomeworkPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_teacher == 'teacher':
            if hasattr(obj, 'course'):
                return obj.course.professors.filter(id=request.user.id).exists()
            elif hasattr(obj, 'lecture'):
                return obj.lecture.course.professors.filter(id=request.user.id).exists()
        return False


class CommentsPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_teacher == 'teacher':
            homework = obj.student_homework.homework
            course = homework.lecture.course
            return course.professors.filter(id=request.user.id).exists()
        return False


class SendingStudentsHomework(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.lecture.course.professors.filter(id=request.user.id).exists()
        if request.user.is_authenticated and request.user.is_teacher == 'student':
            if hasattr(obj, 'course'):
                return obj.course.students.filter(id=request.user.id).exists()
            elif hasattr(obj, 'lecture'):
                return obj.lecture.course.students.filter(id=request.user.id).exists()
        return False


class StudentHomeworkPermissions(permissions.BasePermission):
    # def has_object_permission(self, request, view, obj):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     if request.user.is_authenticated and request.user.is_teacher == 'student':
    #         homework = obj.homework
    #         course = homework.lecture.course
    #         return obj.student == request.user and course.students.filter(id=request.user.id).exists()
    #     return False
    def has_permission(self, request, view):
        if request.method == 'POST':
            student_id = request.data.get('student')
            course_id = request.data.get('course')

            if student_id and course_id:
                student = User.objects.get(id=student_id)
                course = Courses.objects.get(id=course_id)
                return course.students.filter(id=student.id).exists()

            return False
        return True


# class TeacherHomeworkPermissions(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         if request.user.is_authenticated and request.user.is_teacher == 'teacher':
#             lecture = obj.homework.lecture
#             course = lecture.course
#             return course.professors.filter(id=request.user.id).exists()
#         return False

