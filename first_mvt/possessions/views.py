from django.shortcuts import render
from django.contrib import messages

from possessions.models import Possession
from possessions.forms import PossessionForm

# Create your views here.

def get_possessions(request):
    return Possession.objects.all()

def index(request):

    posessions = Possession.objects.all()
    context_dict = {
        'possessions': posessions,
    }

    return render(
        request=request,
        context=context_dict,
        template_name='possessions/list_possessions.html'
    )

def possesions_add(request):

    if request.method == 'POST': # Si se envia el formulario, el metodo es post
        possessions_form = PossessionForm(request.POST) # Obtenemos el formulario, y sus datos
        if possessions_form.is_valid(): # Si el formulario es válido (sin errores)
            data = possessions_form.cleaned_data # Entonces borramos el HTML y nos quedamos con los datos puros Key-Values
            actual_objects = Possession.objects.filter(
                item=data['item'],
            ).count() # Creamos una variable que busca en la base de datos si ya existe un item con la misma descripción
            if actual_objects: # Si ya existe, entonces no se puede crear otro igual
                print("Ya existe este objeto")
                messages.error(request, f"Ya existe algun objeto '{data['item']}', vuelve a intentarlo.",)
            else: # De lo contrario, creamos una nueva instancia de clase, guardando los datos el formulario e insertandolós en la base de datos
                new_possession = Possession(
                    item=data['item'],
                    value=data['value'],
                    owner=data['owner'],
                )
                new_possession.save()
                print("Creado con exito")
                messages.success(request, f"Has creado el bien: '{data['item']}' con valor {data['value']} y es de {data['owner']}",)

            return render(
                request=request,
                context={
                    'possessions': get_possessions(request),
                },
                template_name='possessions/list_possessions.html',
                
            )
    
    possessions_form = PossessionForm(request.POST)
    print(possessions_form)
    context_dict = {
        'form': possessions_form,
    }

    return render(
        request=request,
        context=context_dict,
        template_name='possessions/form_possessions.html',
    )