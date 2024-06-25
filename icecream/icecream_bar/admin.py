from django.contrib import admin

from django.contrib import admin
from .models import Cup, IceCream, Topping, Task


# Класс администратора для модели Project
@admin.register(Cup)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(IceCream)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(Topping)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    ordering = ('name',)

# Класс администратора для модели Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    #list_display = ('name', 'project', 'assignee', 'status', 'created_at', 'updated_at')
    #list_filter = ('status', 'assignee', 'project')
    search_fields = ('task_id', 'cup', 'ice_cream', 'topping', 'created_at')
    #list_editable = ('status',  'assignee')
    readonly_fields = ('created_at', 'updated_at')

