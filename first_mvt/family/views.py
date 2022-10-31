from traceback import print_tb
from django.contrib import messages
from django.shortcuts import render

from family.models import Family_member
from family.forms import FamilyMemberForm

# Create your views here.

def get_members(request):
    members = Family_member.objects.all()
    return members

def family_list(request):
    members = get_members(request)
    context_dict = {'members': members}

    return render(
        request=request,
        context=context_dict,
        template_name='family/member_list.html',
    )

def family_add_member(request):
    if request.method == "POST": # Si el método es POST, entonces:

        member_form = FamilyMemberForm(request.POST)
        '''Primero guardamos en una variable los datos introducidos en el formulario.
        La variable guarda un objeto de tipo FamilyMemberForm, creado en forms.py'''

        if member_form.is_valid(): # Valida si el formato guardado en la variable es correcto
            data = member_form.cleaned_data # Elimina HTML, y deja solo un diccionario con Keys-Values
            actual_objects = Family_member.objects.filter(
                name=data['name'],
                last_name=data['last_name'],
            ).count()
            '''Acá contamos cuantos objetos tienen el nombre y apellido
            que el usuario introdujo en el formulario'''
            if actual_objects:
                '''Verificamos que no exista ningun familiar con este nombre y apellido
                Si existe alguno, se envia un mensaje de error.'''
                messages.error(
                    request,
                    f"El familiar {data['name']} {data['last_name']} ya está creado.",
                )
            else:
                '''Si no existe, se crea un nuevo miembro, con la clase Family_member
                anteriormente definida en los modelos'''
                member = Family_member(
                    name=data['name'],
                    last_name=data['last_name'],
                    age=data['age'],
                    relationship=data['relationship'],
                )
                member.save() # Guardamos en la base de datos
                
                # Enviamos mensaje de miembro creado al usuario
                messages.success(
                    request,
                    f"Has creado a tu {data['relationship']}, {data['name']} {data['last_name']} con {data['age']} años"
                )

            return render(
                request=request,
                context={'members': get_members(request)},
                template_name='family/member_list.html',
            )

    # Si no es POST, entonces:
    member_form = FamilyMemberForm(request.POST)
    context_dict = {'form': member_form}
    return render(
        request=request,
        context=context_dict,
        template_name='family/member_form.html',
    )
