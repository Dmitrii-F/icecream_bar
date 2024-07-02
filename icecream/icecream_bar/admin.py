from django.contrib import admin

from django.contrib import admin
from .models import Cup, IceCream, Topping, Order
from django.utils.safestring import mark_safe


# Класс администратора для модели Project
@admin.register(Cup)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    # Добвлять для изображения
    readonly_fields = ('get_image',)
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="100')

    get_image.short_description = "Изображение"

@admin.register(IceCream)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    ordering = ('name',)
    # Добвлять для изображения
    readonly_fields = ('get_image',)
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="100')

    get_image.short_description = "Изображение"

@admin.register(Topping)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    ordering = ('name',)
    # Добвлять для изображения
    readonly_fields = ('get_image',)
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="100')

    get_image.short_description = "Изображение"

# Класс администратора для модели Order
@admin.register(Order)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'status', 'created_at')
    #list_filter = ('status', 'assignee', 'project')
    search_fields = ('order_id', 'cup', 'ice_cream', 'topping', 'created_at')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

