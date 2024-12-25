from django.shortcuts import render


def IndexView(request):
    context = {}

    return render(request, 'base.html', context)
