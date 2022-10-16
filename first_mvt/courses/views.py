import imp
from django.http import HttpResponse
from django.shortcuts import render

from courses.models import Course

from django.template import loader

# Create your views here.

def fun_create_course(request, name: str, code: int):
    '''Esta función crea un curso a través de una URL.
    Tienes dos parámetros, el primero es el nombre del curso,
    y el segundo parámetro es el código. create_course/<str:name>/<int:code>'''

    template = loader.get_template('create_course.html') # Obtenemos la plantilla que va ser renderizada

    # Create course by Model-Class called Course, and save into DB
    course = Course(name=name, code=code)
    course.save()

    # Render template with loader method
    context_dict = {'course': course} # Creamos el contexto en el diccionario
    render = template.render(context_dict) # Renderizamos el contexto

    return HttpResponse(render)