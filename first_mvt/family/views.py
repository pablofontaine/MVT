from datetime import datetime
from django.shortcuts import render

from family.models import Family_member

# Create your views here.

def fun_create_family_member(request, name: str, last_name: str, age: int, relationship: str, birth: str):
    '''Esta función vista crea un miembre de la familia a través de una URL.
    Los parámetros para la función son nombre, apellido, edad, relación y fecha de nacimiento.
    Se insertan por URL, separados por una barra.'''
    birth = datetime.strptime(birth, "%Y-%m-%d")
    member = Family_member(name=name, last_name=last_name, age=age, relationship=relationship, birth=birth)
    member.save()

    context_dict = {'member': member}
    return render(
        request=request,
        context=context_dict,
        template_name='family/create_family_member.html',
    )

def fun_show_family_members(request):
    '''Esta función devuelve la lista de todos los miembros de la familia creados.'''
    members = Family_member.objects.all()

    context_dict = {'members': members}

    return render(
        request=request,
        context=context_dict,
        template_name='family/list_family_members.html',
    )