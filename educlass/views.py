from django.shortcuts import render


# Create your views here.

def educlass_view(request):
    context = {}
    return render(request, 'edubase/base.html', context)
