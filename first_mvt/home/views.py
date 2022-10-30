from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render

from family.models import Family_member


# Create your views here.

def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )

def search(request):
    search_param = request.GET['search_param']
    context_dict = dict()

    if search_param:
        query = Q(name__contains=search_param)
        print(query)
        query.add(Q(relationship__contains=search_param), Q.OR)
        print(query)
        query.add(Q(last_name__contains=search_param), Q.OR)
        print(query)
        members = Family_member.objects.filter(query)
        context_dict.update(
            {
                'members': members,
                'search_param': search_param,
            }
        )

    return render(
        request=request,
        context=context_dict,
        template_name='home/index.html'
    )