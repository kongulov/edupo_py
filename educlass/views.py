from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from educlass.models import *
from educlass.forms import *
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@require_POST
def create_category_ajax(request):
    name = request.POST.get('name')
    company = request.user.company  # İstifadəçinin şirkətini alırıq

    if not name:
        return JsonResponse({'error': 'No name provided'}, status=400)

    # Yaradılmış və ya mövcud olan kategoriyanı alırıq
    category, created = Category.objects.get_or_create(name=name, company=company)

    return JsonResponse({'id': category.id, 'name': category.name})


def educlass_view(request):
    context = {}
    return render(request, 'edubase/base.html', context)


def course_view(request):
    context = {}
    context['course_list'] = Course.objects.filter(company=request.user.company)
    return render(request, 'course/course-list.html', context)


# add course
@login_required(login_url='/sign-in/')
def CourseAddView(request):
    if request.method == 'POST':
        form = CourseAddForm(request.POST, company=request.user.company)
        if form.is_valid():
            course = form.save(commit=False)
            course.company = request.user.company
            course.author = request.user
            course.save()

            messages.success(request,
                             'The new course has been successfully added.')
            return redirect('educlass:course_view')
    else:
        form = CourseAddForm(company=request.user.company)
    context = {
        'form': form
    }
    return render(request, 'course/course-add.html', context)


# course update
@login_required(login_url='/sign-in/')
def CourseUpdateView(request, slug):
    context = {}

    obj = get_object_or_404(Course, slug=slug)
    context['obj'] = obj

    if request.method == 'POST':

        form = CourseUpdateForm(request.POST, instance=obj, company=request.user.company)

        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            messages.success(request,
                             'The course information has been successfully updated.')
            return redirect('educlass:course_view')
    else:

        form = CourseUpdateForm(instance=obj, company=request.user.company)
    context['form'] = form
    return render(request, 'course/course-update.html', context)


# course delete
def course_delete(request, slug):
    obj = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        obj.delete()
        messages.success('The course information has been successfully deleted.')

    return redirect('educlass:course_view')


# class view
def ClassView(request):
    context = {}
    context['class_list'] = Class.objects.filter(company=request.user.company)
    return render(request, 'class/class-list.html', context)


@login_required(login_url='/sign-in/')
def ClassAddView(request):
    if request.method == 'POST':
        form = ClassAddForm(request.POST, company=request.user.company)
        if form.is_valid():
            class_data = form.save(commit=False)
            class_data.company = request.user.company
            class_data.author = request.user
            class_data.status = 1
            class_data.save()

            messages.success(request,
                             'The new class has been successfully added.')
            return redirect('educlass:class_list')
    else:
        form = ClassAddForm(company=request.user.company)
    context = {
        'form': form
    }
    return render(request, 'class/class-add.html', context)
