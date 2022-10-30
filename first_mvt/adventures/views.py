from django.shortcuts import render

from adventures.models import Adventure

# Create your views here.

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