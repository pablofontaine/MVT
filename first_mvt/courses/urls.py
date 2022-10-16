from django.urls import path

from courses.views import fun_create_course

urlpatterns = [
    path('create_course/<str:name>/<int:code>', fun_create_course),
]
