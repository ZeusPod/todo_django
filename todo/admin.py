from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'description',
        'created_at',
        'limite_date',
        'status',
        'color',
        )
    

admin.site.register(Task, TaskAdmin)