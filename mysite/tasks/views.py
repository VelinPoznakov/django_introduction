from django.shortcuts import render
from django import http

from mysite.tasks.models import Task


# Create your views here.
def show_it_works(request):  # request saves the information about the request.
    return http.HttpResponse('It works')


def get_all_tasks(request):
    all_tasks = Task.objects.order_by('name').all()
    print(list(all_tasks))
    result = ', '.join(f'{t.name}: ({t.id})' for t in all_tasks)
    return http.HttpResponse(result)


def index(request):
    return render(request, 'index.html')
