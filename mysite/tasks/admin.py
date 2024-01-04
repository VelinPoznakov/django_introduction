from django.contrib import admin

from mysite.tasks.models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'priority')


#admin.site.register(Task)