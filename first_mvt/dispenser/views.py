from django.shortcuts import render

from dispenser.models import Dispenser

# Create your views here.

def list_dispenser(request):
    dispensers = Dispenser.objects.all()

    contex_dict = {'dispensers': dispensers}

    return render(
        request=request,
        context=contex_dict,
        template_name='dispenser/list_dispenser.html',
    )
