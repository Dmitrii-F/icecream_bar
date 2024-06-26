from django import forms
from django.forms import ModelForm
from .models import IceCream, Cup, Topping, Order

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