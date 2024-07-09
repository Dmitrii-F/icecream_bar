from django.db import models
from django.contrib.auth.models import User


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=15)
#     address = models.CharField(max_length=200)


class Flavor(models.Model):
    # ICE_CREAM_TYPES = (
    #     ('Creamy', 'Сливочное мороженое'),
    #     # ('Ice_Pop', 'Фруктовый лёд'),
    #     # ('Eskimo', 'Эскимо'),
    # )
    # type = models.CharField(max_length=100, choices=ICE_CREAM_TYPES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Flavor/', blank=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Container(models.Model):
    # SIZE_CHOICES = (
    #     ('Small', 'Маленький'),
    #     ('Medium', 'Средний'),
    #     ('Large', 'Большой'),
    # )
    name = models.CharField(max_length=100)
    description = models.TextField()
    # size = models.CharField(max_length=100, choices=SIZE_CHOICES, blank=True, null=True)
    # max_flavors = models.PositiveIntegerField()
    image = models.ImageField(upload_to='Container/', blank=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Topping/', blank=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class IceCreamInContainer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE, verbose_name='Добавка')
    flavor3 = models.ForeignKey(Flavor, on_delete=models.CASCADE, related_name='flavor3', verbose_name='Вкус')
    flavor2 = models.ForeignKey(Flavor, on_delete=models.CASCADE, related_name='flavor2', verbose_name='Вкус')
    flavor1 = models.ForeignKey(Flavor, on_delete=models.CASCADE, related_name='flavor1', verbose_name='Вкус')
    container = models.ForeignKey(Container, on_delete=models.CASCADE, verbose_name='Основа')
    total_price = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='Стоимость')
    ordered_at = models.DateTimeField(auto_now_add=True)

    def save(self):
        self.total_price = (self.topping.price + self.flavor3.price + self.flavor2.price + self.flavor1.price +
                            self.container.price)
        return super(IceCreamInContainer, self).save()

    def __str__(self):
        flavors = self.flavor1.name + ', ' + self.flavor2.name + ', ' + self.flavor3.name
        topping = self.topping.name
        return f"Сливочное со вкусами: {flavors} в {self.container.name} с добавкой: {topping}"


# class IceCreamAtStick(models.Model):
#     TYPES = (
#         ('Ice_Pop', 'Фруктовый лёд'),
#         ('Eskimo', 'Эскимо'),
#     )
#     type = models.CharField(max_length=100, choices=TYPES)
#     flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)
#     topping = models.ForeignKey(Topping, on_delete=models.SET_NULL, blank=True, null=True)
#     price = models.PositiveIntegerField()
#
#     def __str__(self):
#         return self.type + str(self.flavor.name)


# class Drink(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.PositiveIntegerField()
#
#     def __str__(self):
#         return self.name
#
#
# class Item(models.Model):
#     ice_cream_in_container = models.ForeignKey(IceCreamInContainer, on_delete=models.SET_NULL, blank=True, null=True)
#     ice_cream_at_stick = models.ForeignKey(IceCreamAtStick, on_delete=models.SET_NULL, blank=True, null=True)
#     drink = models.ForeignKey(Drink, on_delete=models.SET_NULL, blank=True, null=True)
#
#     def __str__(self):
#         if self.ice_cream_in_container:
#             return 'Мороженое' + str(self.ice_cream_in_container)
#         if self.ice_cream_at_stick:
#             return 'Мороженое' + str(self.ice_cream_at_stick)
#         if self.drink:
#             return 'Напиток' + self.drink.name
#
#
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     item = models.ManyToManyField(Item)
#     quantity = models.PositiveIntegerField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def calculate_total_price(self):
#         self.total_price = sum(item.quantity * item.price for item in self.item.all())
#         self.save()

#     def __str__(self):
#         return 'Корзина №' + str(self.id)


# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('New', 'Новый'),
#         ('Completed', 'Завершен'),
#     ]
#     cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(
#         max_length=50,
#         choices=STATUS_CHOICES,
#         default='New'
#     )
#
#     def __str__(self):
#         return f"Заказ № {self.id}"
