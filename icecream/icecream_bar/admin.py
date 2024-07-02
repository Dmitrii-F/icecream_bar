from django.contrib import admin

from django.contrib import admin
from .models import (Flavor, Container, Topping, IceCreamInContainer, IceCreamAtStick, Drink, Item, Cart, Order)


@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    pass


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    pass


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    pass


@admin.register(IceCreamInContainer)
class IceCreamInContainerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flavors', 'toppings')


@admin.register(IceCreamAtStick)
class IceCreamAtStickAdmin(admin.ModelAdmin):
    pass


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.calculate_total_price()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
