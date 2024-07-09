from django.contrib import admin

from django.contrib import admin
from .models import (Flavor, Container, Topping, IceCreamInContainer)
from django.utils.safestring import mark_safe


@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    ordering = ('name',)
    # Добвлять для изображения
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
    pass

# @admin.register(IceCreamAtStick)
# class IceCreamAtStickAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Drink)
# class DrinkAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         obj.calculate_total_price()
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     pass
