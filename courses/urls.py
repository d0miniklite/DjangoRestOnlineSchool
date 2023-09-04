from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CoursesView, LectureView

router = DefaultRouter()
router.register(r'courses', CoursesView)
router.register(r'lecture', LectureView)


urlpatterns = [
    path('', include(router.urls)),
]