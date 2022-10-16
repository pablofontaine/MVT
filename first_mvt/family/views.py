import re
from django.shortcuts import render

from family.models import Family_member

# Create your views here.

def fun_create_family_member(request, name: str, last_name: str, age: int, relationship: str):
    '''Esta función vista crea un miembre de la familia a través de una URL.
    Los parámetros para la función son nombre, apellido, edad y relación.
    Se insertan por URL, separados por una barra.'''
    member = Family_member(name=name, last_name=last_name, age=age, relationship=relationship)
    member.save()

    context_dict = {'member': member}
    return render(
        request=request,
        context=context_dict,
        template_name='family/create_family_member.html',
    )