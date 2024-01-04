from django.urls import path

from mysite.tasks.views import show_it_works, get_all_tasks, index

urlpatterns = [
    path('', index),
    path('it_works/', show_it_works),
    path('all/', get_all_tasks),
]
