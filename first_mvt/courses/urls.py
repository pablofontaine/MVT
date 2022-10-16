from django.urls import path

from courses.views import fun_create_course
from courses.views import fun_list_all_courses

urlpatterns = [
    path('create_course/<str:name>/<int:code>', fun_create_course),
    path('list_all_courses/', fun_list_all_courses)
]
