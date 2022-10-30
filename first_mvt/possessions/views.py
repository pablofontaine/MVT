from django.shortcuts import render

from possessions.models import Possession

# Create your views here.

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