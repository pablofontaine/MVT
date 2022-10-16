from django.http import HttpResponse
from django.shortcuts import render

from courses.models import Course

# Create your views here.

def fun_create_course(request, name: str, code: int):
    '''Esta función crea un curso a través de una URL.
    Tienes dos parámetros, el primero es el nombre del curso,
    y el segundo parámetro es el código. create_course/<str:name>/<int:code>'''

    course = Course(name=name, code=code)
    course.save()

    return HttpResponse(f'Creaste el curso {name} con código {code}')