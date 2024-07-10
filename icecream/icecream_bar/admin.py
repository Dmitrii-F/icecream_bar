from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Flavor, Container, Topping, IceCreamInContainer


@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    ordering = ('name',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="100')

    get_image.short_description = "Изображение"


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    ordering = ('name',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="100')

    get_image.short_description = "Изображение"


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    ordering = ('name',)
    # Добвлять для изображения
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="100')

    get_image.short_description = "Изображение"


@admin.register(IceCreamInContainer)
class IceCreamInContainerAdmin(admin.ModelAdmin):
    readonly_fields = ('total_price', 'topping', 'flavor3', 'flavor2', 'flavor1', 'container',
                       'user', 'ordered_at')
