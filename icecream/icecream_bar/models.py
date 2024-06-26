from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class IceCream(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
    def __str__(self):
        return self.name

class Cup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
    def __str__(self):
        return self.name



class Order(models.Model):
    # Кортеж из возможных статусов заказа
    STATUS_CHOICES = [
        ('New', 'Новый'),
        ('Completed', 'Завершен'),
    ]

    cup = models.ForeignKey(
        Cup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    ice_cream = models.ForeignKey(
        IceCream,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    topping = models.ForeignKey(
        Topping,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    order_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New'
    )
    assignee = models.ForeignKey(
        User,
        related_name='orders',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.order_id)