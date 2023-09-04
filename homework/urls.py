from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import HomeworkView, StudentsHomeworkView, CommentsView

router = DefaultRouter()
router.register(r'homework', HomeworkView)
router.register(r'completed_homework', StudentsHomeworkView)
router.register(r'comments', CommentsView)

urlpatterns = [
    path('', include(router.urls))
]