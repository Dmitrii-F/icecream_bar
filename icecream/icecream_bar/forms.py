from django import forms
from django.forms import ModelForm
from .models import IceCreamInContainer, Container, Topping
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')


class IceCreamInContainerForm(ModelForm):
    class Meta:
        model = IceCreamInContainer
        fields = ['topping', 'flavor3', 'flavor2', 'flavor1', 'container']


class ContainerForm(ModelForm):
    class Meta:
        model = Container
        fields = ['name', 'description']


class ToppingForm(ModelForm):
    class Meta:
        model = Topping
        fields = ['name', 'description']


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['user', 'status']


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Пароль должен состоять из латинских букв и цифр...',
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

# class SignUpForm(UserCreationForm):
#     phone_number = forms.CharField(
#         max_length=15,
#         help_text='Укажите номер телефона. Пример: +7-123-456-7890',
#         label='Номер телефона'
#     )
#     password1 = forms.CharField(
#         label='Пароль',
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
#         help_text='Пароль должен состоять из латинских букв и цифр...',
#     )
#     address = forms.CharField(
#         max_length=200,
#         help_text='Введите адрес для доставки',
#         label='Адрес'
#     )
#
#     class Meta:
#         model = User
#         fields = ['username', 'phone_number', 'password1', 'password2', 'address']