from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/sign-in/')
def DashboardView(request):
    context = {}


    return render(request, 'base/base.html', context)
