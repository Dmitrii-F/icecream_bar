from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import IceCreamInContainer, Container, Topping


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


class UserInfoForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        label='Имя пользователя (username)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя пользователя'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите email'
        })
    )
    first_name = forms.CharField(
        max_length=150,
        label='Имя',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваше имя'
        })
    )
    last_name = forms.CharField(
        max_length=150,
        label='Фамилия',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите вашу фамилию'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UserPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=128,
        label='Старый пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите старый пароль'
        })
    )
    new_password1 = forms.CharField(
        max_length=128,
        label='Новый пароль',
        help_text=password_validation.password_validators_help_text_html(),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите новый пароль'
        })
    )
    new_password2 = forms.CharField(
        max_length=128,
        label='Подтверждение нового пароля',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Повторите новый пароль'
        })
    )


class SignUpForm(UserCreationForm):
    # Добавлен атрибут widget с CSS-классами и плейсхолдерами
    username = forms.CharField(
        max_length=150,
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',  # Добавлен класс form-control для Bootstrap стилизации
            'placeholder': 'Введите имя пользователя'  # Плейсхолдер для подсказки пользователю
        })
    )
    # Добавлен атрибут widget с CSS-классами и плейсхолдерами
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-3',  # Добавлен класс form-control для Bootstrap стилизации
            'placeholder': 'Введите email'  # Плейсхолдер для подсказки пользователю
        })
    )
    # Добавлен атрибут widget с CSS-классами и плейсхолдерами
    first_name = forms.CharField(
        max_length=150,
        label='Имя',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',  # Добавлен класс form-control для Bootstrap стилизации
            'placeholder': 'Введите ваше имя'  # Плейсхолдер для подсказки пользователю
        })
    )
    # Добавлен атрибут widget с CSS-классами и плейсхолдерами
    last_name = forms.CharField(
        max_length=150,
        label='Фамилия',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',  # Добавлен класс form-control для Bootstrap стилизации
            'placeholder': 'Введите вашу фамилию'  # Плейсхолдер для подсказки пользователю
        })
    )
    # Добавлен атрибут widget с CSS-классами и плейсхолдерами
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3',  # Добавлен класс form-control для Bootstrap стилизации
            'placeholder': 'Введите пароль'  # Плейсхолдер для подсказки пользователю
        }),
        help_text='',  # Убран стандартный текст подсказки
    )
    # Добавлен атрибут widget с CSS-классами и плейсхолдерами
    password2 = forms.CharField(
        label='Подтверждение пароля',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3',  # Добавлен класс form-control для Bootstrap стилизации
            'placeholder': 'Повторите пароль'  # Плейсхолдер для подсказки пользователю
        }),
        help_text='',  # Убран стандартный текст подсказки
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
