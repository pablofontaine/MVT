from django.shortcuts import render
from adventures.models import Adventure
from adventures.forms import AdventuresForm
from django.contrib import messages
# Create your views here.

def get_adventures(request):
    adventure = Adventure.objects.all()
    return adventure

def index(request):

    adventures = Adventure.objects.all()
    context_dict = {
        'adventures': adventures,
    }

    return render(
        request=request,
        context=context_dict,
        template_name='adventures/list_adventures.html'
    )

def adventures_add(request):

    if request.method == 'POST':
        adventures_form = AdventuresForm(request.POST)
        if adventures_form.is_valid():
            data = adventures_form.cleaned_data
            print(data)
            actual_objects = Adventure.objects.filter(
                place=data['place'], date=data['date'],
            ).count()
            print(actual_objects)
            if actual_objects:
                print("Error, ya existe")
                #messages.error(
                #    request,
                #    f'Este evento ya existe, intenta con otro',
                #)
            else:
                new_adventure = Adventure(
                    place=data['place'],
                    date=data['date'],
                    description=data['description'],
                )
                new_adventure.save()
                print("Exito")

            return render(
                request=request,
                context={'adventures': get_adventures(request)},
                template_name='adventures/list_adventures.html',
            )

                # messages.success(
                #     request,
                #     f"¡Felicidades, tienen una nueva aventura!",
                # )


    adventures_form = AdventuresForm(request.POST)
    context_dict = {
        'form': adventures_form,
    }

    return render(
        request=request,
        context=context_dict,
        template_name='adventures/form_adventures.html'
    )
