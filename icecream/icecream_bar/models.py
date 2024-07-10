from django.contrib.auth.models import User
from django.db import models


class Flavor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Flavor/', blank=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Container(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
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
    flavor3 = models.ForeignKey(Flavor, on_delete=models.CASCADE, related_name='flavor3',
                                verbose_name='Вкус')
    flavor2 = models.ForeignKey(Flavor, on_delete=models.CASCADE, related_name='flavor2',
                                verbose_name='Вкус')
    flavor1 = models.ForeignKey(Flavor, on_delete=models.CASCADE, related_name='flavor1',
                                verbose_name='Вкус')
    container = models.ForeignKey(Container, on_delete=models.CASCADE, verbose_name='Основа')
    total_price = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='Стоимость')
    ordered_at = models.DateTimeField(auto_now_add=True)

    def save(self):
        self.total_price = (
                self.topping.price + self.flavor3.price + self.flavor2.price +
                self.flavor1.price + self.container.price)
        return super().save()

    def __str__(self):
        flavors = self.flavor1.name + ', ' + self.flavor2.name + ', ' + self.flavor3.name
        topping = self.topping.name
        return f"Сливочное со вкусами: {flavors} в {self.container.name} с добавкой: {topping}"
