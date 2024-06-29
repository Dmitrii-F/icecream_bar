from django.views import View
from django.views.generic import ListView, CreateView
from .models import IceCream, Cup, Topping, Order, User
from django.shortcuts import render, redirect
from .forms import FeedbackForm, OrderForm
from django.urls import reverse_lazy

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            return redirect('/')
    else:
        form = FeedbackForm()
    return render(request, 'icecream_bar/feedback.html', {'form': form})

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'icecream_bar/index.html')

class IceCreamsListView(ListView):
    model = IceCream
    template_name = 'icecream_bar/ice_creams_list.html'
    context_object_name = 'ice_creams_list'

class CupsListView(ListView):
    model = Cup
    template_name = 'icecream_bar/cups_list.html'
    context_object_name = 'cups_list'

class ToppingsListView(ListView):
    model = Topping
    template_name = 'icecream_bar/toppings_list.html'
    context_object_name = 'toppings_list'

class OrdersListView(ListView):
    model = Order
    template_name = 'icecream_bar/orders_list.html'
    context_object_name = 'orders_list'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'icecream_bar/order_create.html'
    success_url = reverse_lazy('icecream_bar:index')