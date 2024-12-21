from django.shortcuts import render


def DashboardView(request):
    context = {}

    return render(request, 'base.html', context)