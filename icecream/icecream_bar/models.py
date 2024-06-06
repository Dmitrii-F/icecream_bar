from django.db import models
from django.contrib.auth.models import User

class Icecream(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(max_length=4)
    def __str__(self):
        return self.name

class Cup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(max_length=4)
    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(max_length=4)

    def __str__(self):
        return self.name



class Task(models.Model):
    # Кортеж из возможных статусов задачи
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('Completed', 'Завершена'),
    ]

    cup = models.ForeignKey(
        Cup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    icecream = models.ForeignKey(
        Icecream,
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
    task_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New'
    )
    assignee = models.ForeignKey(
        User,
        related_name='tasks',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


