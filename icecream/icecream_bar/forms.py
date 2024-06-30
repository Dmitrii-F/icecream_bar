from django import forms
from django.forms import ModelForm
from .models import IceCream, Cup, Topping, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')

class IceCreamForm(ModelForm):
    class Meta:
        model = IceCream
        fields = ['name', 'description', 'price']

class CupForm(ModelForm):
    class Meta:
        model = Cup
        fields = ['name', 'description', 'price']

class ToppingForm(ModelForm):
    class Meta:
        model = Topping
        fields = ['name', 'description', 'price']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_id', 'ice_cream', 'cup', 'topping', 'status']



class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        help_text='Укажите номер телефона. Пример: +7-123-456-7890',
        label='Номер телефона'
    )
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Пароль должен состоять из латинских букв и цифр...',
    )
    address = forms.CharField(
        max_length=200,
        help_text='Введите адрес для доставки',
        label='Адрес'
    )
    class Meta:
        model = User
        fields = ['username', 'phone_number', 'password1', 'password2', 'address']