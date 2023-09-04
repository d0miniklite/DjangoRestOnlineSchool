from django.contrib import admin
from .models import Homework, Comments, StudentsHomework
# Register your models here.
admin.site.register(Homework)
admin.site.register(StudentsHomework)
admin.site.register(Comments)